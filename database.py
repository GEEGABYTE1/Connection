import time
from graph import Graph
from script import Prompt
from double_ll import DoubleLinkedList

server_base = DoubleLinkedList()


def initial_prompt(server_base=server_base):
    print('Welcome to Connection! ')
    print("You have 5 options: ")
    time.sleep(0.1)
    print("-"*24)
    print('/add_server: To add a new server to track your modems/routers')
    time.sleep(0.2)
    print('-'*24) 
    print('/remove_server: To remove a server/network from the software')
    time.sleep(0.2)
    print("-"*24)
    print("/view_servers: To view all the servers registered in the software ")
    time.sleep(0.2)
    print('-'*24)
    print("/access_server: To analyze and access one of the servers registered on the server" )
    time.sleep(0.2)
    print('-'*24)
    print("/quit: To quit the program")
    

    start = True 
    while start:
        print('\n')
        user_prompt = input(':')
        
        if user_prompt == '/add_server':
            server_name = input('Please type in the name of the server: ')
            
            if not server_name in server_base.nodes:
                server_extra_info = input('Is there any other extra info you would like to add (*Type \'None\' if not applicable): ')
                
                if server_extra_info == None:
                    new_server = [server_name, Graph()]
                else:
                    new_server = [server_name, Graph(), server_extra_info]

                server_base.add_to_tail(new_server)
                time.sleep(0.2)
                print("Your Server has been added. To view it, please type \'/view_servers\' or to access it, type \'/access_server\'")
            else:
                print("That server is already registered in the software")
                time.sleep(0.1)
                print('We recommend to type \'/view_servers\' to view all the servers you have added.')

        elif user_prompt == '/remove_server':
            server_name = input('Please type in the name of the server: ')
            if len(server_base.nodes) == 0:
                print("There is no server to remove as the software has not registered anything yet! ")
                time.sleep(0.1)
            elif not server_name in server_base.nodes:
                print("That server does not seem to be registered in this software currently ")
                time.sleep(0.1)
                print("We recommend to type \'/add_server\' to do so ")
                time.sleep(0.1)
        
            else:
                server_base.remove_by_value(server_name)
                server_base.nodes.remove(server_name)
                time.sleep(0.1)
                print('Server has been successfully deleted ')
        
        elif user_prompt == '/view_servers':
            if len(server_base.nodes) == 0:
                print("There currently is no server registered on the software yet. ")
                time.sleep(0.2)
                print("We recommend to type \'/add_server\' to add a new server to the software ")
            else:
                print('Here are your current servers: ')
                server_base.stringify_list()

        
        elif user_prompt == "/access_server":
            server_name = input('Please type in the name of the server: ')
            if not server_name in server_base.nodes:
                print("That server does not seem to be registered in this software currently ")
                time.sleep(0.1)
                print("We recommend to type \'/add_server\' to do so ")
                time.sleep(0.1)
            else:
                current_server = server_base.linear_search(server_name)
                time.sleep(0.1)
                test = Prompt(current_server[1])
                print("You have succesfully loaded into the server. ")
                time.sleep(0.2)
                try:
                    print('EXTRA INFO: {}'.format(current_server[2]))
                except IndexError:
                    pass
                print()
                print(test.database())
        
        elif user_prompt == "/quit":
            print('You have quit the software. ')
            break 
        else:
            print("That command seems to be invalid ")



print(initial_prompt())