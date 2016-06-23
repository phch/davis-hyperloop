#ifndef NETWORK_H
#define NETWORK_H

#include <Ethernet.h>

extern byte mac[];
extern IPAddress local_host;

// These must be visible to setup().
extern unsigned int local_tcp_port;
extern EthernetServer tcp_server;

void recv_command();
void send_data();

#endif
