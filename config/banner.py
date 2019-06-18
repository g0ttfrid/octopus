# -*- coding: utf-8 -*-
colors = {
    'ITALIC':'\033[3m',
    'GREEN':'\033[92m',
    'YELLOW':'\033[1;93m',
    'BLUE':'\033[1;94m',
    'RED':'\033[1;91m',
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
                 `      '-;         (-'

                        OCTOPUS
    {GREEN}--== Looking for AWS ID and Secret Access ==--{FIM}
                        {GREEN}B4d C0d3{FIM}
    {GREEN}Author: {FIM}g0ttfr1d
    {GREEN}Contibutor: {FIM}Achilles0x01
    {GREEN}github: {FIM}g0ttfr1d
    {GREEN}github: {FIM}iBLISSLabs
    
    {BLUE}IBLISS Labs{FIM}

'''.format(**colors)

def banner():
    return(show_me)
