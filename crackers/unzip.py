from __future__ import print_function
import zipfile
import optparse
from threading import Thread
def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=bytes(password, 'utf-8'))
        print('[+] Password = ' + password + "\n")
    except:
        pass
def main():
    parser = optparse.OptionParser("usage%prog " + "-f <zipfile> -d <dictionary>")
    parser.add_option("-f", dest="zname", type="string", help="specify zip file")
    parser.add_option("-d", dest="dname", tpye="string", help="specify dictionary file")
    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()
if __name__ == '__main__':
    main()
