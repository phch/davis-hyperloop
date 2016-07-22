#include "Constants.h"
#include "Debug.h"
#include "Network.h"

#include <Ethernet.h>
#include <EthernetUdp.h> // UDP library from: bjoern@cs.stanford.edu 12/30/2008
#include <SPI.h>

oneCAN can;

void setup() {
  Serial.begin(9600);
  while (!Serial)
    ;
  can.init();
  can.beginReceiving();

  prepare_readers();
  prepare_writers();

  Ethernet.begin(mac, local_host);

  tcp_server.begin();
  Serial.print("server is at ");
  Serial.println(Ethernet.localIP());

  int ok = udp_client.begin(local_udp_port);
  if (!ok) {
    Serial.println("no sockets available to use");
    for (;;)
      ;
  }
  debug("complete\n");
}

void loop() {
  recv_command();
  if (can.dataAvailable)
    can.getData();
  send_data();
}
