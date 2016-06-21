#include <SPI.h> // needed for Arduino versions later than 0018
#include <Ethernet.h>
#include <EthernetUdp.h> // UDP library from: bjoern@cs.stanford.edu 12/30/2008

byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
};

// for receiving commands over TCP
IPAddress local_host(192, 168, 2, 5);
unsigned int local_port = 8001;
EthernetServer tcp_server(local_port);

// for sending data over UDP
IPAddress remote_host;
unsigned int remote_port;
EthernetUDP udp;

void setup() {
  Serial.begin(9600);
  while (!Serial)
    ;
  Ethernet.begin(mac, local_host);
  
  tcp_server.begin();
  Serial.print("server is at ");
  Serial.println(Ethernet.localIP());
}

void loop() {
  recv_command();
  send_data();
}

void recv_command() {
  static EthernetClient remote;

  if (!remote.connected()) {
    remote = tcp_server.available();
    if (remote)
      Serial.println("new client");
    else
      return;
  }

  int bytes = remote.available();
  if (bytes == 0)
    return;

  Serial.println("received data");
  // TODO: deal with client messages
  while (bytes-- > 0)
    Serial.write(remote.read());
  Serial.println();
}

void send_data() {
  static char packetBuffer[UDP_TX_PACKET_MAX_SIZE + 1] = "XXX"; // for testing
  // TODO: get data from subsystems and actually send it
  udp.write(packetBuffer);
}
