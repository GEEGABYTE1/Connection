
from graph import Graph
from vertex import Vertex
import hashlib
import time 



class Prompt:
    wifibase = Graph()
    unregisted_modems = [] 
    def database(self):
        playing = True 
        while playing:
            print('\n')
            prompt = input(':')

            if prompt == '/add_modem':
                name = input('Name of the modem: ')
                ip_address = input('First three numbers of ip: ')
                ip_address = hash_lib.sha224(ip_address).hexdigest()

                validation = False 
                
                for i in list(self.wifibase.graph_dict.keys()):
                    if i[0] == name:
                        validation = True 
                        break
                    elif i[-1] == ip_address:
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
                    self.unregisted_modems.append(vertex_modem)
                    time.sleep(0.1)
                    print('New Modem added. Type \`/register\` to register the modem in to the system')
            
            elif prompt == "/register":
                modem_name = input('Name of the modem: ')
                validation = False 
                modem = None
                for i in self.unregisted_modems:
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
                        print('Modem added')
                        time.sleep(0.1)
                        print('Once there are more modems (>1) defined in the software, you will be able to add links')
                    else:
                        for wifi in list(self.wifibase.graph_dict.keys()):
                            print('-'*24)
                            print(wifi[0])
                        
                        temp_modem_list = list(self.wifibase.graph_dict.keys())
                        temp_modem_names = [i[0] for i in temp_modem_list]
                        print('-'*24)
                        print()
                        
                        print("Here are the modem(s) that are in the server ")
                        time.sleep(0.1)
                        router_name = input('Please enter one of the modem\'s name exactly to add a link. If you wish to have no link, please type \'None\' ')

                        if not router_name in temp_modem_names:                                     # If the link is not even defined 
                            print('That router does not seem to be in the sever ')
                            time.sleep(0.1)
                        elif router_name == "None" or router_name == "None ":                       # If the user wants no link
                            self.wifibase.add_vertex(modem)
                            print('Modem added with no link ')
                            time.sleep(0.1)
                        
                        elif router_name in temp_modem_names:                                       # If link is defined
                            link_router = None 
                            for data, vertex in self.wifibase.graph_dict.items():
                                if data[0] == router_name:
                                    link_router = vertex 
                                    break 
                                else:
                                    continue 
                            
                            latency = random.randint(1, 1000)
                            self.wifibase.add_vertex(modem)
                            self.wifibase.add_edge(modem, link_router, latency)

                            print('{modem1} is linked to {modem2} with {latency} ms '.format(modem1=modem, modem2=link_router, latency=latency))


                            





            

                
                


                
