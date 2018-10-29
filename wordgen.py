import argparse
from sys import argv, exit
from random import randint, choice
from itertools import product
from time import time
from encod import detect
import re
is_printed = False


def flt(x):
    au = 'auioe'
    regex = re.compile('[-=@_!#$%^&*()<>?/\|}{~:]')
    if not regex.findall(x):
        for i in range(len(x)):
            try:
                if x[i] in au:
                    if x[i+1] in au:
                        if x[i] == x[i+1]:
                            continue
                        else:
                            if not i == 0:
                                if not x[i] == x[i-1]:
                                    return False
                            else:
                                return False
                    else:
                        continue
                else:
                    if x[i+1] in au:
                        continue
                    else:
                        if x[i] == x[i+1]:
                            continue
                        else:
                            if not i == 0:
                                if not x[i] == x[i-1]:
                                    return False
                            else:
                                return False

            except IndexError:
                return True
        return True
    else:
        for l in re.findall(r"[\w']+", x):
            if flt(l):
                continue
            else:
                return False
    return True


banner1 = r"""
                       _                  
                      | |                 
__      _____  _ __ __| | __ _  ___ _ __  
\ \ /\ / / _ \| '__/ _` |/ _` |/ _ \ '_ \ 
 \ V  V / (_) | | | (_| | (_| |  __/ | | |
  \_/\_/ \___/|_|  \__,_|\__, |\___|_| |_|
                          __/ |           
                         |___/            
"""
banner2 = r"""
                        |                  
\ \  \   / _ \   __| _` |  _` |  _ \ __ \  
 \ \  \ / (   | |   (   | (   |  __/ |   | 
  \_/\_/ \___/ _|  \__,_|\__, |\___|_|  _| 
                         |___/             
"""
banner3 = r"""
                         __               
 _      ______  _________/ /___ ____  ____ 
| | /| / / __ \/ ___/ __  / __ `/ _ \/ __ \
| |/ |/ / /_/ / /  / /_/ / /_/ /  __/ / / /
|__/|__/\____/_/   \__,_/\__, /\___/_/ /_/ 
                        /____/             
"""
banner4 = r"""
                       _                  
__      _____  _ __ __| | __ _  ___ _ __  
\ \ /\ / / _ \| '__/ _` |/ _` |/ _ \ '_ \ 
 \ V  V / (_) | | | (_| | (_| |  __/ | | |
  \_/\_/ \___/|_|  \__,_|\__, |\___|_| |_|
                         |___/           
"""
print(choice([banner1, banner2, banner3, banner4]))
parser = argparse.ArgumentParser(
    description='Wordgen v 1.0.0 - Created By Mohammadamin Alidoost',
    usage='Wordgen.py -h [input] [options]'
)

parser.add_argument('-i', '--input', type=str, help='input file to Wordgen', nargs='+')
parser.add_argument('-m', '--make-wordlist', type=str, help='make wordlist with wordgen', nargs='+')
parser.add_argument('-o', '--output', type=str, help='get output from wordgen', nargs=1)
parser.add_argument('-r', '--randomize', action='store_true', help='randomize output')
parser.add_argument('-rm', '--remove-from', type=str, help='remove a wordlist from another one', nargs=2)
parser.add_argument('-f', '--filter-words', help='filter words that is easier to pronouns', action='store_true')
parser.add_argument('-c', '--combine-words', help='combine words together', nargs='+', type=str)
parser.add_argument('-j', '--join', help='joining wordlists together', type=str, nargs='+')
parser.add_argument('-rp', '--remove-repeated', help='remove repeated words', action='store_true')


args_dict = vars(parser.parse_args())
arg = parser.parse_args()

if len(argv) == 1:
    parser.print_help()

if args_dict['output'] is None and args_dict['join']is None and len(argv) != 1:
    print('-o/--output arguments are required\n')
    exit()

