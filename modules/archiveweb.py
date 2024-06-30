import requests
import urllib3
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import unquote
from fake_useragent import UserAgent

urllib3.disable_warnings()

def dorks(target, proxy=None):
    print('[+] Google dorks')
    
    if proxy:
        proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
    else:
        proxies = None

    data = set()
    cont = 0

    while True:
        ua = UserAgent()
        headers = {"Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": f"{ua.random}", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "X-Client-Data": "CNzeygE=", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Priority": "u=0, i", "Referer": "https://www.google.com.br"}
        req = f'https://www.google.com.br/search?q=site:{target}&num=50&start={cont}&cr=countryBR&tbs=ctr:countryBR,lr:lang_1pt&source=lnt&lr=lang_pt'
        
        try:
            r = requests.get(req, headers=headers, proxies=proxies, timeout=8, verify=False, allow_redirects=False)
            r.raise_for_status()
        except requests.exceptions.RequestException as err:
            print(f'[!] Erro: {err}')
            break
        
        if 'o encontrou nenhum document' in r.text:
            break

        bs = BeautifulSoup(r.text, 'html.parser')
        for link in bs.find_all('a'):
            if target in link.text:
                data.add(unquote(link.get('href')))

        time.sleep(5.0)
        cont += 50
    
    return data


def wayback(target, proxy=None):
    print('[+] Wayback machine')

    if proxy:
        proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
    else:
        proxies = None

    data = set()
    
    try:
        r = requests.get(f'http://web.archive.org/cdx/search/cdx?url={target}/*&output=json&collapse=urlkey', proxies=proxies, timeout=8, verify=False, allow_redirects=False)
        for value in r.json():
            data.add(unquote(value[2]))
    
    except Exception as err:
        print(f'[!] Erro: {err}')
    
    return data


def remove_ext(list):
    data = set()
    ext = ('.css', '.png', '.pdf', '.jpg', '.jpeg', '.ico', '.bmp', '.svg', '.gif', '.woff', '.woff2', '.ttf', '.eot', '.otf')
    
    for url in list:
        u = urlparse(url)
        if not any(x in u.path.split('/')[-1] for x in ext) and 'http' in url:
            data.add(url.rstrip())
    
    return data


def clear(list):
    #print('[+] Organizando lista')
    
    data = set()
    temp = set()
    
    urls = sorted(set(list))
    
    for url in urls:
        u = urlparse(url)

        if not u.query:
            data.add(url.rstrip())
        
        if u.query and '&' not in u.query:
            param = u.query.split('=')[0]
            x = f'{u.scheme}{u.netloc}{u.path}{param}'
            if x not in temp:
                temp.add(x)
                data.add(url.rstrip())
        
        if '&' in u.query:
            param = u.query.split('&')
            concat = ''
            for p in param:
                c = f'{p.split("=")[0]}'
                concat += c
            x = f'{u.scheme}{u.netloc}{u.path}{sorted(concat)}'
            if x not in temp:
                temp.add(x)
                data.add(url.rstrip())
    
    return sorted(data)


def archiveweb(target, proxy=None):
    data = clear(remove_ext([*dorks(target, proxy), *wayback(target, proxy)]))
    return data

if __name__ == '__main__':
    try:
        print(*archiveweb(""), sep="\n")
    except KeyboardInterrupt:
        print('[!] Stopping')