# pycurity
A list of python hacking scripts I wrote with the guide of [this book](http://amzn.to/2iaG8t6)

This is a current work in progress.

I also have some PenTesting/ Hacking and Coding videos on my [YouTube Channel](https://www.youtube.com/channel/UCGISJ8ZHkmIv1CaoHovK-Xw) if you're into that.

As soon as I've finished the book, I'll fork this project and create a more usefull pentesting-framework.

# List of Scripts and what they do:
## crackers
### unzip.py
A simple zip-pw dictionary cracker.

Usage:
``` bash
python unzip.py -f <zipfile> -d <dictionary_file>
```

This script will crack a pw- protected zip file with a dictionary list. It will create a pseudo- Thread for each dictionary_file line to speed up the process.

## metasploit
### conficker.py
Clone of conficker exploit

Usage:
``` bash
python -H <RHOST[s]> -l <LHOST> [-p <LPORT> -F <Password File>]
```
Simplifies the process of creating a conficker exploit by handling all the configuration and launching the exploit via msf.

## scanners
### port_scanner.py
A port scanner for hostnames/ips and port(s)

Usage: 
``` bash
python port_scanner.py -H <ip-adress> -p <single port>
python port_scanner.py -H <ip-adress> -p "<mutliple ports separated by comma>"
# eg for multiple port scan
python port_scanner.py -H 127.0.0.1 -p "20, 21, 443"
```

### nmap\_port_scanner.py
Same as [port_scanner.py](#port_scannerpy) but with nmap integration.

### simple\_vuln_scanner.py
A simple scanner for common vulnerabilities.

Usage: 
``` bash
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
``` bash
python ssh_dictionary.py -H <hostname> -u <username> -F <password- file>
```
Tries to brute- force an ssh connection for a given user using a dictionary.

# Disclosure
This Readme may contain affiliate marketing links, which means I may get paid commission on sales of those products or services we write about. My content is not influenced by advertisers or affiliate partnerships. This disclosure is provided in accordance with the Federal Trade Commission’s 16 CFR § 255.5: Guides Concerning the Use of Endorsements and Testimonials in Advertising.
