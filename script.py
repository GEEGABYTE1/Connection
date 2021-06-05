
from graph import Graph
from vertex import Vertex
import hashlib
import time 
import random 



class Prompt:
    wifibase = Graph()
    unregistered_modems = [] 
    registered_modems = []

    def database(self):
        
        playing = True 
        while playing:
            print('\n')
            prompt = input(':')

            if prompt == '/add_modem':
                name = input('Name of the modem: ')
                ip_address = input('First three numbers of ip: ')
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

                        if not router_name in temp_modem_names:                                     # If the link is not even defined 
                            print('That router does not seem to be in the sever ')
                            time.sleep(0.1)
                        elif router_name == "None" or router_name == "None ":                       # If the user wants no link
                            self.wifibase.add_vertex(modem)
                            self.registered_modems.append(modem)
                            print('Modem added with no link ')
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
                            self.wifibase.add_vertex(modem)
                            self.registered_modems.append(modem)
                            self.wifibase.add_edge(modem, link_router, miliseconds)

                            print('\'{modem1}\' is linked to \'{modem2}\' with a return speed of {latency} m/s '.format(modem1=modem.value[0], modem2=link_router.value[0], latency=miliseconds))


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

                            




test = Prompt()

test.database()
            

                
                


                
