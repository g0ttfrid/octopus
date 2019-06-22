#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import requests
import lxml.html
import argparse
from config.banner import colors

# g0ttfr1d
# Edit by Achilles0x0
# v1.0

def clear_url(target):
    return re.sub('.*www\.','',target,1).split('/')[0].strip()

def sub_domains(target):
    print('{GREEN}[+]{FIM} Subdomains'.format(**colors))
    subdomains = []

    r = requests.get("https://crt.sh/?q=%.{t}&output=json".format(t=target))

    if r.status_code != 200:
        print('{RED}[!]{FIM} Information not available!'.format(**colors))
        exit(1)

    for (key, value) in enumerate(r.json()):
        subdomains.append(value['name_value'])

    subdomains = sorted(set(subdomains))
    for subdomain in subdomains:
        print("  + {s}".format(s=subdomain))

    if subdomains == []:
        print('{YELLOW}[!]{FIM} Subdomains not found!'.format(**colors))
        exit(1)

    return subdomains

def parse_site(subdomains):
    print('\n{GREEN}[+]{FIM} Parsing sites'.format(**colors))
    links = []
    for sub in subdomains:
        if '*' not in sub:
            try:
                r = requests.get('https://{s}'.format(s=sub), timeout=(3,5))

                dom = lxml.html.fromstring(r.content)
                for link in dom.xpath('//script/@src'):
                    if link.startswith('https://'):
                        links.append(link)
                    elif link.startswith('//'):
                        links.append('https:{l}'.format(l=link))
                    elif link.startswith('/'):
                        links.append('https://{s}{l}'.format(s=sub,l=link))
                    else:
                        links.append('https://{s}/{l}'.format(s=sub,l=link))
            except:
                pass
    return links

def search_key(urls):
    print('\n{GREEN}[+]{FIM} Searching creds'.format(**colors))

    words = ['S3_KEY', 'S3_SECRET', 'AWS_ACCESS_KEY_ID',
            'AWS_SECRET_ACCESS_KEY', 'AccessKeyId', 'SecretAccessKey',
            'aws_access_key_id', 'aws_secret_access_key', 'aws_session_token'
        ]

    for url in urls:

        r = requests.get(url, timeout=(3,5))
        r = str(r.content)
        r = r.split("'")

        len_id = 20
        len_secret = 40

        print('  + URL: {u}'.format(u=url))
        for word in words:
            if word in r:
                print('  - Possible {RED}{w}{FIM}'.format(**colors, w=word))
                for find in r:
                    if 'id' in word.lower():
                        if len(find) == len_id and find.isupper() and find.isalnum():
                            print('    > Access ID: {GREEN}{f}{FIM}'.format(**colors, f=find))
                    elif 'secret' in word.lower():
                        if len(find) == len_secret and ' ' not in find:
                            print('    > Access Secret: {GREEN}{f}{FIM}'.format(**colors, f=find))
