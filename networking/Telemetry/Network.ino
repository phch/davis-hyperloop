#include "Constants.h"
#include "Network.h"
#include "Debug.h"

byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
};
IPAddress local_host(192, 168, 2, 5);
IPAddress remote_host;

// for receiving commands over TCP
unsigned int local_tcp_port = 8001;
EthernetServer tcp_server(local_tcp_port);

// for sending data over UDP
unsigned int local_udp_port = 8002;
unsigned int remote_udp_port;
EthernetUDP udp_client;

void recv_command() {
  static EthernetClient remote;
  if (!remote.connected()) {
    remote = tcp_server.available();
    if (remote)
      Serial.println("new client");
    else
      return;
  }
  read_and_react(remote);
}

void read_and_react(EthernetClient& remote) {
  static char tagbuf[MAX_TAG_LEN + 1];
  static char msgbuf[MAX_MESSAGE_LEN + 1];

  int bytes = remote.available();
  if (bytes == 0)
    return;
  Serial.println("received data");

#define CHECK(e) \
  do { \
    if (e) { \
      DEBUG_PRINT(e); \
      goto FLUSH_INPUT; \
    } \
  } while(0)

  const char *error;
  error = read_tag(remote, tagbuf, bytes);
  CHECK(error);
  error = read_message(remote, msgbuf, bytes);
  CHECK(error);
  react(remote, tagbuf, msgbuf);
  return;

#undef CHECK

FLUSH_INPUT:
  for (; bytes > 0; bytes--)
    remote.read();
}

const char* read_tag(EthernetClient& remote, char* buf, int& bytes) {
  int i;
  char c;
  for (i = 0; i < MAX_TAG_LEN; i++) {
    if (bytes == 0)
      goto NO_COLON;
    c = remote.read();
    --bytes;
    if (c == ':')
      goto OK_TAG;
    buf[i] = c;
  }
  return "tag too long";

NO_COLON:
  return "no colon tag terminator";

OK_TAG:
  buf[i] = '\0';
  Serial.print("tag: ");
  Serial.println(buf);
  return 0;
}

const char* read_message(EthernetClient& remote, char* buf, int& bytes) {
  int i;
  for (i = 0; i < MAX_MESSAGE_LEN; i++, bytes--) {
    if (bytes == 0)
      goto OK_MESSAGE;
    buf[i] = remote.read();
  }
  return "message too long";

OK_MESSAGE:
  buf[i] = '\0';
  Serial.print("message: ");
  Serial.println(buf);
  return 0;
}

void react(EthernetClient& remote, char* tag, char* msg) {
  static char packetBuffer[MAX_PACKET_LEN];
  if (tag[0] == '?')
    tag[0] = '!';
  struct reader_entry *e = (struct reader_entry *)
    bsearch(tag, readers, reader_count, sizeof(struct reader_entry), find_tag);
  if (e == 0) {
    DEBUG_PRINT("unrecognized tag");
    return;
  }
  // TODO: print the tag here?
  e->reader(msg, packetBuffer);
  remote.println(packetBuffer);
}

void send_data() {
  static bool connected = false;
  static char packetBuffer[MAX_PACKET_LEN] = "XXX"; // for testing

  // Search for a client trying to connect.
  int bytes = udp_client.parsePacket();
  if (bytes > 0) {
    remote_host = udp_client.remoteIP();
    remote_udp_port = udp_client.remotePort();
    connected = true;
  }
  if (!connected)
    return;

  int ok;
  for (size_t i = 0; writers[i].tag != 0; i++) {
    ok = udp_client.beginPacket(remote_host, remote_udp_port);
    if (!ok) {
      DEBUG_PRINT("could not connect to remote host");
      return;
    }
    writers[i].writer(packetBuffer);
    udp_client.write(packetBuffer);
    ok = udp_client.endPacket();
    if (!ok) {
      DEBUG_PRINT("failed to write packet");
      return;
    }
  }
}
