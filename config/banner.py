#!/usr/bin/python3
# -*- coding: utf-8 -*-
colors = {
    'ITALIC':'\033[3m',
    'BOLD':'\033[01m',
    'REVR':'\033[07m',
    'GREEN':'\033[92m',
    'LGRAY':'\033[90m',
    'ORANGE':'\033[33m',
    'YELLOW':'\033[1;93m',
    'BLUE':'\033[1;94m',
    'CYAN':'\033[96m',
    'RED':'\033[1;31m',
    'FIM':'\033[0m',
}

show_me = r'''
{RED}                            ___
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
                 `      '-;         (-'{GREEN}{ITALIC}V1.2{FIM}{FIM}

{ORANGE}{BOLD}                       __
          ____   _____/  |_  ____ ______  __ __  ______
         /  _ \_/ ___\   __\/  _ \\____ \|  |  \/  ___/
        (  <_> )  \___|  | (  <_> )  |_> >  |  /\___ \
         \____/ \___  >__|  \____/|   __/|____//____  >
                    \/            |__|              \/{FIM}
    {GREEN}--== Looking for AWS ID and Secret Access ==--{FIM}
                       {RED}B4d C0d3{FIM}
    {RED}{ITALIC}[Author]+[GITHUB]: {FIM}g0ttfr1d - {RED}{ITALIC}[Contributor]: {FIM}Achilles0x01
    {BLUE}{ITALIC}[GITHUB]: {FIM}iBLISSLabs

'''.format(**colors)

def banner():
    return(show_me)
