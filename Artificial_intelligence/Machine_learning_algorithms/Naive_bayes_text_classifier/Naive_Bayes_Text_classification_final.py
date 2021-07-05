#!/usr/bin/env python3

import os
from math import log


def dict_generator(class_name):
    d = dict()
    all_words = 0
    path = 'data/train/' + class_name

    files = []
    i = 1

        # r=root, d=directories, f = files
    for r, dir, f in os.walk(path):

        for file in f:
            files.append(os.path.join(r, file))


    for f in files:
        file = open(f, "rt")
        try:
            data = file.read()
        except:
            continue

        wordlist = data.split()
        wordlist = [x for x in wordlist if len(
            x) > 2 and ':' not in x and x != 'the' and x != 'and' and x != 'was' and '=' not in x and ';' not in x and '/' not in x]
        wordfreq = []
        all_words = all_words + len(wordlist)
        for w in wordlist:
            wordfreq.append(wordlist.count(w))

        if i == 1:
            d = dict(list(zip(wordlist, wordfreq)))
            i = i + 1
        else:
            new_dict = dict(list(zip(wordlist, wordfreq)))
            d = {x: d.get(x, 0) + new_dict.get(x, 0) for x in set(d).union(new_dict)}
    for word in d:
        x = d[word]
        x = x / all_words
        temp_d = {word: x}
        d.update(temp_d)

    return d


def Bayesian_test(folder_name):
    path = 'data/test/' + folder_name

    files = []
    i = 1

    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))


    for f in files:

        d0_t_prob = 0
        d1_t_prob = 0
        d2_t_prob = 0
        d3_t_prob = 0
        file = open(f, "rt")
        try:
            data = file.read()
        except:
            continue

        wordlist = data.split()
        wordlist = [x for x in wordlist if len(
            x) > 2 and ':' not in x and x != 'the' and x != 'and' and x != 'was' and '=' not in x and ';' not in x and '/' not in x]


        for w in wordlist:
            # print(str(w))

            try:
                d0_prob = d0[str(w)]
                d0_t_prob = d0_t_prob + log(d0_prob)
            except:
                continue

        for w in wordlist:
            # print(str(w))

            try:
                d1_prob = d1[str(w)]
                d1_t_prob = d1_t_prob + log(d1_prob)
            except:
                continue

        for w in wordlist:
            # print(str(w))

            try:
                d2_prob = d2[str(w)]
                d2_t_prob = d2_t_prob + log(d2_prob)
            except:
                continue

        for w in wordlist:
            # print(str(w))

            try:
                d3_prob = d3[str(w)]
                d3_t_prob = d3_t_prob + log(d3_prob)
            except:
                continue


        d0_t_prob = abs(d0_t_prob)
        d1_t_prob = abs(d1_t_prob)
        d2_t_prob = abs(d2_t_prob)
        d3_t_prob = abs(d3_t_prob)
        max_prob = max(d0_t_prob, d1_t_prob, d2_t_prob, d3_t_prob)

        # print('rec.autos:',d0_t_prob,'comp.graphics:',d1_t_prob,'comp.windows.x:',d2_t_prob,'rec.sport.hockey:',d3_t_prob)
        if (max_prob == d0_t_prob):
            print("The file",f, "belongs to class comp.windows.x" )
            # a =0


        if(max_prob == d1_t_prob):
            print("The file", f, "belongs to class sci.crypt")
            # a = 0

        if (max_prob == d2_t_prob):
            print("The file", f, "belongs to class rec.sport.hockey")

        if (max_prob == d3_t_prob):
            print("The file", f, "belongs to class talk.politics.misc")

    return

if __name__ == "__main__":




    d0 = dict_generator('comp.windows.x')
    d1 = dict_generator('sci.crypt')
    d2 = dict_generator('rec.sport.hockey')
    d3 = dict_generator('talk.politics.misc')



    #-------------------------- testing -------------------------#



    print("test folder 1:")
    Bayesian_test('talk.politics.misc')
    print("test folder 2:")
    Bayesian_test('sci.crypt')
    print("test folder 3:")
    Bayesian_test('rec.sport.hockey')
    print("test folder 4:")
    Bayesian_test('comp.windows.x')
    print("End")


