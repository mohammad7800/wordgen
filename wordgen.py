import argparse
from sys import argv, exit
from random import randint, choice
from itertools import product, combinations, permutations
from time import time
from encod import detect
import re
is_printed = False
a = r'abcdefghijklmnopqrstuvwxyz1234567890[-=@_!#$%^&*()<>?/\|}{~:]'
d = '1234567890'
ll = 'abcdefghijklmnopqrstuvwxyz'
e = '[-=@_!#$%^&*()<>?/\|}{~:]'


def replace_list(h:list):
    global a
    global d
    global ll
    global e
    while '?a' in h:
        h[h.index('?a')] = a
    while '?l' in h:
        h[h.index('?l')] = ll
    while '?d' in h:
        h[h.index('?d')] = d
    while '?e' in h:
        h[h.index('?e')] = e
    return h


def list_get(lm, idx, default):
    try:
        return lm[idx]
    except IndexError:
        return default


def flt(x):
    au = 'auioe1234567890'
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


def remove_duplicate(s):
    if (len(s)) < 2:
        return s

    result = []
    for i in s:
        if i not in result:
            result.append(i)

    return ''.join(result)


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
parser.add_argument('-mb', '--make-big-wordlist', help='make big wordlist', type=str, nargs='+')
parser.add_argument('-o', '--output', type=str, help='get output from wordgen', nargs=1)
parser.add_argument('-r', '--randomize', action='store_true', help='randomize output')
parser.add_argument('-rm', '--remove-from', type=str, help='remove a wordlist from another one', nargs=2)
parser.add_argument('-f', '--filter-words', help='filter words that is easier to pronouns', action='store_true')
parser.add_argument('-c', '--combine-words', help='combine words together (with replacement)', nargs='+', type=str)
parser.add_argument('-cw', '--combine-without', help='combine words with replacement', nargs='+', type=str)
parser.add_argument('-j', '--join', help='joining wordlists together', type=str, nargs='+')
parser.add_argument('-rp', '--remove-repeated', help='remove repeated words', action='store_true')
parser.add_argument('-a', '--add', help='use an argument between words (used with -cw)', nargs=1, default='')

args_dict = vars(parser.parse_args())
arg = parser.parse_args()

if len(argv) == 1:
    parser.print_help()


if args_dict['output'] is None and args_dict['join']is None and len(argv) != 1:
    print('-o/--output arguments are required\n')
    exit()

if args_dict['input'] is None and args_dict['make_wordlist'] is None and args_dict['combine_words'] is None and args_dict['combine_without'] is None and args_dict['remove_from'] is None and args_dict['join'] is None and args_dict['make_big_wordlist'] is None and len(argv) != 1:
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
    elif args_dict['combine_without'] is not None:
        print('option -rm should be used alone\n')
        exit()


lst = []
if args_dict['make_big_wordlist'] is not None:
    if args_dict['make_wordlist'] is not None:
        print('-mb, --make-big-wordlist could be used only with -o')
        exit()
    elif args_dict['combine_words'] is not None:
        print('-mb, --make-big-wordlist could be used only with -o')
        exit()
    elif args_dict['remove_from'] is not None:
        print('-mb, --make-big-wordlist could be used only with -o')
        exit()
    elif args_dict['input'] is not None:
        print('-mb, --make-big-wordlist could be used only with -o')
        exit()
    elif args_dict['join'] is not None:
        print('-mb, --make-big-wordlist could be used only with -o')
        exit()
    elif args_dict['remove_repeated'] is not False:
        print('-mb, --make-big-wordlist could be used only with -o')
        exit()
    elif args_dict['randomize'] is not False:
        print('-mb, --make-big-wordlist could be used only with -o')
        exit()
    elif args_dict['filter_words'] is not False:
        print('-mb, --make-big-wordlist could be used only with -o')
        exit()
    if args_dict['output'] is None:
        print('-o, --output should\'t be none')
        exit()
    tm = time()
    print('Working on it ...\n')
    for n in args_dict['make_big_wordlist']:
        args_dict['make_big_wordlist'][args_dict['make_big_wordlist'].index(n)] = remove_duplicate(n)
    with open(args_dict['output'][0], 'w') as ng:
        for k in product(*tuple(args_dict['make_big_wordlist'])):
            ng.write("".join(k)+'\n')
    print('Done in '+str(int(time()-tm))+' seconds')
    exit()
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
    for r in product(tuple(args_dict['combine_words']), repeat=len(args_dict['combine_words'])):
        lst.append(r)

if args_dict['combine_without'] is not None:
    tm = time()
    if args_dict['input'] is not None:
        print('option -cw coudn\'t be used with -i')
        exit()
    elif args_dict['make_wordlist'] is not None:
        print('option -m coudn\'t be used with -cw')
        exit()
    if not is_printed:
        print('Working on it ...\n')
        is_printed = True
    for i in range(2, len(args_dict['combine_without'])):
        for t in combinations(args_dict['combine_without'], i):
            for tl in permutations(list(t)):
                lst.append(list_get(args_dict['add'], 0, '').join(tl))

if args_dict['make_wordlist'] is not None:
    try:
        tm
    except NameError:
        tm = time()
    if not is_printed:
        print('Working on it ...\n')
        is_printed = True
    args_dict['make_wordlist'] = replace_list(args_dict['make_wordlist'])
    for rg in args_dict['make_wordlist']:
        args_dict['make_wordlist'][args_dict['make_wordlist'].index(rg)] = remove_duplicate(rg)
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
    for mon in lst:
        if lst.count(mon) != 0:
            del lst[lst.index(mon)]
if args_dict['output'] is not None:
    try:
        with open(args_dict['output'][0], 'w') as f:
            if args_dict['combine_words'] is not None:
                for u in lst:
                    f.write(''.join(list(u)) + '\n')
                tn = time()
                print('Done in '+str(int(tn-tm))+' seconds')
            else:
                f.write('\n'.join(lst))
                tn = time()
                print('Done in ' + str(int(tn-tm)) + ' seconds')
        del lst
        print('\n')
        exit()
    except NameError as fp:
        print(fp)
        exit()
try:
    print('Done in '+str(int(time()-tn))+' seconds.')
    print('\n')
except NameError:
    print('\n')
    exit()
