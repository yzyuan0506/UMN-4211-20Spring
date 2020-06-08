/*
* name: Zhiyuan Yang
* Zhang CSCI4211
* date: 15/03/2020
*/
---
### Compilation steps ###
Since Python is an interpreted language, users do not need to compile source files to executable.
However, users must have **Python 3** installed.
One can run:
```
python3 --version
```
As long as Python 3 is installed, you can go to the root folder and run:
```
python3 main.py
```

---

### Test cases ###
Totally six test cases were run for this program.

Test cases 1 - 3 are the tests for stop and wait version.
Test cases 4 - 6 are the tests for stop and wait version.

The settings of the simulator and output are as follows:

**Settings for test case 1**
In simulator.py,
```
self.lossprob = 0.5  # probability that a packet is dropped
self.corruptprob = 0.5  # probability that one bit is packet is flipped
self.Lambda = 1000 # arrival rate of messages from layer 5
self.nsimmax = 20  # number of msgs to generate, then stop
self.TRACE = 0  # for your debugging
```
**Output of test case 1**
```
data recieved：aaaaaaaaaaaaaaaaaaaa
data recieved：bbbbbbbbbbbbbbbbbbbb
data recieved：cccccccccccccccccccc
data recieved：dddddddddddddddddddd
data recieved：eeeeeeeeeeeeeeeeeeee
data recieved：ffffffffffffffffffff
data recieved：gggggggggggggggggggg
data recieved：hhhhhhhhhhhhhhhhhhhh
data recieved：iiiiiiiiiiiiiiiiiiii
data recieved：jjjjjjjjjjjjjjjjjjjj
data recieved：kkkkkkkkkkkkkkkkkkkk
data recieved：llllllllllllllllllll
data recieved：mmmmmmmmmmmmmmmmmmmm
data recieved：nnnnnnnnnnnnnnnnnnnn
data recieved：oooooooooooooooooooo
data recieved：pppppppppppppppppppp
data recieved：qqqqqqqqqqqqqqqqqqqq
data recieved：rrrrrrrrrrrrrrrrrrrr
data recieved：ssssssssssssssssssss
simulation end
```
**Settings for test case 2**
In simulator.py,
```
self.lossprob = 0.7  # probability that a packet is dropped
self.corruptprob = 0.7  # probability that one bit is packet is flipped
self.Lambda = 1000 # arrival rate of messages from layer 5
self.nsimmax = 20  # number of msgs to generate, then stop
self.TRACE = 0  # for your debugging
```
**Output of test case 2**
```
data recieved：aaaaaaaaaaaaaaaaaaaa
data recieved：bbbbbbbbbbbbbbbbbbbb
data recieved：cccccccccccccccccccc
data recieved：dddddddddddddddddddd
data recieved：eeeeeeeeeeeeeeeeeeee
data recieved：ffffffffffffffffffff
data recieved：gggggggggggggggggggg
data recieved：hhhhhhhhhhhhhhhhhhhh
data recieved：iiiiiiiiiiiiiiiiiiii
data recieved：jjjjjjjjjjjjjjjjjjjj
data recieved：kkkkkkkkkkkkkkkkkkkk
data recieved：llllllllllllllllllll
data recieved：mmmmmmmmmmmmmmmmmmmm
data recieved：nnnnnnnnnnnnnnnnnnnn
data recieved：oooooooooooooooooooo
data recieved：pppppppppppppppppppp
data recieved：qqqqqqqqqqqqqqqqqqqq
data recieved：rrrrrrrrrrrrrrrrrrrr
data recieved：ssssssssssssssssssss
simulation end
```

**Settings for test case 3**
In simulator.py,
```
self.lossprob = 0.9  # probability that a packet is dropped
self.corruptprob = 0.9  # probability that one bit is packet is flipped
self.Lambda = 1000 # arrival rate of messages from layer 5
self.nsimmax = 26  # number of msgs to generate, then stop
self.TRACE = 0  # for your debugging
```
**Output of test case 3**
```
data recieved：aaaaaaaaaaaaaaaaaaaa
data recieved：bbbbbbbbbbbbbbbbbbbb
data recieved：cccccccccccccccccccc
data recieved：dddddddddddddddddddd
data recieved：eeeeeeeeeeeeeeeeeeee
data recieved：ffffffffffffffffffff
data recieved：gggggggggggggggggggg
data recieved：hhhhhhhhhhhhhhhhhhhh
data recieved：iiiiiiiiiiiiiiiiiiii
data recieved：jjjjjjjjjjjjjjjjjjjj
data recieved：kkkkkkkkkkkkkkkkkkkk
data recieved：llllllllllllllllllll
data recieved：mmmmmmmmmmmmmmmmmmmm
data recieved：nnnnnnnnnnnnnnnnnnnn
data recieved：oooooooooooooooooooo
data recieved：pppppppppppppppppppp
data recieved：qqqqqqqqqqqqqqqqqqqq
data recieved：rrrrrrrrrrrrrrrrrrrr
data recieved：ssssssssssssssssssss
data recieved：tttttttttttttttttttt
data recieved：uuuuuuuuuuuuuuuuuuuu
data recieved：vvvvvvvvvvvvvvvvvvvv
data recieved：wwwwwwwwwwwwwwwwwwww
data recieved：xxxxxxxxxxxxxxxxxxxx
data recieved：yyyyyyyyyyyyyyyyyyyy
simulation end
```

