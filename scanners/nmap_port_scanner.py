from __future__ import print_function
import optparse
import nmap
def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print(" [*] " + tgtHost + " tcp/" +tgtPort + " " + state)
def main():
    parser = optparse.OptionParser(('usage %prog -H <target host> -p <target port(s) separated by space>'))
    parser.add_option("-H", dest="tgtHost", type="string", help="specify tarhet host")
    parser.add_option("-p", dest="tgtPort", type="string", help="specify target port(s) separated by space")
    (options, args) = parser.parse_args()
    tgtHost = str(options.tgtHost).strip()
    tgtPorts = [s.strip() for s in str(options.tgtPort).split(',')]
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    for tgtPort in tgtPorts:
        nmapScan(tgtHost, tgtPort.strip())
if __name__ == "__main__":
    main()