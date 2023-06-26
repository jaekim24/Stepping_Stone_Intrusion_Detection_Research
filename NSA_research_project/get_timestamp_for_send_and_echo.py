def seperate_to_just_send_file_and_echo_file():
    #read the file that has the send and echo packets
    mixed_data_file = open("no_ack_packet_file.txt","r")

    # making a file by extracting the send packets from the mixed_data_file
    # is a send: when the first IP address doesnt end with a 22 
    with open ('send_timestamp.txt','w') as sendfile:
        for mixed_packet in mixed_data_file:
            # if destination IP address uses the 22 port then it is a send packet
            if ( mixed_packet.find('>') < mixed_packet.find('.22:')):
                #sendfile.write(mixed_packet)       
                send_timestamp = get_timestamp(mixed_packet)
                sendfile.write(remove_the_dot(send_timestamp)+"\n")

    sendfile.close()
    mixed_data_file.close()

    mixed_data_file = open("no_ack_packet_file.txt","r")
    # is an echo: when the first IP address and if it ends in 22 it is an echo bc it came from the ssh server port
    with open ('echo_timestamp.txt','w') as echofile:
        for mixed_packet_of_echo_and_send in mixed_data_file:
            # if source IP address uses the 22 port then it is an echo packet
            # if it cant find the string then it returns -1 
            if ( mixed_packet_of_echo_and_send.find('>') > mixed_packet_of_echo_and_send.find('.22 ') & mixed_packet_of_echo_and_send.find('.22 ') != -1 ):
                #echofile.write(mixed_packet_of_echo_and_send)
                echo_timestamp = get_timestamp(mixed_packet_of_echo_and_send)
                echofile.write(remove_the_dot(echo_timestamp)+"\n")

    echofile.close()
    mixed_data_file.close()

def remove_the_dot(timestamp):
    output = timestamp.replace(".","")
    return output

def get_timestamp(packet):
    output = packet[0:17]
    return output

def main():
    seperate_to_just_send_file_and_echo_file()

main()