**Settings for test case 4**
In simulator.py,
```
self.lossprob = 0.5  # probability that a packet is dropped
self.corruptprob = 0.5  # probability that one bit is packet is flipped
self.Lambda = 50000 # arrival rate of messages from layer 5
self.nsimmax = 20  # number of msgs to generate, then stop
self.TRACE = 0  # for your debugging
```
**Output of test case 4**
```
data recieved：aaaaaaaaaaaaaaaaaaaa
data recieved：bbbbbbbbbbbbbbbbbbbb
data recieved：cccccccccccccccccccc
data recieved：dddddddddddddddddddd
data recieved：eeeeeeeeeeeeeeeeeeee
data recieved：ffffffffffffffffffff
data recieved：gggggggggggggggggggg
data recieved：hhhhhhhhhhhhhhhhhhhh
data recieved：iiiiiiiiiiiiiiiiiiii
data recieved：jjjjjjjjjjjjjjjjjjjj
data recieved：kkkkkkkkkkkkkkkkkkkk
data recieved：llllllllllllllllllll
data recieved：mmmmmmmmmmmmmmmmmmmm
data recieved：nnnnnnnnnnnnnnnnnnnn
data recieved：oooooooooooooooooooo
data recieved：pppppppppppppppppppp
data recieved：qqqqqqqqqqqqqqqqqqqq
data recieved：rrrrrrrrrrrrrrrrrrrr
data recieved：ssssssssssssssssssss
simulation end
```
**Settings for test case 5**
In simulator.py,
```
self.lossprob = 0.7  # probability that a packet is dropped
self.corruptprob = 0.7  # probability that one bit is packet is flipped
self.Lambda = 50000 # arrival rate of messages from layer 5
self.nsimmax = 20  # number of msgs to generate, then stop
self.TRACE = 0  # for your debugging
```
**Output of test case 5**
```
data recieved：aaaaaaaaaaaaaaaaaaaa
data recieved：bbbbbbbbbbbbbbbbbbbb
data recieved：cccccccccccccccccccc
data recieved：dddddddddddddddddddd
data recieved：eeeeeeeeeeeeeeeeeeee
data recieved：ffffffffffffffffffff
data recieved：gggggggggggggggggggg
data recieved：hhhhhhhhhhhhhhhhhhhh
data recieved：iiiiiiiiiiiiiiiiiiii
data recieved：jjjjjjjjjjjjjjjjjjjj
data recieved：kkkkkkkkkkkkkkkkkkkk
data recieved：llllllllllllllllllll
data recieved：mmmmmmmmmmmmmmmmmmmm
data recieved：nnnnnnnnnnnnnnnnnnnn
data recieved：oooooooooooooooooooo
data recieved：pppppppppppppppppppp
data recieved：qqqqqqqqqqqqqqqqqqqq
data recieved：rrrrrrrrrrrrrrrrrrrr
data recieved：ssssssssssssssssssss
simulation end
```

**Settings for test case 6**
In simulator.py,
```
self.lossprob = 0.9  # probability that a packet is dropped
self.corruptprob = 0.9  # probability that one bit is packet is flipped
self.Lambda = 60000 # arrival rate of messages from layer 5
self.nsimmax = 26  # number of msgs to generate, then stop
self.TRACE = 0  # for your debugging
```
**Output of test case 6**
```
data recieved：aaaaaaaaaaaaaaaaaaaa
data recieved：bbbbbbbbbbbbbbbbbbbb
data recieved：cccccccccccccccccccc
data recieved：dddddddddddddddddddd
data recieved：eeeeeeeeeeeeeeeeeeee
data recieved：ffffffffffffffffffff
data recieved：gggggggggggggggggggg
data recieved：hhhhhhhhhhhhhhhhhhhh
data recieved：iiiiiiiiiiiiiiiiiiii
data recieved：jjjjjjjjjjjjjjjjjjjj
data recieved：kkkkkkkkkkkkkkkkkkkk
data recieved：llllllllllllllllllll
data recieved：mmmmmmmmmmmmmmmmmmmm
data recieved：nnnnnnnnnnnnnnnnnnnn
data recieved：oooooooooooooooooooo
data recieved：pppppppppppppppppppp
data recieved：qqqqqqqqqqqqqqqqqqqq
data recieved：rrrrrrrrrrrrrrrrrrrr
data recieved：ssssssssssssssssssss
data recieved：tttttttttttttttttttt
data recieved：uuuuuuuuuuuuuuuuuuuu
data recieved：vvvvvvvvvvvvvvvvvvvv
data recieved：wwwwwwwwwwwwwwwwwwww
data recieved：xxxxxxxxxxxxxxxxxxxx
data recieved：yyyyyyyyyyyyyyyyyyyy
simulation end
```

