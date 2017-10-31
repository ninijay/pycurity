# pycurity
A list of python hacking scripts I wrote with the guide of [this book](http://amzn.to/2iaG8t6)

This is a current work in progress.

As soon as I've finished the book, I'll fork this project and create a more usefull pentesting-framework.

# List of Scripts and what they do:
## crackers
### unzip.py
A simple zip-pw dictionary cracker.

Usage:
```
python unzip.py -f <zipfile> -d <dictionary_file>
```

This script will crack a pw- protected zip file with a dictionary list. It will create a pseudo- Thread for each dictionary_file line to speed up the process.

## scanners
### port_scanner.py
A port scanner for hostnames/ips and port(s)

Usage: 
```
python port_scanner.py -H 124.03.31.22 -p 20
python port_scanner.py -H 123.32.32.03 -p "20, 21, 80, 443"
```

### nmap\_port_scanner.py
Same as [port_scanner.py](#port_scannerpy) but with nmap integration.

### simple\_vuln_scanner.py
A simple scanner for common vulnerabilities.

Usage: 
```
python simple_vuln_scanner.py <vuln_list.txt>
```

vuln_list.txt can contain banner info like
- "FreeFloat FTP Server"
- "3Com 3CDaemon FTP Server Version 2"

as suggested by the book. Not limited to FTP- Services.

Scans some ports in a range of IP- Adresses to get vulnerable services.

## ssh

### ssh_dictionary.py
A simple brute-forcer for ssh connections, using a dictionary.

Usage:
```
python ssh_dictionary.py -H <hostname> -u <username> -F <password- file>
```
Tries to brute- force an ssh connection for a given user using a dictionary.

# Disclosure
This Readme may contain affiliate marketing links, which means I may get paid commission on sales of those products or services we write about. My content is not influenced by advertisers or affiliate partnerships. This disclosure is provided in accordance with the Federal Trade Commission’s 16 CFR § 255.5: Guides Concerning the Use of Endorsements and Testimonials in Advertising.