if args_dict['input'] is None and args_dict['make_wordlist'] is None and args_dict['combine_words'] is None and args_dict['remove_from'] is None and args_dict['join'] is None and len(argv) != 1:
    print('Wordgen needs at least one input\n')
    exit()


if args_dict['remove_from'] is not None:
    if args_dict['input'] is not None:
        print('option -rm should be used alone\n')
        exit()
    elif args_dict['make_wordlist'] is not None:
        print('option -rm should be used alone\n')
        exit()
    elif args_dict['combine_words'] is not None:
        print('option -rm should be used alone\n')
        exit()


lst = []
if args_dict['join'] is not None:
    try:
        if not is_printed:
            print('Working on it ...\n')
            is_printed = True
        try:
            tm
        except NameError:
            tm = time()
        encod = detect(open(args_dict['join'][0], 'rb').readline())['encoding']
        with open(args_dict['join'][0], 'a', encoding=encod) as r:
            for ut in args_dict['join'][1:]:
                necod = detect(open(ut, 'rb').readline())['encoding']
                with open(ut, 'r', encoding=necod) as ry:
                    while True:
                        data = ry.readline()
                        if not data:
                            break
                        r.write(data)
    except FileNotFoundError as le:
        print('File is not found ', le)

if args_dict['combine_words'] is not None:
    if args_dict['input'] is not None:
        print('option -c coudn\'t be used with -i')
        exit()
    elif args_dict['make_wordlist'] is not None:
        print('option -m coudn\'t be used with -c')
        exit()
    tm = time()
    if not is_printed:
        print('Working on it ...\n')
        is_printed = True
    lst = list(product(tuple(args_dict['combine_words']), repeat=len(args_dict['combine_words'])))

if args_dict['make_wordlist'] is not None:
    try:
        tm
    except NameError:
        tm = time()
    if not is_printed:
        print('Working on it ...\n')
        is_printed = True
    for n in list(product(*tuple(args_dict['make_wordlist']))):
        lst.append(''.join(n))

if args_dict['remove_from'] is not None:
    if not is_printed:
        print('Working on it ...\n')
        is_printed = True
    try:
        tm
    except NameError:
        tm = time()
    try:
        a, b = tuple(args_dict['remove_from'])
        lst = open(a, 'r').read().split('\n')
        for v in open(b, 'r').read().split('\n'):
            if lst.count(v) != 0:
                del lst[lst.index(v)]
    except FileNotFoundError as le:
        print('File not found', le)
if args_dict['input'] is not None:
    try:
        tm
    except NameError:
        tm = time()
    if not is_printed:
        print('Working on it ...\n')
        is_printed = True
    try:
        for t in args_dict['input']:
            encod = detect(open(str(t), 'rb').read())['encoding']
            for l in open(str(t), 'rb').read().decode(encod).split('\n'):
                lst.append(l.strip('\r'))
    except FileNotFoundError as le:
        print('File not found ', le)
if arg.filter_words:
    lst = list(filter(flt, lst))
if arg.randomize:
    try:
        for i in range(len(lst)):
            h = randint(0, (len(lst) - 1))
            lst[i], lst[h] = lst[h], lst[i]
    except NameError:
        print('lst is not defined')
if args_dict['remove_repeated'] is True:
    if not is_printed:
        print('Working on it...\n')
        is_printed = True
    for mon in range(len(lst)):
        if lst.count(lst[mon]) != 0:
            del lst[mon]
if args_dict['output'] is not None:
    try:
        with open(args_dict['output'][0], 'w') as f:
            if args_dict['combine_words'] is not None:
                for u in lst:
                    f.write(''.join(list(u)) + '\n')
                tn = time()
                print('Done in '+str(tm-tn)+' seconds')
            else:
                f.write('\n'.join(lst))
                tn = time()
                print('Done in ' + str(tm - tn) + ' seconds')
        del lst
        print('\n')
        exit()
    except NameError:
        print('lst is not defined')
        exit()
try:
    print('Done in '+str((tm-time()))+' seconds.')
    print('\n')
except NameError:
    print('\n')
    exit()