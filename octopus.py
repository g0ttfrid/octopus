#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import requests
import lxml.html

'''
g0ttfr1d
v0.2
add opção de usar uma url

[+] Requirements
requests
lxml

[+] Inspired by 
https://github.com/UnaPibaGeek/ctfr
https://github.com/PortSwigger/aws-security-checks
'''

def parse_args():
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--domain', type=str, required=True)
	return parser.parse_args()

def clear_url(target):
    return re.sub('.*www\.','',target,1).split('/')[0].strip()

def sub_domains(target):
    print('[+] Subdomains')
    subdomains = []
    
    r = requests.get("https://crt.sh/?q=%.{t}&output=json".format(t=target))
        
    if r.status_code != 200:
        print('[!] Information not available!') 
        exit(1)

    for (key,value) in enumerate(r.json()):
        subdomains.append(value['name_value'])

    subdomains = sorted(set(subdomains))
    for subdomain in subdomains:
        print("  + {s}".format(s=subdomain))

    if subdomains == []:
        print('[!] Subdomains not found!')
        exit(1)
        
    return subdomains

def parse_site(subdomains):
    links = []
    for sub in subdomains:
        if '*' not in sub:
            try:
                r = requests.get('https://{s}'.format(s=sub))
                
                dom = lxml.html.fromstring(r.content)
                for link in dom.xpath('//script/@src'):
                    
                    if link.startswith('https://'):
                        links.append(link)
                    elif link.startswith('www'):
                        links.append('https://{l}'.format(l=link))
                    elif link.startswith('//www'):
                        links.append('https:{l}'.format(l=link))
                    elif link.startswith('/'):
                        links.append('https://{s}{l}'.format(s=sub,l=link))
                    else:
                        links.append('https://{s}/{l}'.format(s=sub,l=link))
            except:
                pass
    return links

def search_key(urls):
    print('\n[+] Parsing sites and searching creds')
    
    words = ['S3_KEY', 'S3_SECRET', 'AWS_ACCESS_KEY_ID',
            'AWS_SECRET_ACCESS_KEY', 'AccessKeyId', 'SecretAccessKey',
            'aws_access_key_id', 'aws_secret_access_key', 'aws_session_token'
        ]

    for url in urls:

        r = requests.get(url)
        r = str(r.content)
        r = r.split("'")

        len_id = 20
        len_secret = 40

        print('  + URL: {u}'.format(u=url))
        for word in words:
            if word in r:
                print('  - Possible {w}'.format(w=word))
                for find in r:
                    if 'id' in word.lower():
                        if len(find) == len_id and find.isupper() and find.isalnum():
                            print('    > Access ID: {f}'.format(f=find))
                    elif 'secret' in word.lower():
                        if len(find) == len_secret and ' ' not in find:
                            print('    > Access Secret: {f}'.format(f=find))

def banner():
    b = r'''
                            ___
                         .-'   `'.
                        /         \
                        |         ;
                        |         |           ___.--,
               _.._     |0) ~ (0) |    _.---'`__.-( (_.
        __.--'`_.. '.__.\    '--. \_.-' ,.--'`     `""`
       ( ,.--'`   ',__ /./;   ;, '.__.'`    __
       _`) )  .---.__.' / |   |\   \__..--""  """--.,_
      `---' .'.''-._.-'`_./  /\ '.  \ _.-~~~````~~~-._`-.__.'
            | |  .' _.-' |  |  \  \  '.               `~---`
             \ \/ .'     \  \   '. '-._)
              \/ /        \  \    `=.__`~-.
              / /\         `) )    / / `"". \
        , _.-'.'\ \        / /    ( (     / /
         `--~`   ) )    .-'.'      '.'.  | (
                (/`    ( (`          ) )  '-;
                 `      '-;         (-'
    
                        OCTOPUS
    --=={ Looking for AWS ID and Secret Access }==-- 
    '''
    print(b)

def main():
    banner()
    
    args = parse_args()
    target = clear_url(args.domain)
    print("\n[+] Target: {d}\n".format(d=target))
    
    sub_list = []
    sub_list = sub_domains(target)
    search_key(parse_site(sub_list))

main()