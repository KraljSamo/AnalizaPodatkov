import os
import requests
from requests.auth import HTTPBasicAuth
import re

def shrani(url, ime_dat):
    cookie = {'DYNSRV': 'lin-10-170-0-29', 'PHPSESSID' : 'd3f5633764bca14aa7266b73b29ffd18', 'keep_alive' : '755538%23DPoW8e4ty1ggRiMnE2Lk920O829AeoxH'}
    r = requests.post(url, cookies = cookie)
    dat = os.path.dirname(ime_dat)
    if dat:
        os.makedirs(dat, exist_ok = True)
    with open(ime_dat, "w") as file:
        file.write(r.text)
        print("Shranjeno: ", url)
        
def zajemi():
    glavni_url = 'https://projecteuler.net'
    
    for stran in range(6,13):
        url = glavni_url + '/archives;page=' + str(stran)
        pot = 'Arhivi/Stran_{}'.format(stran)
        shrani(url, pot)

    for st_naloge in range(277, 567):
        url = glavni_url + '/fastest=' + str(st_naloge)
        pot = r'Fastest_Solvers/Naloga_{}'.format(st_naloge)
        shrani(url,pot)

#zajemi()
