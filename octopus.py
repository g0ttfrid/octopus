# -*- condig: utf-8 -*-

import os
import argparse
import codecs
from config import banner as bn
from config.banner import colors
from config.module import *

os.system('cls' if os.name == 'nt' else 'clear')
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

try:
    raw_input # if you using Python 2
except NameError:
    raw_input = input # If you using Python 3

class Octopus2(object):
    """docstring for octopus."""

    def __init__(self):
        self.description = bn.banner()
        parser = argparse.ArgumentParser(prog=self.description, usage='%(prog)s [options]')
        parser.add_argument('-d', '--domain', nargs='?', metavar='{BLUE}\'example.com\'{FIM}'.format(**colors), type=str, help='{YELLOW}\'Specify your domain\'{FIM}'.format(**colors))
        parser.add_argument('-u', '--url', nargs='?', metavar='{BLUE}\'https://www.example.com\'{FIM}'.format(**colors), type=str, help='{YELLOW}\'Specify your URL\'{FIM}'.format(**colors))
        self.args = parser.parse_args()

    def start(self):
        print(self.description)
        
        if self.args.url != None:
            url = str(self.args.url)
            print("\n{YELLOW}[+]{FIM} Target: {YELLOW}{d}{FIM}\n".format(**colors, d=url))
            search_key(parse_site(url))
        elif self.args.domain != None:
            domain = clear_url(self.args.domain)    
            print("\n{YELLOW}[+]{FIM} Target: {YELLOW}{d}{FIM}\n".format(**colors, d=domain))
            sub_list = []
            sub_list = sub_domains(domain)
            search_key(parse_site(sub_list))
        else:
            print("\n{RED}[!] NO Target!!!{FIM}\n".format(**colors))

try:
    Octopus2().start()
except KeyboardInterrupt:
    print('\n{RED}Exit system{FIM}'.format(**colors))
exit()
