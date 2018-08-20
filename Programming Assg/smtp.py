from socket import *
from ssl import *
from sys import * #to take the username and password from command line
import base64  #we need to use this to encode the username and password and send it for authentication


if (len(argv) < 2):
    print "Usage : smtp.py UserName"
    exit(0)

program,UName = argv

msg = "\r\n I love computer networks"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver mailserver = #Fill in start #Fill in end

#Note : Since we have been using GMAIL's SMTP server, inorder to check our code for the same we need to go
#       Google's security settings and allow less secure apps for this code to work and send mail .
mailServerHost = "smtp.nyu.edu"
mailserverPort = 25 #for SSL based SMTP communication

# Create socket called clientSocket and establish a TCP connection with mailserver
sslClientSock = socket(AF_INET, SOCK_STREAM)
sslClientSock.settimeout(10)

sslClientSock.connect((mailServerHost, mailserverPort))

recv = sslClientSock.recv(1024)

print recv

if recv[:3] != '220':
    print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO ALICE\r\n'

sslClientSock.send(heloCommand)

recv1 = sslClientSock.recv(1024)

print recv1

if recv1[:3] != '250':
    print '250 reply not received from server.'

#Send Mail From command
MailFrom = "MAIL FROM:<"+UName+">\r\n"

sslClientSock.send(MailFrom)

recv1 = sslClientSock.recv(1024)
if recv1[:3] != '250':
    print '[MAIL FROM:] 250 reply was not received from the server'
else:
    print recv1

#Note : for test purposes we will be using the same mail from and rcpt to id
RcptTo = "RCPT TO:<"+UName+">\r\n"
sslClientSock.send(RcptTo)

recv1 = sslClientSock.recv(1024)

if recv1[:3] != '250':
    print '[RCPT TO:] 250 reply was not received from the server'
else:
    print recv1

sslClientSock.send("DATA\r\n")
recv1 = sslClientSock.recv(1024)

if recv1[:3] != '354':
    print '[DATA] 354 reply was not received from the server'

#create a header to be send along with the payload
header = "To:"+UName+"\r\nFrom:"+UName+"\r\nSubject:Test Mail For Computer Networking Assignment 5\r\n"

#send the header, msg body and the end msg
sslClientSock.send(header)
sslClientSock.send(msg)
sslClientSock.send(endmsg)

recv1 = sslClientSock.recv(1024)

if recv1[:3] != '250':
    print '[DATA STREAM END] 250 reply was not received from the server'
else:
    print recv1

sslClientSock.send("QUIT\r\n")

print sslClientSock.recv(1024)

sslClientSock.close()
