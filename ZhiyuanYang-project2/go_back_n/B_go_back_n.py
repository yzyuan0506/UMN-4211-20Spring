from pj2.simulator import to_layer_five
from pj2.packet import *


class B:
    def __init__(self):
        # stop and wait, the initialization of B
        # The state only need to maintain the information of expected sequence number of the packet
        self.state = 0
    def output(self, m):
        return
    def B_input(self, pkt):
        # stop and wait, B_input
        # you need to verify the checksum to make sure that packet isn't corrupted
        # If the packet is either corrupted or not the expected one
        # If the packet is the right one, you need to pass to the fifth layer "using to_layer_five(entity,payload)"
        # Send acknowledgement using "send_ackt(entity,seq)" based on the correctness of received packet
        # If the packet is the correct one, in the last step, you need to update its state ( update the expected sequence number)
        if (pkt.checksum != pkt.get_checksum()) or (pkt.seqnum == 1 - self.state):
            old_ack = packet(acknum=1-self.state)
            to_layer_three("B", old_ack)
            return
        if (pkt.checksum == pkt.get_checksum()) and (pkt.seqnum == self.state):
            to_layer_five("B", pkt.payload.data)
            send_ack("B", self.state)
            self.state = 1 - self.state

    def B_handle_timer(self):
        return

b = B()