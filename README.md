```shell
                                           __                              
                              ____   _____/  |_  ____ ______  __ __  ______
                             /  _ \_/ ___\   __\/  _ \\____ \|  |  \/  ___/
                            (  <_> )  \___|  | (  <_> )  |_> >  |  /\___ \
                             \____/ \___  >__|  \____/|   __/|____//____  >
                                        \/            |__|              \/
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
                              --== Looking for hardcoded API Keys ==--
                                              B4d C0d3

    Author: g0ttfrid
    Contributor : Achilles0x01

    IBLISS Labs

```

# Intro
Simple tool to help you catch hardcode API Keys.
  1. Enum sub-domains (crt.sh and certspotter);
  2. Fetch all the URLs that Google and Wayback Machine knows of the target (Add new subdomains too);
  3. Connects to sub-domains and search for URLs in code (concatenating with the urls from the previous phase);
  4. Fetch some types of API Keys in source code using regex.

- following the worst programming practices.


>Recommended to use specific proxy for crawling.
>subdomains.py accesses crt.sh and certspotter.
>archiveweb.py accesses google.com.br and web.archive.org.
>getlinks.py and search.py access target urls.

>Add more regex in search.py to get other types of keys.

# Arguments

  ```shell
  -h, --help            show this help message and exit
  -d [example.com], --domain [example.com]
                        Specify your domain
  -p [username:password@myproxy.com:1337], --proxy [username:password@myproxy.com:1337]
                        Specify your proxy. Recommended to use specific proxies for    
                        crawling
  ```

# References
[ctfr](https://github.com/UnaPibaGeek/ctfr)\
[aws-security-checks](https://github.com/PortSwigger/aws-security-checks)\
[archiveweb](https://github.com/g0ttfrid/archiveweb)\
[pygmy](https://github.com/g0ttfrid/pygmy)
