import zipfile
from threading import Thread
def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print '[+] Password = ' + password + "\n"
    except:
        pass
def main():
    zFile = zipfile.ZipFile("secret.zip")
    passFile = open("dictionary.txt")
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()
if __name__ == '___main__':
    main()
