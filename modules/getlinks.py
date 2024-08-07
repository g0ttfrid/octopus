import requests
import lxml.html
import urllib3
import argparse
from fake_useragent import UserAgent
from urllib.parse import urlparse

urllib3.disable_warnings()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--subdomains', type=open, required=True)
    parser.add_argument('-u', '--urls', type=open, required=True)
    return parser.parse_args()

def newsubs(list):
    data = set()

    for url in list:
        u = urlparse(url)
        d = u.netloc
        data.add(d)

    return data


def crawling(subdomains, proxy=None):
    print('[+] Crawling')

    if proxy:
        proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
    else:
        proxies = None
    
    links = set()
    for sub in subdomains:
        ua = UserAgent()
        headers = {'User-Agent': f'{ua.random}'}
        
        try:
            r = requests.get('https://{s}'.format(s=sub), headers=headers, proxies=proxies, timeout=8, verify=False, allow_redirects=False)
            dom = lxml.html.fromstring(r.content)
            links.add('https://{s}'.format(s=sub))
            for link in dom.xpath('//script/@src'):
                if link.startswith('https://'):
                    links.add(link)
                elif link.startswith('//'):
                    links.add('https:{l}'.format(l=link))
                elif link.startswith('/'):
                    links.add('https://{s}{l}'.format(s=sub,l=link))
                else:
                    links.add('https://{s}/{l}'.format(s=sub,l=link))
        except:
            pass
    
    if links:
        return links
    else:
        print('[+] Crawling failed')
        return None


def getlinks(subdomains, urls, proxy=None):
    data = set()
    subdomains.update(newsubs(urls))
    data = crawling(subdomains, proxy)
    data.update(urls)
    return data

if __name__ == '__main__':
    try:
        args = parse_args()
        getlinks(args.subdomains, args.urls)
    except KeyboardInterrupt:
        print('[!] Stopping')
