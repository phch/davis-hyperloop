/*
 * This is a slightly modified version of UDPSendReceiveString.

 UDPSendReceiveString:
 This sketch receives UDP message strings, prints them to the serial port
 and sends an "acknowledge" string back to the sender

 A Processing sketch is included at the end of file that can be used to send
 and received messages for testing with a computer.

 created 21 Aug 2010
 by Michael Margolis

 This code is in the public domain.
 */

#include <SPI.h> // needed for Arduino versions later than 0018
#include <Ethernet.h>
#include <EthernetUdp.h> // UDP library from: bjoern@cs.stanford.edu 12/30/2008

byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
};
IPAddress ip(192, 168, 2, 5);

unsigned int localPort = 8888;

// buffers for receiving and sending data
char packetBuffer[UDP_TX_PACKET_MAX_SIZE + 1];
char replyBuffer[] = "ACK\n";

// An EthernetUDP instance to let us send and receive packets over UDP
EthernetUDP Udp;

void setup() {
  Serial.begin(9600);
  while(!Serial);
  Serial.print("Establishing Network Connection...");
  Ethernet.begin(mac, ip);
  Serial.println("OK!");
  Udp.begin(localPort);
}

void loop() {
  // if there's data available, read a packet
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    Serial.print("Received packet of size ");
    Serial.println(packetSize);
    Serial.print("From ");
    IPAddress remote = Udp.remoteIP();
    printIPAddress(remote);
    Serial.print(", port ");
    Serial.println(Udp.remotePort());
    Serial.println("Contents:");
    printPacket(packetSize);

    // send a reply to the IP address and port that sent us the packet we received
    Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
    Udp.write(replyBuffer);
    Udp.endPacket();
  }
  delay(10);
}

void printPacket(int packetSize) {
  int readSize;
  while (packetSize > 0) {
    readSize = Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
    packetBuffer[readSize] = '\0';
    Serial.print(packetBuffer);
    packetSize -= readSize;
  }
  Serial.println();
}

void printIPAddress(IPAddress ip) {
  for (int i = 0; i < 3; i++) {
    Serial.print(ip[i], DEC);
    Serial.print('.');
  }
  Serial.print(ip[3], DEC);
}
