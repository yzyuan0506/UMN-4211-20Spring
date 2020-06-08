from pj2.simulator import to_layer_three
class packet:
    def __init__(self, seqnum=0, acknum=0, payload=0):
        self.seqnum = seqnum
        self.acknum = acknum
        self.payload = payload
        self.checksum=0
        self.checksum = self.get_checksum()

    def get_checksum(self):
        # map the packet data to an integer
        checksum=0
        if self.payload!=0:
            for i in range(20):
                checksum= checksum + ord(self.payload.data[i])
        checksum = checksum+self.seqnum+self.acknum
        return checksum

def send_ack(AorB,ack):
    pkt=packet(acknum=ack)
    pkt.checksum=pkt.get_checksum()
    to_layer_three(AorB,pkt)
