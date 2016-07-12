#ifndef NETWORK_H
#define NETWORK_H

#include "Readers.h"
#include "Writers.h"

#include <Ethernet.h>
//#include <oneCAN.h>

extern byte mac[];
extern IPAddress local_host;
//extern oneCAN can;

// These must be visible to setup().
extern unsigned int local_tcp_port;
extern EthernetServer tcp_server;
extern EthernetUDP udp_client;
extern unsigned int local_udp_port;

void recv_command();
void send_data();

#endif
