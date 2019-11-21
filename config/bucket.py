# -*- coding: utf-8 -*-
import re
import requests
from config.banner import colors

def combinations(target):
    names = []
    names1 = ['storage', 'dev', 'cloud', 'staging']
    names2 = re.sub('.*//|\.com.*','',target).split('.')

    for n1 in names1:
        for n2 in names2:
            names.append('{n1}-{n2}'.format(n1=n1,n2=n2))
            names.append('{n2}-{n1}'.format(n1=n1,n2=n2))
            names.append('{n2}'.format(n2=n2))

    return list(set(names))

def buckets3(words):
    print('\n{GREEN}[+]{FIM} Searching Buckets'.format(**colors))
    bkts = []
    for word in combinations(words):
        try:
            r = requests.get('https://{w}.s3.amazonaws.com'.format(w=word), timeout=(5,5))
            if r.status_code != 404:
                print('  + Possible {RED}Bucket S3{FIM} {YELLOW}{w}.s3.amazonaws.com{FIM}'.format(**colors, w=word))
                bkts.append(word)
            else:
                r = requests.get('https://s3.amazonaws.com/{w}/'.format(w=word), timeout=(5,5))
                if r.status_code != 404:
                    print('  + Possible {RED}Bucket S3{FIM} {YELLOW}s3.amazonaws.com/{w}/{FIM}'.format(**colors, w=word))
                    bkts.append(word)
        except:
            pass
    return bkts