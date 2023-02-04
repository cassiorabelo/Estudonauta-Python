import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[031mSite não acessível\033[m')
else:
    print('\033[032mSite acessível\033[m')
