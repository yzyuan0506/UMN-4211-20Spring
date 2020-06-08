/*
* name: Zhiyuan Yang
* Zhang CSCI4211
* date: 15/02/2020
*/
---
### Compilation Section ###
Since Python is an interpreted language, users do not need to compile source files to executable.
However, users must have **Python 3** installed.
One can run:
```
python3 --version
```
to check if Python 3 is installed in the computer

---

### Execution/Running Section ###
First, users should launch 'DNSServerV3.py' to listen on connections from clients 
User can run the server by ’python3' command:
```
    python3 DNSServerV3.py
```
The server program will run and display "Server is listening..." in the termianl.
Then users should keep the server running and open a new terminal window.
In the same directory, we can run the client, which is 'DNSClientV3.py' to establish a new connection with server in the new termianl window by:
```
    python3 DNSClientV3.py
```
Client will get started and should display "Type in a domain name to query, or 'q' to quit:"

To terminate the server, users can type "exit" in the termianl and type "q" to terminate a client.

---

### Description Section ###
'DNSServerV3.py' is the code for the server program.
Once the server get running, it will listens on port 9889
and be able to handle multiple requests from clients at the same time.
Completing a service for a client will not terminate the server.
The service that the server provides for clients is translating URL to IP address (DNS).
After recieving the request from clients, the server has two ways to do the translation:
1. Local DNS Cache
2. API Call (gethostbyname)
The server will first look for the hostname that requested by the client in the local DNS cache file "DNS-text-mapping.txt". If the requested hostname is found in the cache, the server just take the corresonding IP address and send back to the client. Otherwise, the server will use built-in API call "gethostbyname" to get the corresonding IP address and store it in cache. If the server cannot find the IP address in both ways. Error message will be sent back to client and the hostname will be mapped with "Host not found" in the cache. After completion of the service, the log of the sever will be saved in "dns-server-log.csv" and the server will continue on listening on other connections.
To terminate the server, users can type "exit" in the terminal.

'DNSClientV3.py' is the code for the client program.
Once client get started, users can continue to request services from the server unless users want to terminal the client.
Users can query the IP address of a URL address after establishing a connection with the server. For example, users can type "www.google.com" to query the IP address of "www.google.com". The server should response with the corresponding IP address (e.g. 192.1.1.1) and it will display in the terminal that the client is running on.
To terminate the client, users can simply type "q" in the terminal.


