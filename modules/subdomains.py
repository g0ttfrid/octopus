import requests
import urllib3
from fake_useragent import UserAgent

urllib3.disable_warnings()

def subdomains(domain, proxy=None):
    print('[+] Subdomains')
    domain = domain.strip()
    data = set()

    ua = UserAgent()
    headers = {'User-Agent': f'{ua.random}'}

    if proxy:
        proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
    else:
        proxies = None

    try:
        r = requests.get(f'https://api.certspotter.com/v1/issuances?domain={domain}&include_subdomains=true&expand=dns_names&expand=issuer&expand=cert', headers=headers, proxies=proxies, timeout=8, verify=False, allow_redirects=False)
    except Exception as err:
        print(f'[!] certspotter: {err}')
    
    try:
        for (key,value) in enumerate(r.json()):
            for name in value['dns_names']:
                if '*' not in name and domain in name: data.add(name)
    except Exception as err:
        print(f'[!] certspotter: {err}')

    try:
        r = requests.get(f'https://crt.sh/?q=%.{domain}&output=json', headers=headers, proxies=proxies, timeout=15, verify=False, allow_redirects=False)
    except Exception as err:
        print(f'[!] crt.sh: {err}')

    try:
        for (key,value) in enumerate(r.json()):
            if '\n' in value['name_value']:
                for name in value['name_value'].split(sep='\n'):
                    if '*' not in name and domain in name: data.add(name)
            else:
                if '*' not in value['name_value']: data.add(value['name_value'])
    except Exception as err:
        print(f'[!] crt.sh: {err}')

    return sorted(data)


if __name__ == '__main__':
    try:
        print(*subdomains("", ""), sep="\n")
    except KeyboardInterrupt:
        print('[!] Stopping')
