#include "Constants.h"
#include "Network.h"

#include <Ethernet.h>
#include <EthernetUdp.h> // UDP library from: bjoern@cs.stanford.edu 12/30/2008

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
