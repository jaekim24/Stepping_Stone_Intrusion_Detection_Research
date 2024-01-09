import os 
import glob




#get rtt.txt with just time no dups
#create a list with the 
def just_get_rtt():
    rtt = []
    for out in glob.glob('Cluster/*/*/*/*' ):
        rtt_file = open(out[0:31]+ "rtt.txt",'w')
        print(out[0:30]+"rtt.txt")
        if(out.find("cluster.txt")):
            file = open(out,'r')
            #skips first line 
            file.readline()
            for line in file:
                print(line)
                if( line.find("*")):
                    print("clsoing")
                    file.close()
                    break
                else:
                    #gets the rtt from cluster.txt
                   # rtt_file.write(line[0:14])
                   print(line[0:14])

    rtt_file.close()









            

#need to access in a nested for loop 
# for each ( attack_x):
#     for each ( out_y ):
#            make /send/attack1/aws1/test1/only_send_packets.txt
#                 /send/attack1/aws1/test1/only_send_timestamps.txt

#                 /echo/attack1/aws1/test1/only_echo_packets.txt
#                 /echo/attack1/aws1/test1/only_echo_timestamps.txt

#cluster/attacker1/aws1/test01/insert send and echo timestamps
def traversing_the_directories():
    for out in glob.glob('coding_programs/analyzing_packets/*/*' ):
        if ("OUT" in out):
            
            #print(out)   

            #prints the list of non ack packets (so just send and echo packets)
            only_send_and_echo_packets = (removing_ack_packets(out))
            seperate_to_just_send_file_and_echo_file(only_send_and_echo_packets,out)
            
            #this seperates the sends and echos and creates the files
            #seperate_to_just_send_file_and_echo_file(removing_ack_packets,out)

            #must make a only_send_packets and a only_send_timestamps
            # and only_echo_packets and only_echo_timestamps


    






#this works! 
def removing_ack_packets(file_directory):
    list_of_send_and_echo_packets = []
    file_dir = open(str(file_directory),"r") 
    #opens the tcpdump file that has send, echo, and ack packets

    #lines = open("AWS1_OUT_Attack1_Test01.txt","r")  dont need to make a file anymore

    for a_line in file_dir:
        #if the packet is not ack then add it to the list of non ack packets
        #also have to account for finish packets "[F.]"
        if ( "[.]" not in a_line and "[F.]" not in a_line):
            list_of_send_and_echo_packets.append(a_line)
    #lines.close()  dont need to make a file anymore 
    return list_of_send_and_echo_packets


"""dont need this 
def creating_new_file_without_ack_packets():
    #outputs a txt file for the non ack packets
    with open('no_ack_packet_file.txt','w') as newfile :
        for a_packet in list_of_send_and_echo_packets:
            newfile.write(a_packet)
    newfile.close()
"""




def seperate_to_just_send_file_and_echo_file(list_of_send_and_echo_packets, current_path):
    #read the list that has the send and echo packets
    mixed_data_file = list_of_send_and_echo_packets
    mixed_data_file_ = list_of_send_and_echo_packets
    show_entire_path = str(current_path)

    #prints "Attack?" where ? is the number
    #it is okay to put indexes since there is only three attacks
    name_of_which_attack =  show_entire_path[47:54]
    #prints which aws?
    #cant just put the indexes bc theres AWS_ and CCT30
    name_of_which_aws_or_cct = show_entire_path[show_entire_path.find("AWS"):show_entire_path.find("AWS")+4]
    if(show_entire_path.find("AWS") == -1):
        if(show_entire_path.find("CCT30") != -1):
            name_of_which_aws_or_cct = "CCT30"
        elif(show_entire_path.find("AWS") != -1 ):
            name_of_which_aws_or_cct = show_entire_path[show_entire_path.find("AWS"):show_entire_path.find("AWS")+4]

    #prints which test num
    name_of_which_test_num = name_of_which_test_num = show_entire_path[show_entire_path.find("Test"):show_entire_path.find("Test")+6] 
    #if(show_entire_path.find("Test") != -1):
    #    name_of_which_test_num = show_entire_path[show_entire_path.find("Test"):show_entire_path.find("Test")+6]


    #takes in a parameter of the current path and use substring to abtain where it is located
    #example :coding_programs/analyzing_packets\OG_DONT_EDIT_Attack3\AWS6_OUT_Attack3_Test02.txt 
    #   want                                    "this           "and "this"        an "this "
    #after running once should look like this 
    
