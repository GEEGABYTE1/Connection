from pattern_search import pattern_search
#from database import current_server
from vertex import Vertex
import hashlib
import time 
import random 




class Prompt:

    def __init__(self, wifibase):
        self.wifibase = wifibase                   # Returned Graph of the search algorithm 
        self.unregistered_modems = [] 
        self.registered_modems = []
        self.latency = 0

    def database(self):
        
        playing = True 
        while playing:
            print('\n')
            prompt = input(':')

            if prompt == '/add_modem':
                name = input('Name of the modem: ')
                ip_address = input('First 5 characters of the Ip address (Include Periods, but they do not count as a character): ')
                if len(ip_address) > 6 or not '.' in ip_address:
                    print("Looks like the Ip Adress you have prompted exceeds the 5 character limit or does not follow the following format.")
                    time.sleep(0.1)
                    print('-'*7)
                    print("The format should be: 123.45 ")
                    print('-'*7)
                    time.sleep(0.1)
                    print('You have printed: {}'.format(ip_address))
                else:
                    ip_address = ip_address.encode()
                    ip_address = hashlib.sha224(ip_address).hexdigest()

                    validation = False 
                    
                    for i in self.unregistered_modems:
                        if len(self.unregistered_modems) == 0:
                            break 
                        elif i.value[-1] == ip_address:
                            validation = True 
                        elif i.value[0] == name:
                            validation = True
                            break
                        else:
                            continue 

                    if validation == True:
                        print("There is already a modem that either has the same name or same ip address in our database")
                        time.sleep(0.1)
                        
                    else:
                        modem_list = [name, ip_address]
                        vertex_modem = Vertex(modem_list)
                        self.unregistered_modems.append(vertex_modem)
                        time.sleep(0.1)
                        print('New Modem added. Type \'/register\' to register the modem in to the system')
            
            elif prompt == "/register":
                modem_name = input('Name of the modem: ')
                validation = False 
                modem = None
                for i in self.unregistered_modems:
                    if i.value[0] == modem_name:
                        validation = True 
                        modem = i
                        break
                    else:
                        continue 

                if validation == False:
                    print('That modem does not seem to be added into the software. Please type \'/add_modem\' to add the modem first')
                else:

                    if len(list(self.wifibase.graph_dict.keys())) == 0:
                        print('This is the first modem in the server, hence, there will be no links')
                        time.sleep(0.01)
                        self.wifibase.add_vertex(modem)
                        self.registered_modems.append(modem)
                        print('Modem added')
                        self.unregistered_modems.remove(modem)
                        time.sleep(0.1)
                        print('Once there are more modems (>1) defined in the software, you will be able to add links')
                    else:
                        for wifi in list(self.wifibase.graph_dict.keys()):
                            print('-'*24)
                            print(wifi)
                        
                        temp_modem_names = list(self.wifibase.graph_dict.keys())
                        print('-'*24)
                        print()
                        
                        print("Here are the modem(s) that are in the server ")
                        time.sleep(0.1)
                        router_name = input('Please enter one of the modem\'s name exactly to add a link. If you wish to have no link, please type \'None\': ')

                        if router_name == "None" or router_name == "None ":                       # If the user wants no link
                            self.wifibase.add_vertex(modem)
                            self.registered_modems.append(modem)
                            print('Modem added with no link ')
                            self.unregistered_modems.remove(modem)
                            time.sleep(0.1)
                        

                        elif not router_name in temp_modem_names:                                     # If the link is not even defined 
                            print('That router does not seem to be in the sever ')
                            time.sleep(0.1)
                        
                        
                        elif router_name in temp_modem_names:                                       # If link is defined
                            link_router = None 
                            for data, vertex in self.wifibase.graph_dict.items():
                                if data == router_name:
                                    link_router = vertex 
                                    break 
                                else:
                                    continue 
                            
                            miliseconds = random.randint(1, 2500)
                            self.latency += miliseconds 
                            self.wifibase.add_vertex(modem)
                            self.registered_modems.append(modem)
                            self.wifibase.add_edge(modem, link_router, miliseconds)

                            print('\'{modem1}\' is linked to \'{modem2}\' with a return speed of {latency} m/s '.format(modem1=modem.value[0], modem2=link_router.value[0], latency=miliseconds))
                            self.unregistered_modems.remove(modem)


            elif prompt == "/check_link":
                for i in self.registered_modems:
                    print("-"*24)
                    print(i.value[0])
                    time.sleep(0.1)
                print("-"*24)
                print("Here are the current registered modems on the server")
                modem_one = input("Plese enter the first modem name: ")
                modem_two = input('Please enter the second modem name: ' )

                time.sleep(0.1)
                #modem_one = self.wifibase.graph_dict[modem_one]
                #modem_two = self.wifibase.graph_dict[modem_two]

                print('Finding if there is a link between the two modems... ')
                
                for i in range(3):
                    print("...")
                    time.sleep(0.2)
                
                self.wifibase.find_path(modem_one, modem_two)

            elif prompt == "/check_total_latency":
                time.sleep(0.1)
                print('-'*24)
                print('Total Latency of Network: {}'.format(self.latency))
                print('-'*24)
                print('Average Latency of Network: {}'.format(self.latency/len(self.registered_modems)))

            elif prompt == "/delete":
                time.sleep(0.1)
                deleted_modem = input("Please enter a modem you want to delete: ")
                
                if len(list(self.wifibase.graph_dict.keys())) == 0:
                    print("There is no modem to remove as the server is empty! ")
                else:
                    
                    modem_checker = None
                    modem_vertex = None
                    for name, vertex in self.wifibase.graph_dict.items():
                        if deleted_modem == name:
                            modem_checker = True 
                            modem_vertex = vertex
                            break 
                        else:
                            continue 
                    if modem_checker == True:
                        self.wifibase.graph_dict.pop(deleted_modem)

                        try:
                            print(self.wifibase.graph_dict[deleted_modem])
                        except KeyError:
                            print('The modem has been successfully deleted')
                            self.registered_modems.remove(modem_vertex)
                    else:
                        print('That modem is not on the server')

            elif prompt == "/view_modems":
                if len(self.registered_modems) == 0:
                    time.sleep(0.1)
                    print("The sever is empty")
                    print('-'*24)
                else:
                    for i in list(self.wifibase.graph_dict.keys()):
                        print('-'*24)
                        print(i)
                    print("-"*24)
                    time.sleep(0.1)
                    print('Here are currently all your modems on your server ')

            elif prompt == "/ip_validation":
                ips = []
                for i in self.registered_modems:
                    ips.append(i.value[-1])
                
                user_ip = input("Please enter the first 6 characters of your ip: ")
                user_ip = user_ip.encode()
                user_ip = hashlib.sha224(user_ip).hexdigest()

                valid_ips = []
                for ip in ips:
                    outcome = pattern_search(ip, user_ip)
                    if len(outcome) > 0:
                        valid_ips.append(ip)
                    else:
                        continue
                
                if len(valid_ips) == 0:
                    print("That Ip seems to be either fake or does not seem to be registered under this software ")
                else:
                    for i in ips:
                        print("Your Ip is registered {}".format(i))
                        
                        for k in self.registered_modems:
                            if k.value[-1] == i:
                                print("That ip is from the modem \'{}\'".format(k.value[0]))
                                break 
                            else:
                                continue 
                

            elif prompt == "/check_ip":
                print("\n")
                modem = input('Type in the modem you want to verify the ip for: ')
                modem_found = None 
                try:
                    modem_found = self.wifibase.graph_dict[modem]
                except KeyError:
                    pass 
                    
                if modem_found == None:
                    print("That modem does not seem to be registered in this software. Type \'/add_modem\' to add that specific modem")
                    time.sleep(0.1)
                else:
                    user_ip = print("Please type in the first six characteres of your ip: ")
                    outcomes = pattern_search(modem_found[-1], user_ip)

                    if len(outcomes) == 0:
                        print("The Ip you have inputted seems to be incorrect and does not match with the one that has been registered under this software")
                        time.sleep(0.1)
                        print("If this is an accident, please type in the right ip address again, or delete the registered modem with \'/delete\' and re-enter the modem with the correct ip")
                        time.sleep(0.1)
                    else:
                        print('The Ip matches ')

            elif prompt == "/quit":
                print('You have successfully quit the server. ')
                break 
            
            else:
                print("That command does not seem to be valid")

                
            
                

                            





            

                
                


                
