# pycurity
A list of python hacking scripts I wrote with the guide of [this book](http://amzn.to/2iaG8t6)
This is a current work in progress.

# List of Scripts and what they do:
## scanners
### simple\_vuln_scanner.py
A simple scanner for common vulnerabilities.

Usage: 
`
python simple\_vuln_scanner.py <vuln_list.txt>
`

vuln_list.txt can contain banner info like
- "FreeFloat FTP Server"
- "3Com 3CDaemon FTP Server Version 2"

as suggested by the book. Not limited to FTP- Services.

Scans some ports in a range of IP- Adresses to get vulnerable services.


# Disclosure
This Readme may contain affiliate marketing links, which means I may get paid commission on sales of those products or services we write about. My content is not influenced by advertisers or affiliate partnerships. This disclosure is provided in accordance with the Federal Trade Commission’s 16 CFR § 255.5: Guides Concerning the Use of Endorsements and Testimonials in Advertising.
