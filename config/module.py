# -*- coding: utf-8 -*-
import re
import requests
import lxml.html
from config.banner import colors

def sub_domains(target):
    print('{GREEN}[+]{FIM} Subdomains'.format(**colors))
    subdomains = []

    r = requests.get("https://crt.sh/?q=%.{t}&output=json".format(t=target))

    if r.status_code != 200:
        print('{RED}[!]{FIM} Information not available, check the domain informed!'.format(**colors))
        exit(1)

    for key,value in enumerate(r.json()):
        subdomains.append(value['name_value'])

    subdomains = sorted(set(subdomains))
    for subdomain in subdomains:
        print("  + {s}".format(s=subdomain))

    if subdomains == []:
        print('{YELLOW}[!]{FIM} Subdomains not found, check the domain informed!'.format(**colors))
        exit(1)

    return subdomains

def parse_site(subdomains):
    print('\n{GREEN}[+]{FIM} Scraping...'.format(**colors))
    links = []
    if type(subdomains) is list:
        for sub in subdomains:
            if '*' not in sub:
                try:
                    r = requests.get('https://{s}'.format(s=sub), timeout=(5,5))
                    dom = lxml.html.fromstring(r.content)
                    links.append('https://{s}'.format(s=sub))
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
    else:
        try:
            r = requests.get('{s}'.format(s=subdomains), timeout=(5,5))
            dom = lxml.html.fromstring(r.content)
            links.append('{s}'.format(s=subdomains))
            for link in dom.xpath('//script/@src'):
                if link.startswith('https://'):
                    links.append(link)
                elif link.startswith('//'):
                    links.append('https:{l}'.format(l=link))
                elif link.startswith('/'):
                    links.append('{s}{l}'.format(s=subdomains,l=link))
                else:
                    links.append('{s}/{l}'.format(s=subdomains,l=link))
        except:
            pass
    return links

def search_key(urls):
    print('\n{GREEN}[+]{FIM} Searching Credentials'.format(**colors))

    words = {'S3_KEY':'', 'S3_SECRET':'', 'AWS_ACCESS_KEY_ID':'',
            'AWS_SECRET_ACCESS_KEY':'', 'AccessKeyId':'', 'SecretAccessKey':'',
            'aws_access_key_id':'', 'aws_secret_access_key':'', 'aws_session_token':''
            }

    url_list = []

    for url in urls:

        r = requests.get(url, timeout=(5,5))
        r = str(r.content)
        r = r.split("'")

        len_id = 20
        len_secret = 40

        for word in words.keys():
            if word in r:
                print('  + Possible {RED}{w}{FIM} in {YELLOW}{u}{FIM}'.format(**colors, w=word, u=url))
                url_list.append(url)
                for find in r:
                    if 'id' in word.lower():
                        if len(find) == len_id and find.isupper() and find.isalnum():
                            print('{BOLD}{ORANGE}   - {w}{FIM} > {REVR}{f}{FIM}'.format(**colors, w=word, f=find))
                            words[word] = find
                    elif 'secret' in word.lower():
                        if len(find) == len_secret and ' ' not in find:
                            print('{BOLD}{ORANGE}   - {w}{FIM} > {REVR}{f}{FIM}'.format(**colors, w=word, f=find))
                            words[word] = find
    return words, list(set(url_list))
