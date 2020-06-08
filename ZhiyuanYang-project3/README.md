/*
* name: Zhiyuan Yang
* Zhang CSCI4211
* date: 19/04/2020
*/

### Ethernet Algorithm ###

I implemented a self-learning ehternet algorithm for the controller, which is in ethernet-learning.py

**Data structure**
In the algorithm, I create a hash table as the internal state of the controller.

A hash table is a data structure that implements an associative array abstract data type, a structure that can map keys to values.

In the hash table I created for the controller, the key of the table is the combination of switch ID and MAC address. Each key is mapped to a port.

With this hash table, the controller can learn where an incoming packet should be forwarded to by mapping the source MAC address and the switch ID. So that the controller can instruct the switch how to forward the packet and avoid flooding.

### Pseudocode ###

algorithm ethernet-learning (event):

variables:
    event: event is the input of the algorithm. Information such as packet, switchID and etc. can be extracted from event

    packet: the packet came in on for the switch contacting the controller

    keyToPort: a hash table that serves as the internal state of the controller

    switchID: id # of the switch contacting the controller

procedures:
    // update internal state
    keyToPort[(switchID, packet.src_mac)] = event.port

    // the controller knows what to do
    If (switchID, packet.dst_mac) in keyToPort:
        // telling switch to send a packet to the destination port
        desPort = keyToPort[(switchID, packet.dst_mac)]
        event.send(packet, desPort)

        // adding a flow to a switch, create a flow that matches inport #, destination MAC address and source MAC address
        msg = new flow()
        msg.match.in_port = packetInPort
        msg.match.dl_src = packet.src
        msg.match.dl_dst = packet.dst
        event.send(msg)
    Else:
        // instruct the switch to flood all ports except for the ingress port
        event.send(flood)