**Analysis**
We can see that even if the corrupted and lost probabilities of packet are high, the data are still transfered without disorder and corruption. That is because a reliable data transfer protocol is implemented in the program. Timer is set in A(sender). The timer will be triggered if a packet is lost, and then all the unacknowledged packets in the buffer will be resent. By comparing the computed checksum of a packet and its checksum field, we can know if a packet is corrupted. Corrupted packets will be discarded and NACK may be sent.

---

### Data structure ###

#### Stop and Wait Version ####

The class for **A (the sender)** has the following fields:
- state: state of the sender, WAIT_LAYER5 or WAIT_ACK
- estimated_rtt: estimated round time trip delay, used for setting timer
- seq: the sequence number of the next packet to be sent

The class for **B (the reciever)** has the following fields:
- state: the expected sequence number for the imcoming packet 

---

#### Go back N Version ####

The class for **A (the sender)** has the following fields:
- base: the sequence number of the oldest unacknowleged packet
- next_seq: the sequence number of the next packet to be sent
- estimated_rtt: estimated round time trip delay, used for setting timer
- self.win_size: size of the sliding window, also the size of circular buffer
- self.cir_buf: a circular buffer that is used for caching packets

The class for **B (the reciever)** has the following fields:
- expected_seq: the expected sequence number for the imcoming packet

---

### Functions or methods ###

#### Stop and Wait Version ####

**Intitialization of A**:
Intialize the `state` of the sender as WAIT_LAYERS and set `estimated_rtt` to be 30. Also, the first sequence number `seq` would be 0.

**A_output()**:
If the current state is WAIT_LAYER5, A will pick up a data from layer 5. Then A would make up a packet with `seq` 1 or 0 and send to B. After the package is sent, A will start a timer and turn in the state of WAIT_ACK.

**A_input**:
If A is waiting for acknowlegement from B, it will first verify the arrived acknowledgement packet by checksum and sequence number. If the packet is the one A wants, it will remove the timer and turn into state WAIT_LAYER5

**A_handle_timer**:
When the timer goes off, A will resent the previous packet to B.

**Initialization of B**:
Initialize `state` with 0, it means that B is expecting packet with sequence number 0.

**B_input**:
B will verify the arriving packet by checksum and sequence number. If the packet is good, the packet will be sent to upper layer 5 and send a new acknowlegment to A. Otherwise, B will send the old ack packet to A.

---

#### Go back N Version ####

**Intitialization of A**:
Intialize `base` and `next_seq` to be 0 because base and next_seq should be equal at first. `estimated_rtt` is estimated to be 30 and `win_size` is initialzed to be 8. `cir_buf` is initialized with size 8 because it has to have the same size as the sliding window

**A_output()**:
If the circular buffer is not full, this function will receive message from upper layer 5 and save it in the circular buffer. Then the packet will be sent to B(the reciever). After a packet is sent, a timer will be started to make sure the packet would arrive at the receiver side. Messages from the upper layer 5 may be discarded if the buffer has been full.

**A_input**:
This function will be triggered when a ACK packet is arrived at A. A will dicard all the corrupted packets by computing the checksum. `base` will be updated according to the ack number of the incoming packet. All the packets that have a lower sequence number than `base` will be poped out from the circular buffer since we know that those packets have been acknowledged.

**A_handle_timer**:
This function will be triggered when the timer goes off, which means some packets in the buffer have not been acknowledged in a given amount of time. Then the function will resend all the packets that have not been acknowledged and set a new timer for those packets

**Initialization of B**:
`expected_seq` will be initialzed to be 0, which is as same as the first sequence number of packets from A, for convenience. In real world, the reciever and sender may need to synchronize their sequence number first.

**B_input**:
This function will be triggered when a packet arrives at B. B will check if the packet is corrupted and has the expected sequence number. If not, B will resend the last ACK packet to A. If the packet is uncorrupted and expected, B will send the packet to the upper layer 5 and send a new ACK to A and update its `expected_seq`.




