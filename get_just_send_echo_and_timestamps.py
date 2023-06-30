

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
    #outputs a txt file for the non ack packets
    with open('no_ack_packet_file.txt','w') as newfile :
        for a_packet in list_of_send_and_echo_packets:
            newfile.write(a_packet)
    newfile.close()




def seperate_to_just_send_file_and_echo_file():
    #read the file that has the send and echo packets
    mixed_data_file = open("no_ack_packet_file.txt","r")
    just_send_packets = open ("just_send_packets.txt", "w")
    # making a file by extracting the send packets from the mixed_data_file
    # is a send: when the first IP address doesnt end with a 22 
    with open ('send_timestamp.txt','w') as sendfile:
        for mixed_packet in mixed_data_file:
            # if destination IP address uses the 22 port then it is a send packet
            if ( mixed_packet.find('>') < mixed_packet.find('.22:')):
                #if send packet insert to just_send_packets
                just_send_packets.write(mixed_packet)       
                send_timestamp = get_timestamp(mixed_packet)
                sendfile.write(remove_the_dot(send_timestamp)+"\n")

    sendfile.close()
    just_send_packets.close()
    mixed_data_file.close()

    mixed_data_file = open("no_ack_packet_file.txt","r")
    just_echo_packets = open("just_echo_packets.txt","w")

    # is an echo: when the first IP address and if it ends in 22 it is an echo bc it came from the ssh server port
    with open ('echo_timestamp.txt','w') as echofile:
        for mixed_packet_of_echo_and_send in mixed_data_file:
            # if source IP address uses the 22 port then it is an echo packet
            # if it cant find the string then it returns -1 
            if ( mixed_packet_of_echo_and_send.find('>') > mixed_packet_of_echo_and_send.find('.22 ') & mixed_packet_of_echo_and_send.find('.22 ') != -1 ):
                #if echo packet insert to just_echo_packets
                just_echo_packets.write(mixed_packet_of_echo_and_send)
                echo_timestamp = get_timestamp(mixed_packet_of_echo_and_send)
                echofile.write(remove_the_dot(echo_timestamp)+"\n")

    echofile.close()
    just_echo_packets.close()
    mixed_data_file.close()

def remove_the_dot(timestamp):
    output = timestamp.replace(".","")
    return output

def get_timestamp(packet):
    output = packet[0:17]
    return output

def main():
    #removes ack packets and adds the non ack packets to a list
    removing_ack_packets()
    #outputs a new file with the packets from the list 
    creating_new_file_without_ack_packets()


    seperate_to_just_send_file_and_echo_file()

main()

