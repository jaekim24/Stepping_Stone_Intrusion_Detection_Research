
list_of_send_and_echo_packets = []

def removing_ack_packets():
    #opens the tcpdump file that has send, echo, and ack packets
    lines = open("AWS1_OUT_Attack1_Test01.txt","r") 
    for a_line in lines:
        #if the packet is not ack then add it to the list of non ack packets
        if ( "[.]" not in a_line):
            list_of_send_and_echo_packets.append(a_line)
    lines.close()

def creating_new_file_without_ack_packets():
    #creating a txt file for the non ack packets
    with open('no_ack_packet_file.txt','w') as newfile :
        for a_packet in list_of_send_and_echo_packets:
            newfile.write(a_packet)
    newfile.close()


def main():
    removing_ack_packets()
    creating_new_file_without_ack_packets()

main()