# Zhiyuan Yang, Zhang CSCI4211, 15/02/2020
# Spring 2020 CSci4211: Introduction to Computer Networks
# This program serves as the server of DNS query.
# Written in Python v3.

import sys, threading, os, random, csv
from socket import *

def main():
	host = "localhost" # Hostname. It can be changed to anything you desire.
	port = 9889 # Port number.

	#create a socket object, SOCK_STREAM for TCP
	try:
		sSock = socket(AF_INET, SOCK_STREAM)
	except error as msg:
		sSock = None
	#bind socket to the current address on port 5001
	sSock.bind((host, port))
	#Listen on the given socket maximum number of connections queued is 20
	sSock.listen(5)

	monitor = threading.Thread(target=monitorQuit, args=[])
	monitor.start()

	print("Server is listening...")

	while 1:
		#blocked until a remote machine connects to the local port 5001
		connectionSock, addr = sSock.accept()
		server = threading.Thread(target=dnsQuery, args=[connectionSock, addr[0]])
		server.start()

def dnsQuery(connectionSock, srcAddress):
	#recieve message from clinet
	data = connectionSock.recv(1024).decode()

	#create dns-server-log.csv if not exist
	logPath = './dns-server-log.csv'
	if not os.path.isfile(logPath):
		f = open(logPath, 'w')
		f.close()

	#check the DNS_mapping.txt to see if the host name exists
	#set local file cache to predetermined file.
	cachePath = './DNS-text-mapping.txt'
	if not os.path.isfile(cachePath):
		#create cahe file if it doesn't exist
		f = open(cachePath, 'w')
		f.close()
	
    #if it does exist, read the file line by line to look for a
    #match with the query sent from the client
    #If match, use the entry in cache.
	#reference from Jason's example, read all lines in the cache and use dict for accessing
	cacheLines = None
	with open(cachePath, 'r') as f:
		cacheLines = f.readlines()
	
	cacheDict = dict()
	for line in cacheLines:
		linePair = line.split(',')
		hostName = linePair[0]
		ipAddr = linePair[1]
		cacheDict[hostName] = ipAddr

	#check if the hostname requested by client exists in cache
	#resAddr: corresponding address, source: how it was resolved
	resAddr = None
	source = None
	if data in cacheDict:
		#remove newline character
		resAddr = cacheDict[data].strip('\n')
		source = 'Local DNS'
	else:
		#If no lines match, query the local machine DNS lookup to get the IP resolution
		source = 'API DNS'
		try:
			resAddr = gethostbyname(data)
		except:
			resAddr = 'host not found'

		#write the response in DNS_mapping.txt
		if data and resAddr is not None:
			with open(cachePath, 'a') as txtFile:
				txtFile.write(data + ',' + resAddr + '\n')

	#print response to the terminal
	if source and data and resAddr is not None:
		res = source + ':' + data + ': ' + resAddr
		print(res)

		# write server log to dns-server-log.csv
		with open(logPath, 'a') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow([data, resAddr])

		#send the response back to the client
		connectionSock.send(res.encode())

	#Close the server socket.
	connectionSock.close()

def monitorQuit():
	while 1:
		sentence = input()
		if sentence == "exit":
			os.kill(os.getpid(),9)

main()
