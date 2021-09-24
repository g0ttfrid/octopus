#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import argparse
import codecs
from config import banner as banana
from config.banner import colors
from config.module import *
from config.bucket import *


os.system('cls' if os.name == 'nt' else 'clear')
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class Octopus(object):

    def __init__(self):
        self.description = banana.banner()
        parser = argparse.ArgumentParser(description='Simple tool to help you catch aws credentials, when dev falter - B4d C0d3', prog=self.description, usage='%(prog)s [ I want to play a game ] ')
        parser.add_argument('-d', '--domain', nargs='?', metavar='{BLUE}example.com{FIM}'.format(**colors), type=str, help='{CYAN}{BOLD}Specify your domain{FIM}'.format(**colors))
        parser.add_argument('-u', '--url', nargs='?', metavar='{BLUE}https://www.example.com{FIM}'.format(**colors), type=str, help='{CYAN}{BOLD}Specify a URL{FIM}'.format(**colors))
        self.args = parser.parse_args()

    def start(self):
        print(self.description)

        if self.args.url != None:
            url = self.args.url
            print('\n{YELLOW}[+]{FIM} Target: {YELLOW}{d}{FIM}\n'.format(**colors, d=url))
            keys, urls = search_key(parse_site(url))
            bkt = buckets3(url)

        elif self.args.domain != None:
            target = self.args.domain
            print("\n{YELLOW}[+]{FIM} Target: {YELLOW}{d}{FIM}\n".format(**colors, d=target))
            sub_list = []
            sub_list = sub_domains(target)
            keys, urls = search_key(parse_site(sub_list))
            bkt = buckets3(target)

        else:
            print('{RED}{BOLD}[!]Please, choice a target or input a dork to search one{FIM}\n\nUse -h or --help'.format(**colors))

try:
    Octopus().start()
except KeyboardInterrupt:
    print('\n{RED}Exit system{FIM}'.format(**colors))
exit()