#                  /send/attack1/aws1/test1/only_send_packets.txt
#                 /send/attack1/aws1/test1/only_send_timestamps.txt

#                 /echo/attack1/aws1/test1/only_echo_packets.txt
#                 /echo/attack1/aws1/test1/only_echo_timestamps.txt


    if not os.path.exists("send/" + str(name_of_which_attack) +"/"+ str(name_of_which_aws_or_cct)+"/"+str(name_of_which_test_num)):
        os.makedirs("send/" + str(name_of_which_attack) +"/"+ str(name_of_which_aws_or_cct)+"/"+str(name_of_which_test_num))

    just_send_packets = open ("send/" + str(name_of_which_attack) +"/"+ str(name_of_which_aws_or_cct)+"/"+str(name_of_which_test_num)+"/" +"send_packets.txt", "w+")
    # making a file by extracting the send packets from the mixed_data_file
    # is a send: when the first IP address doesnt end with a 22 

    total_send_packets = 0 

    with open ("send/" + str(name_of_which_attack) +"/"+ str(name_of_which_aws_or_cct)+"/"+str(name_of_which_test_num)+"/" +"send_timestamps.txt", "w+") as send_timestamp_file:

        no_blank_line_send_timestamp = []

        for mixed_packet in mixed_data_file:
            # if destination IP address uses the 22 port then it is a send packet
            if ( mixed_packet.find('>') < mixed_packet.find('.22:') ):
                total_send_packets += 1 

                #if send packet insert to just_send_packets
                #making just_send_packet file
                just_send_packets.write(mixed_packet)       

                #creating send_timestamp file 
                send_timestamp = remove_the_dot(get_timestamp(mixed_packet))
                
                no_blank_line_send_timestamp.append(send_timestamp)
                no_blank_line_send_timestamp.append('\n')
                # send_timestamp_file.write(remove_the_dot(send_timestamp)+"\n")
            
            
        #remove blank line at the end
        for x in range(len(no_blank_line_send_timestamp)-1):
            send_timestamp_file.write(no_blank_line_send_timestamp[x])

        
    send_timestamp_file.close()
    just_send_packets.close()




    if not os.path.exists("echo/" + str(name_of_which_attack) +"/"+ str(name_of_which_aws_or_cct)+"/"+str(name_of_which_test_num)):
        os.makedirs("echo/" + str(name_of_which_attack) +"/"+ str(name_of_which_aws_or_cct)+"/"+str(name_of_which_test_num))


    just_echo_packets = open("echo/" + str(name_of_which_attack) +"/"+ str(name_of_which_aws_or_cct)+"/"+str(name_of_which_test_num)+"/" +"echo_packets.txt", "w")

    # is an echo: when the first IP address and if it ends in 22 it is an echo bc it came from the ssh server port

    no_blank_line_echo_timestamp = []

    with open ("echo/" + str(name_of_which_attack) +"/"+ str(name_of_which_aws_or_cct)+"/"+str(name_of_which_test_num)+"/" +"echo_timestamps.txt", "w") as echofile:
        for mixed_packet_of_echo_and_send in mixed_data_file_:
            # if source IP address uses the 22 port then it is an echo packet
            # if it cant find the string then it returns -1 
            if ( mixed_packet_of_echo_and_send.find('>') > mixed_packet_of_echo_and_send.find('.22 ') & mixed_packet_of_echo_and_send.find('.22 ') != -1 ):
                #if echo packet insert to just_echo_packets
                just_echo_packets.write(mixed_packet_of_echo_and_send)
                echo_timestamp = remove_the_dot(get_timestamp(mixed_packet_of_echo_and_send))
                #echofile.write(remove_the_dot(echo_timestamp)+"\n")

                no_blank_line_echo_timestamp.append(echo_timestamp)
                no_blank_line_echo_timestamp.append('\n')

        #remove blank line at the end
        for x in range(len(no_blank_line_echo_timestamp)-1):
            echofile.write(no_blank_line_echo_timestamp[x])


    echofile.close()
    just_echo_packets.close()

def remove_the_dot(timestamp):
    output = timestamp.replace(".","")
    return output

def get_timestamp(packet):
    output = packet[0:17]
    return output

def main():
    #removes ack packets and adds the non ack packets to a list
    #removing_ack_packets()
    #outputs a new file with the packets from the list 
    #creating_new_file_without_ack_packets()
    #seperate_to_just_send_file_and_echo_file()
    #traversing_the_directories()
    just_get_rtt()



main()

