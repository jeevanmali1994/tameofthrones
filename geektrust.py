from input import input
from kingdom import kingdom
from communication import communication

def main():
    #this varibale stores all the kingdoms to a dictionary with Kingdom_name: kingdom_object pair
    all_kingdom_dictionary = get_all_kingdom_list()

    #this variable stores the sender of message
    sender = get_sender()

    # below two lines get the message list from this file
    inp = input()
    message_list = inp.read_input()
    
    #Here we create a list of communication object
    communication_list = []
    for destination, message in message_list:
        communication_object = communication(message, all_kingdom_dictionary[destination])
        communication_list.append(communication_object)
    
    #here we create the list of all allies
    senders_ally = []
    for communication_object in communication_list:
        if(communication_object.is_valid_message()):
            senders_ally.append(communication_object)
    
    if len(senders_ally) >= 3:
        print(sender, end = " ")
        for ally in senders_ally:
            print(ally.getname(), end = " ")
    else:
        print("NONE")
    
  


def get_all_kingdom_list(file_path = "kingdoms.txt"):
    file_open = open(file_path, "r")
    kingdoms = {}
    for line in file_open:
        kingdom_name, emblem = line.split()
        kingdoms[kingdom_name] = kingdom(kingdom_name, emblem)
    return kingdoms

def get_sender(file_path = "sender.txt"):
    file_open = open(file_path,"r")
    sender = ""
    for line in file_open:
        line = line.rstrip("\n")
        sender = line
    return sender

if __name__ == "__main__":
    main()    