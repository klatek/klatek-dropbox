
import os, sys
#import paramiko

print ('Python utilites by Karol Latek')
print ('Version 0.1')
print ('Last modification 20171118')
print ('')
print ('')
print ('Please authorize with username and password:')
print ('')

'''
def createSSHClient(server,port,user,password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client
#ssh = createSSHClient(server,port,user,password)
#scp = SCPClient(ssh.get_transport())
'''

#znalezione w necie.
'''
from paramiko import SSHClient
from scp import SCPClient

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('example.com')

with SCPClient(ssh.get_transport()) as scp:
   scp.put('test.txt', 'test2.txt')
   scp.get('test2.txt')
'''


def checklogin():
    attemptCount = 0
    users = open("users.txt").read().split("\n")
    for i in range(len(users)):
        users[i] = users[i].split("|")
        #print (users) --- display all collected data from the file

    while attemptCount < 3:
        username = str(input("Username: "))
        password = str(input("Password: "))

        for user in users:
            uname = user[4]
            pword = user[5]

            if uname == username and pword == password:
                print ("\n")
                print ("Login succesful !!")
                print ("\n")
                print ("Welcome back " + user[0]+ " " + user[1] + "!!!")
                print ("\n")
                return #return command get out from definition
        else:
            print ('')
            print ('Please try to use correct password')
            attemptCount = attemptCount + 1
    while attemptCount == 3:
            print ('Bye Bye')
            raise SystemExit       
checklogin()
    
'''

    while True:
        username = str(input("Username: "))
        password = str(input("Password: "))

        for user in users:
            uname = user[4]
            pword = user[5]

            if uname == username and pword == password:
                print ('Hello ' + user[1] + ".")
                pass
        print ("Wrong username/password.")
        print ("Try again ! \n\n")

checklogin()             
'''                                                            
'''
username = 'klatek'
password = 'qwe123'
tempdecissison = ''
username1 = 'user'
password1 = 'password'

attemptCount = 0

while attemptCount < 3:
    tempUser = input('Login: ')
    tempPass = input('Password: ')
    # print "You entered: ", tempPass
    if tempPass == password and tempUser == username :
        print ("")
        print ('Login completed')
        print ('Hello ' + username)
        print ('')
        print ('')
        print ('Welcome back !\n')
        break
    else:
        print ('')
        print ('Please try to use correct password')
        attemptCount = attemptCount + 1
while attemptCount == 3:
        print ('Bye Bye')
        raise SystemExit
'''                    

print ("Current working dir : %s" % os.getcwd())
print ("\n")


Cisco = "D:\10.KODI_FILES\Cisco.one"
IMS = "D:\10.KODI_FILES\IMS.one"
Juniper = "D:\10.KODI_FILES\Juniper.one"
LTEstaff = "D:\10.KODI_FILES\LTEstaff.one"
PacketCore = "D:\10.KODI_FILES\Packet Core.one"
Praca = "D:\10.KODI_FILES\Praca.one"
Python = "D:\10.KODI_FILES\Python.one"
Aws = "D:\10.KODI_FILES\AWS\AWS - solution architect.one"

DNS = "D:\10.KODI_FILES\DNS.txt"
GGSN = "D:\10.KODI_FILES\GGSN.txt"
Linux = "D:\10.KODI_FILES\Linux.txt"
MMEsamsung = "D:\10.KODI_FILES\MME_samsung.txt"
# Numerki = "D:\10.KODI_FILES\Numerki.txt" -error as this file does not exists anymore
SAEGWsamsung = "D:\10.KODI_FILES\SAEGW_samsung.txt"
SGSN = "D:\10.KODI_FILES\SGSN.txt"
threeconnections = "D:\10.KODI_FILES\three_connections.txt"

onenotefiles = [Cisco, IMS, Juniper, LTEstaff, PacketCore, Praca, Python, Aws]
txtfiles = [DNS,GGSN,Linux,MMEsamsung,SAEGWsamsung,SGSN,threeconnections]

print("List of files for upload to private server: ", *txtfiles, sep='\n')
print ("\n")
print("List of files for upload to private server: ", *onenotefiles, sep='\n')


def main_menu():
    print ("W domu")

# menu working fine
    menu = '\nChoose which synchornization method you would like to use \n1) UPLOAD TXT files only \n2) UPLOAD ONENOTE + TXT files 7ziped \n3) UPLOAD PYTHON CONFIGURATION files \n4) UPLOAD MIESZKANIE + KASA XLS \n8) UPLOAD PICTURES \n9) ADD NEW SYCHRONIZATION \n0) EXIT'
    print (menu)

    menuchoice = input()
    choice = int(menuchoice)

    print ('You choosed:', menuchoice)

    while choice == 1:
        os.chdir('D:/10.KODI_FILES')
        print("Current working dir : %s" % os.getcwd())
        print ('11111111')
        main_menu()
    while choice == 2:
        os.chdir('D:/10.KODI_FILES')
        print ("Current working dir : %s" % os.getcwd())
        print ('222222222')
        main_menu()
    while choice == 3:
        os.chdir('D:/10.KODI_FILES')
        print ("Current working dir : %s" % os.getcwd())
        print ('3333333333')
        main_menu()
    while choice == 4:
        os.chdir('D:/10.KODI_FILES')
        print ("Current working dir : %s" % os.getcwd())
        print ('44444444')
        main_menu()
    while choice == 8:
        os.chdir('D:/10.KODI_FILES')
        print ("Current working dir : %s" % os.getcwd())
        print ('888888')
        main_menu()
    while choice == 9:
        print ("Current working dir : %s" % os.getcwd())
        print ('9999999')
        main_menu()
    while choice == 0:
        print ("Current working dir : %s" % os.getcwd())
        print ('000000000')
        raise SystemExit
        break


main_menu()
