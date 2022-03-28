import random


class game(object):
    # Hangman game
    dangle = []
    dangle.append(' =====')
    dangle.append(' ')
    dangle.append(' ')
    dangle.append(' ')
    dangle.append(' ')
    dangle.append(' ')
    dangle.append(' =====')
    lad = {}
    lad[0] = [' @ ']
    lad[1] = [' @ ', ' ! ']
    lad[2] = [' @ ', '/! ']
    lad[3] = [' @ ', '/!\\ ']
    lad[4] = [' @ ', '/!\\ ', '/ ']
    lad[5] = [' @ ', '/!\\ ', '/ \\ ']
    z = []
    states = ''' algeria angola benin botswana burkinafaso burundi cameroon chad comoros djibouti egypt equatorialguinea eritrea eswatini ethiopia gabon ghana guinea guineabissau ivorycoast kenya lesotho liberia libya madagascar malawi mali mauritania mauritius morocco mozambique namibia niger nigeria democraticrepublicofcongo rwanda senegal seychelles sierraleone somalia southafrica southsudan sudan tanzania gambia togo tunisia uganda zambia zimbabwe '''.split()
    design = '@_@\'@_@\'@_@\'@_@\'@_@\'@_@\'@_@\'@_@\'@_@\'@_@\''

    def __init__(K):
        m, n = 2, 0
        K.z.append(K.dangle[:])
        for k in K.lad.values():
            p, n = K.dangle[:], 0
            for i in k:
                p[m + n] = i
                n += 1
            K.z.append(p)

    def Select_Word(K):
        return K.states[random.randint(0, len(K.states) - 1)]

    def photo(K, x, wordLen):
        for slash in K.z[x]:
            print(slash)

    def game(K, term, value, notpresent):
        q = input()
        if q == None or len(q) != 1 or (q in value) or (q in notpresent):
            return None, False
        m = 0
        p = q in term
        for i in term:
            if i == q:
                value[m] = i
            m += 1
        return q, p

    def data(K, data):
        x = len(K.design)
        print(K.design[:-3])
        print(data)
        print(K.design[3:])

    def process(K):
        name = input("Enter your name: ")
        print("Good Luck ,", name)
        print('*****Hangman game starts*****')
        term = list(K.Select_Word())
        outcome = list('_' * len(term))
        print('The state is: ', outcome)
        y, m, k = False, 0, []
        while m < len(K.z) - 1:
            print('Guess the state name : ', end='')
            x, x1 = K.game(term, outcome, k)
            if x == None:
                print('Repeated character.')
                continue
            print(''.join(outcome))
            if outcome == term:
                K.data('Excellent ! You saved a life :)')
                y = True
                break
            if not x1:
                k.append(x)
                m += 1
            K.photo(m, len(term))
            print('Missed words: ', k)
        if not y:
            K.data('The state was \'' + ''.join(term) +
                   '\' Game over ! Man was hanged')


a = game().process()
