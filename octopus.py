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
        parser.add_argument('-d', '--domain', nargs='?', metavar='{BLUE}\'example.com\'{FIM}'.format(**colors), type=str, required=True, help='{YELLOW}\'Specify your domain\'{FIM}'.format(**colors))
        self.args = parser.parse_args()

    def start(self):
        print(self.description)
        target = clear_url(self.args.domain)
        print("\n{YELLOW}[+]{FIM} Target: {YELLOW}{d}{FIM}\n".format(**colors, d=target))

        sub_list = []
        sub_list = sub_domains(target)
        search_key(parse_site(sub_list))

try:
    Octopus2().start()
except KeyboardInterrupt:
    print('\n{RED}Exit system{FIM}'.format(**colors))
exit()
