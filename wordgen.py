#!/usr/bin/python3
import os
import random
import sys
import string
import itertools
pr = """
#################################################################
created by me in 18 Aug 2018
0-randomize a wordlist
1-remove repeated words from wordlist
2-create a wordlist
3-combine a words
4-remove a list from another one
5-exit
#################################################################"""


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pr)
    a = input('choose ==> ')
    num = int(a if a not in string.ascii_letters[:52] else main())
    if num == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        file = open(input('input file path ==> '), 'r')
        lst = list(file.read().split('\n'))
        for i in range(len(lst)):
            h = random.randint(0, len(lst) - 1)
            lst[i], lst[h] = lst[h], lst[i]
        file2 = open(input('output file path ==> '), 'w')
        file2.write("\n".join(lst))
        file.close()
        file2.close()
        main()
    elif num == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        file1 = open(input('insert input file ==> '), 'r')
        file2 = open(input('insert output file ==> '), 'w')
        file2.write("\n".join(list(set(file1.read().split('\n')))))
        file1.close()
        file2.close()
        main()
    elif num == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        file3 = open(input('insert output file ==> '), 'w')
        y = input('inter characters ==> ')
        min = int(input('insert min len ==> '))
        max = int(input('insert max len ==> '))
        for g in range(min, max + 1):
            for xs in itertools.product(y, repeat=g):
                file3.write(''.join(xs) + '\n')
        file3.close()
        main()
    elif num == 3:
        print('a')
        main()
    elif num == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        x = input('insert first list ==> ')
        file4 = open(x, 'r')
        file5 = open(input('insert second list please ==> '))
        lst2 = file4.read().split('\n')
        for v in file5.read().split('\n'):
            if lst2.count(v) != 0:
                del lst2[lst2.index(v)]
        file4.close()
        file4 = open(x, 'w')
        file4.write("\n".join(lst2))
        file4.close()
        file5.close()
        main()
    elif num == 5:
        print('goodbye')
        sys.exit()
    else:
        main()


main()
