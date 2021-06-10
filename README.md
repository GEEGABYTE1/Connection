# Connection 📳

Connection is a software that allows users to track different modems (or routers) on the same network or server. Users can track, and analyze the performance of each router/modem with latency returns, network returns, ip address validations, and more! 

Connection brings a new, innovative, and easy approach to analyze network servers. If a network is a slow for example, users can analyze network return times based on links of every two modems connected (portrayed by the software) and make appropiate decisions based on the analysis. 

# How it works 🔨

Users will first be prompted to type a certain command after the `:` (colon). Commands vary from: 

 ## Database commands
 *These commands will be printed in the terminal once you run the file*
 -`/add_server`: Allows the user to add a new server to track their modems/routers.
 - `/remove_server`: Removes a server/network from the software.
 - `/view_servers`: Lists all the servers registered under the software.
 - `/access_server`: Allows the user to access and modify the modems/routers in the server specified.
 - `/quit`: Quits the program 
 
 *Note* In order to fully quit the program, users must type `/quit` twice, to break both while loops. 


 ## Sever commands: 
 - `/add_modem`: Allows the user to add a modem to the server.
 - `/register`: Registers a certain modem (chosen by the user) onto the network itself, where further analysis of both the modem and the network in general can be done.
 - `/check_link`: Verifies if there is a link between two routers/modems on the network.
 - `/delete`: Delete's a certain modem/router from the network.
 - `/view_modems`: Allows the user to view all the modems on the network.
 - `/ip_validation`: Allows the user to check if their Ip prompted is fake or is registered under a modem on the server.
 - `/check_total_latency`: Returns the total latency of the network. 
 - `/check_ip`: Checks if a prompted ip is the same ip of the prompted modem/router on the network. 
 - `/quit`: Quits the Software.

*Note*: If there the software returns that `The modem is not registered` or `The modem is not on the software`, the user must register the modem on the software with `/register`. If again the command (`/register`) returns `The modem does not seem to be added into the software`, the user must add the modem again by using the command `/add_modem`.


# More Information 📚
### Database Information
If none of the commands listed above are typed on the software, it will return a statement `That command seems to be invalid` and the user will be prompted again until the user types in a valid command. 

Users have the option to type *extra information* about their software when they add the server to the database. This extra information will be printed when the server is accessed to be analyzed or modified with the command `/acess_server`. This allows for people to keep track of information about the server, and will not forget when needed (when modifying and analyzing). In other words, this printing system allows the users to know the information about their server when needed, without memorizing as the software stores it along with the other information about the server.  

### Server Information 
 If none of the commands listed above are typed on the software, the software will return a statement `That command does not seem to be valid` and the user will be prompted again until the the user types in a valid command. 

 Ip addresses must be typed as 5 characters only (for ex, `123.45`) when prompted. Example will printed as well when prompted to type an ip address.

 The ip addresses that are inputted into the software turn into *hash codes* for security and safety. Hence, everytime an ip addresses are inputted, they become hashcodes and the software compares hashcodes instead of ip addresses. 

 The software has two underlying arrays (`registered_modems` and `unregistered_modems`) that keep track of the modems that are registered and unregistered on the network. This allows for better efficiency of the program for functions like `/delete`, `/view_modems`, and etc. 

 For the functions that involve the ip address (`/check_ip`, and `ip_validation`), the *Naive Search Algorithm* is implemented to keep track of each letter of between the prompted ip from the user and the actual ip of the modem. If the prompted ip matches the actual ip of the modem, the algorithm will return a list of indices where the match was found. 

 Please run `database.py` if you want to run the software as a whole and experience the full software.

# Technical Information 🔌

The database is made using a *bi-directional linked list*. The average complexity (time) of each command in the database is `O(n)`. The space complexity of the database is `O(N)`. However, for the helper functions in the linked list (`remove_head(), remove_tail(), get_head_node()`), they have a complexity of O(1). Overall, The space, and the time complexity of the linked list is `O(N)`.

The *Naive Search Algorithm* has a time complexity of `O(N + k)` and space complexity of `O(N)`. 

The `hashlib` library was used to hash the ip addresses prompted.

Time Comlexity of each command varies. However, general case of all commands are `O(N)`.

The *Graph* data structure was used for the underlying network itself. The graph converts each modem into a vertex, and then connects each modem prompted with a *time in miliseconds* as the edge between the two vertices. This allows the whole network to be seen as a *spider-web* or a *mind-map*.

Made in Python 🐍
