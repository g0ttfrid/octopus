#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import argparse
import codecs
from modules.banner import *
from modules.subdomains import subdomains
from modules.archiveweb import archiveweb
from modules.getlinks import getlinks
from modules.search import search,logger

os.system('cls' if os.name == 'nt' else 'clear')
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)



class Octopus(object):

    def __init__(self):
        self.description = banner()
        parser = argparse.ArgumentParser(description='Simple tool to help you catch hardcode API Keys - B4d C0d3', prog=self.description, usage='%(prog)s')
        parser.add_argument('-d', '--domain', nargs='?', metavar='{BLUE}example.com{FIM}'.format(**colors), type=str, help='{CYAN}{BOLD}Specify your domain{FIM}'.format(**colors))
        parser.add_argument('-p', '--proxy', nargs='?', metavar='{BLUE}username:password@myproxy.om:1337{FIM}'.format(**colors), type=str, help='{CYAN}{BOLD}Specify your proxy. Recommended to use specific proxies for crawling{FIM}'.format(**colors))
        self.args = parser.parse_args()

    def start(self):
        print(self.description)

        if self.args.domain != None:
            target = self.args.domain
            print("\n{YELLOW}[+]{FIM} Target: {YELLOW}{d}{FIM}\n".format(**colors, d=target))
            subs = set()
            urls = set()
            subs.update(subdomains(target))
            urls.update(archiveweb(target))
            urls.update(getlinks(subs, urls))
            logger(search(urls))

        else:
            print('{RED}{BOLD}[!] Please, pass a domain. Use -h or --help{FIM}'.format(**colors))

try:
    Octopus().start()
except KeyboardInterrupt:
    print('\n{RED}Exit system{FIM}'.format(**colors))
exit()
