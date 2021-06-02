import time
from Regions import DoubleLinkedList
from graph import Graph
import hashlib
from Hashmap import HashMap
import random


class Modem:
    user_count = 0 
    modem_name = None 
    modem_ip = None

class Prompt:
    database = DoubleLinkedList()

    def prompting(self):
        print('\n')
        print("Welcome to your connection where you can see all your networks worldwide right from your two eyes! ")
        time.sleep(0.2)
        print('/add: To add a modem (wifi connection) to a server')
        print('/view: To view all your modems in a sever')
        print('/most_users: To view the server with the most users')
        print('/view_regions: To view all your regions where you have established networks')
        print('/add_region: Add a region')
        print('/delete: To delete a server entirely')
        print('/view_occupancies: To view the amount of users that are curretly trying to join one of your networks ')
        print("\n")


        playing = True 
        while playing:
            prompt = input(':')

            if prompt == "/add":
                new_modem = Modem()
                new_modem.user_count = random.randint(1, 2360)
                name = input('Please enter the first four digits of your Ip: ')
                name = name.encode()
                ip = hashlib.sha224(name).hexdigest()
                new_modem.modem_ip = ip 
                modem_name_raw = input('Please enter the name of your modem: ')
                new_modem.modem_name = modem_name_raw 
                s_region = input("Please enter the name of your region: ")

                # Add Modem to Graph 
                if self.region_checker(s_region) == False:
                    print('We may have to create a new region...')
                    time.sleep(0.2)
                    new_region_current = HashMap(11)
                    self.database.add_to_tail([s_region, new_region_current])
                    time.sleep(0.2)
                    print('Region added... ')
                    time.sleep(0.1)
                    print("We can now add a modem to that region's server ")
                else:
                    time.sleep(0.2)
                    print('Region found...')
                
                
                s_server = input('Please enter the name of your server: ')
                if self.server_locator(s_region, s_server) == False:
                    print('Looks like this is a brand new server...')
                    time.sleep(0.1)
                    print("We are commencing ")

                




               

                # Add Server to Link
                current_node = self.database.get_head_node()
                checker_add = False
                while current_node:
                    if current_node.get_value()[0] == s_region:
                        current_node.get_value()[1].setter()

            
            elif prompt == "/add_region":
                name_region_name = input("Please enter the name of your region: ")
                checker = False
                current_node = self.database.get_head_node()
                while current_node:
                    if current_node.get_value()[0] == name_region:
                        print("That region is already added in the database! ")
                        checker = True
                    current_node = current_node.get_link()

                if checker == False: 
                    new_region = HashMap(11)
                    self.database.add_to_tail([name_region_name, new_region])
                    time.sleep(0.2)
                    print("Region added")

    
    def region_checker(self, name):
        checker = False 
        current_node = self.database.get_head_node()
        while current_node:
            if current_node.get_value()[0] == name:
                checker = True 
                return checker 
            current_node = current_node.get_link()

        return checker 


    def server_locator(self, name_region, name_server):
        checker = False 
        current_node = self.database.get_head_node()
        self.founded_server = None
        while current_node:
            if current_node.get_value()[0] == name_region:
                servers = current_node.get_value()[1]
                possible_outcomes = servers.retrieve(name_server)
                if len(possible_outcomes) == 0:
                    checker = False
                    return checker 
                else:
                    checker = True
                    self.founded_server = current_node.get_value()[1]
                    return checker 
                
            current_node = current_node.get_link()





test = Prompt()

print(test.prompting())