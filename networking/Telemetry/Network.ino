#include "Constants.h"
#include "Network.h"

byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
};
IPAddress local_host(192, 168, 2, 5);

// for receiving commands over TCP
unsigned int local_tcp_port = 8001;
EthernetServer tcp_server(local_tcp_port);

// for sending data over UDP
IPAddress remote_host;
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
      Serial.print("ERROR: "); \
      Serial.println(e); \
      goto SLURP_INPUT; \
    } \
  } while(0)

  const char *error;
  error = read_tag(remote, tagbuf, bytes);
  CHECK(error);
  error = read_message(remote, msgbuf, bytes);
  CHECK(error);
  react(tagbuf, msgbuf);
  return;

#undef CHECK

SLURP_INPUT:
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

void react(char* tag, char* msg) {
  // TODO: actually react
}

void send_data() {
  static char packetBuffer[UDP_TX_PACKET_MAX_SIZE + 1] = "XXX"; // for testing
  // TODO: get data from subsystems and actually send it
}
