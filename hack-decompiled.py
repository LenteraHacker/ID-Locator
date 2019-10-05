# uncompyle6 version 3.4.0
# Python bytecode 3.7
# Decompiled from: Python 3.7.4 (default, Jul 11 2019, 08:17:56) 
# [Clang 8.0.7 (https://android.googlesource.com/toolchain/clang b55f2d4ebfd35bf6
import argparse, requests, json, sys
from sys import argv
import os
parser = argparse.ArgumentParser()
parser.add_argument('-t', help='target ip address', type=str, dest='target', required=True)
args = parser.parse_args()
lightblue = '\x1b[94m'
lightgreen = '\x1b[92m'
clear = '\x1b[0m'
boldblue = '\x1b[01m\x1b[94m'
cyan = '\x1b[36m'
bold = '\x1b[01m'
red = '\x1b[31m'
lightcyan = '\x1b[96m'
yellow = '\x1b[93m'
os.system('clear')
print(bold + cyan + '\n________  __      __ \n\\______ \\/  \\    /   |    |  \\   \\/\\/   /\n |    `   \\        / \n/_______  /\\__/\\  /  \n        \\/      \\/   \n' + clear)
print(lightcyan + bold + '[ Written By DW ] | [Youtube.com/dw]\n' + clear)
ip = args.target
api = 'http://ip-api.com/json/'
try:
    data = requests.get(api + ip).json()
    sys.stdout.flush()
    a = yellow + bold + '[~]'
    print(a, 'Target:', data['query'])
    print(a, 'ISP:', data['isp'])
    print(a, 'Organisation:', data['org'])
    print(a, 'City:', data['city'])
    print(a, 'Region:', data['region'])
    print(a, 'Region name:', data['regionName'])
    print(a, 'Latitude:', data['lat'])
    print(a, 'Longitude:', data['lon'])
    print(a, 'Timezone:', data['timezone'])
    print(a, 'Zip code:', data['zip'])
    print(' ' + clear)
except KeyboardInterrupt:
    print('Exiting,Da da bosss.....' + clear)
    sys.exit(0)
except requests.exceptions.ConnectionError as e:
    try:
        print(red + bold + '[!]' + ' Cek jaringan mu mpok!' + clear)
        sys.exit(1)
    finally:
        e = None
        del e