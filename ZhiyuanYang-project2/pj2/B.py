# Zhiyuan Yang, Zhang CSCI4211, 15/03/2020
# Spring 2020 CSci4211: Introduction to Computer Networks
# This program serves as the receiver of GBN protocol.
# Written in Python v3

from pj2.simulator import to_layer_five
from pj2.packet import send_ack

class B:
    def __init__(self):
        self.expected_seq = 0

    def B_input(self, pkt):
        # check if the imcoming packet is uncorrupted and expected
        if (pkt.checksum == pkt.get_checksum()) and (pkt.seqnum == self.expected_seq):
            to_layer_five("B", pkt.payload.data)
            send_ack("B", self.expected_seq)
            self.expected_seq = self.expected_seq + 1
        # if not, send the ACK for the last acknowledged packet(serve as NACK)
        else:
            send_ack("B", self.expected_seq - 1)

    def B_output(self, m):
        return

    def B_handle_timer(self):
        return


b = B()

