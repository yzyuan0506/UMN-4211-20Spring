from pox.core import core
import pox.openflow.libopenflow_01 as of


# Even a simple usage of the logger is much nicer than print!
log = core.getLogger()


# !!!!! PROJ3 Define your data structures here
# A hash table as the internal state of the controller
# The key of the table is the combination of switch ID and MAC address
# Each key is mapped to a port number 
keyToPort = {}

# Handle messages the switch has sent us because it has no
# matching rule.

def _handle_PacketIn (event):

  # get the port the packet came in on for the switch contacting the controller
  packetInPort = event.port

  # use POX to parse the packet
  packet = event.parsed

  # get src and dst mac addresses
  src_mac = str(packet.src)
  dst_mac = str(packet.dst)

  # get switch ID
  switchID = str(event.connection.dpid) + str(event.connection.ID)
  
  log.info('Packet has arrived: SRCMAC:{} DSTMAC:{} from switch:{} in-port:{}'.format(src_mac, dst_mac, switchID, packetInPort))

  # !!!!! PROJ3 Your logic goes here
  # map switch ID and source MAC address to the ingress port
  keyToPort[(switchID, src_mac)] = packetInPort

  # get the output port that the packet should be forwarded to
  outPort = keyToPort.get((switchID, dst_mac))

  # if the controller knows where the packet should be forwarded to
  if outPort != None:
    # instruct the switch to send the packet
    msg = of.ofp_packet_out(in_port=packetInPort, data=event.ofp)
    # attach an action, telling the switch to send the packet out on a defined outPort
    msg.actions.append(of.ofp_action_output(port=outPort))
    # send the command to the switch
    event.connection.send(msg)

    # send a flow table modification message to the switch
    msg = of.ofp_flow_mod()
    # set match fields: ingress port number, ethernet source address, ethernet destination address
    msg.match.in_port = packetInPort
    msg.match.dl_src = packet.src
    msg.match.dl_dst = packet.dst
    # append action indicating what port that packets will be sent on as part of the rule
    msg.actions.append(of.ofp_action_output(port=outPort))
    # send the command to the switch
    event.connection.send(msg)
  else:
    # tell the switch to flood the packet
    msg = of.ofp_packet_out(data=event.ofp)
    # flood the all interfaces except the ingress one
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    # send the command to the switch
    event.connection.send(msg)

def launch ():
  core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
  log.info("Pair-Learning switch running.")
