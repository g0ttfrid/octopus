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
                         --== Looking for AWS ID and Secret Access ==--
                                            B4d C0d3

    Author: g0ttfr1d
    Contributor : Achilles0x01
    github: g0ttfr1d
    github: iBLISSLabs

    IBLISS Labs

```

# Intro
Simple tool to help you catch aws credentials, when dev falter.
  1. Enum sub-domains (https://crt.sh/);
  2. Connects to sub-domains and search for script calls in source code;
  3. Search for AWS credentials inside of scripts.

- following the worst programming practices.


# Requirements

```shell
requests
lxml
os
argparse
codecs
re

pip3 install -r requirements.txt
```


# Optional arguments:

  ```shell
  -h, --help            show this help message and exit

  -d ['example.com'],   --domain ['example.com']

                        Specify your domain

  ```


# To Do:

```shell
Integrate the JSON module.
Optimize the code.
Decontaminate the output of information.
Generate output.
Integrate with APIs.
```


# Inspired by
https://github.com/UnaPibaGeek/ctfr

https://github.com/PortSwigger/aws-security-checks
