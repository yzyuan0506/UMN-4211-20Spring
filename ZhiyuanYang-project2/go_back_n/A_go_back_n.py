# Zhiyuan Yang, Zhang CSCI4211, 15/03/2020
# Spring 2020 CSci4211: Introduction to Computer Networks
# This program serves as the sender of GBN protocol.
# Written in Python v3

from pj2.simulator import sim
from pj2.simulator import to_layer_three
from pj2.event_list import evl
from pj2.packet import *
from pj2.circular_buffer import circular_buffer

class A:
    def __init__(self):
        # base: the sequence number of the oldest unacknowleged packet
        # next_seq: the sequence number of the next packet to be sent
        self.base = 0
        self.next_seq = 0
        self.estimated_rtt = 30
        self.win_size = 8
        self.cir_buf = circular_buffer(self.win_size)
        return

    def A_input(self, pkt):
        # process the ACK, NACK from B
        if pkt.checksum == pkt.get_checksum():
            next_base = pkt.acknum + 1
            # pop out all the acknowleged packets
            while self.base < next_base:
                self.cir_buf.pop()
                self.base = self.base + 1
            # remove timer if packets in the current window are all recieved
            if self.base == self.next_seq:
                evl.remove_timer()

    def A_output(self, m):
        if not self.cir_buf.isfull():
            pkt = packet(seqnum=self.next_seq, payload=m)
            to_layer_three("A", pkt)
            # Save the packet to circular buffer
            self.cir_buf.push(pkt)
            # Start the timer
            evl.start_timer("A", self.estimated_rtt)
            self.next_seq = self.next_seq + 1

    def A_handle_timer(self):
        for pkt in self.cir_buf.read_all():
            # resend the packets that are haven't been acknownleged
            if pkt.seqnum >= self.base:
                to_layer_three("A", pkt)
        # Set a new timer after packets are resent
        evl.start_timer("A", self.estimated_rtt)


a = A()
