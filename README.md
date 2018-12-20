# wordgen
wordgen is a free tool to make custom wordlist and editing other wordlists

## usage:
use `python ./wordgen -h` to print help like below:
```
                         __
 _      ______  _________/ /___ ____  ____
| | /| / / __ \/ ___/ __  / __ `/ _ \/ __ \
| |/ |/ / /_/ / /  / /_/ / /_/ /  __/ / / /
|__/|__/\____/_/   \__,_/\__, /\___/_/ /_/
                        /____/

usage: Wordgen.py -h [input] [options]

Wordgen v 1.0.0 - Created By Mohammadamin Alidoost

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT [INPUT ...], --input INPUT [INPUT ...]
                        input file to Wordgen
  -m MAKE_WORDLIST [MAKE_WORDLIST ...], --make-wordlist MAKE_WORDLIST [MAKE_WORDLIST ...]
                        make wordlist with wordgen
  -mb MAKE_BIG_WORDLIST [MAKE_BIG_WORDLIST ...], --make-big-wordlist MAKE_BIG_WORDLIST [MAKE_BIG_WORDLIST ...]
                        make big wordlist
  -o OUTPUT, --output OUTPUT
                        get output from wordgen
  -r, --randomize       randomize output
  -rm REMOVE_FROM REMOVE_FROM, --remove-from REMOVE_FROM REMOVE_FROM
                        remove a wordlist from another one
  -f, --filter-words    filter words that is easier to pronouns
  -c COMBINE_WORDS [COMBINE_WORDS ...], --combine-words COMBINE_WORDS [COMBINE_WORDS ...]
                        combine words together (with replacement)
  -cw COMBINE_WITHOUT [COMBINE_WITHOUT ...], --combine-without COMBINE_WITHOUT [COMBINE_WITHOUT ...]
                        combine words with replacement
  -j JOIN [JOIN ...], --join JOIN [JOIN ...]
                        joining wordlists together
  -rp, --remove-repeated
                        remove repeated words
  -a ADD, --add ADD     use an argument between words (used with -cw)
```
### input
`-i` or `--input` will input a wordlist or text file to modifie it,it could be more than one file,for example:

`python ./wordgen.py -i a.txt b.txt c.txt`

this command will put the text file in memory so it shouldn't be too large.
### making wordlist
`-m` or `--make-wordlist` will make a wordlist and will put it in memory,to use this command u should enter `-m` and enter charracters that u want to use and splite them with space.

### example:

`python ./wordgen.py -m abcd mank adn`

and the output should have 3 charracters

### output:

```
ama
amd
amn
aaa
aad
aan
ana
and
ann
aka
akd
akn
bma
bmd
bmn
baa
bad
ban
bna
bnd
bnn
bka
bkd
bkn
cma
cmd
cmn
caa
cad
can
cna
cnd
cnn
cka
ckd
ckn
dma
dmd
dmn
daa
dad
dan
dna
dnd
dnn
dka
dkd
dkn
````

you are not forced to write all of the charracters you want to use,there are some shorter way to use

```
?a = abcdefghijklmnopqrstuvwxyz1234567890[-=@_!#$%^&*()<>?/\|}{~:]
?d = 1234567890
?l = abcdefghijklmnopqrstuvwxyz
?e = [-=@_!#$%^&*()<>?/\|}{~:]
```

for example instead of :

`python ./wordgen.py -m abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz` you can use:

`python ./wordgen.py -m ?l ?l ?l`

## make big wordlist
`-mb` coulde be used like `-m` but it will write wordlist directly instead of keeping words on memory

## output

`-o` used for saving words that keeped temperory on memory

## randomize

`-r` used for making words that has been keepen on memory random

### for exapmle:

```
abc
unk
hgp
```

### would be:

```
unk
hgp
abc
```

## remove from
`-rf` would remove a wordlist from another one

### for example:

`python -rf a.txt b.txt`

this command will remove all words on b.txt from a.txt

## filter word

`-f` will remove words that are not easy to pronouns (from memory words)

