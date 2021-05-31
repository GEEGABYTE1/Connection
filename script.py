import time
from Regions import DoubleLinkedList
from graph import Graph


class Modem:
    user_count = 0 
    modem_name = None 
    modem_ip = None

class Prompt:
    
    def propmting(self):
        print("Welcome to your connection where you can see all your networks worldwide right from your two eyes! ")
        time.sleep(0.2)
        print('/add: To add a wifi conncetion to a server')
        print('/view: To view all your modems in a sever')
        print('/most_users: To view the server with the most users')
        print('/view_regions: To view all your regions where you have established networks')
        print('/delete: To delete a server entirely')
        print('/view_occupancies: To view the amount of users that are curretly trying to join one of your networks ')
    