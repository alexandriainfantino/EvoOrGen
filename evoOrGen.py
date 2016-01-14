__author__ = 'Lexie Infantino'
import random
import string

def main(*args):
    #for counting iterations, not important
    iteration = 0
    str = 'Hello, World'
    # gen string alpha/numeric/puntuation/whitespace
    ranStr = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation+ string.whitespace) for n in range(len(str))])
    fitLvl = fitness(str, ranStr)
    # if fit level of new evolution is better, keep new string, other wise ignore.
    while ranStr != str:
        tempStr = evolve(ranStr)
        if fitLvl < fitness(str, tempStr):
            pass
        if fitLvl > fitness(str, tempStr):
            ranStr = tempStr
            fitLvl = fitness(str, tempStr)
        iteration += 1
        # print every 100th iteration
        if iteration %100 == 0:
            print('Iteration ', iteration, ': '+ranStr)
    print('Iteration ', iteration, ': '+ranStr)

'''
generate fitness of randomized string compare to original.
square numbers to remove negatives
'''
def fitness(str, ranStr):
    x = 0
    tfit = 0
    while x != len(str):
        strx = ord(str[x])**2
        rstr = ord(ranStr[x])**2
        if(strx > rstr):
            fit = strx - rstr
        else:
            fit = rstr - strx
        tfit = tfit+fit
        x = x+1
    return tfit


'''
pick a random char from random string and turn it into another random char
'''
def evolve(str):
    index = random.randint(0, len(str) - 1)
    strLst = list(str)
    strLst[index] = (random.choice(string.ascii_letters + string.digits + string.punctuation + string.whitespace))
    str = ''.join(strLst)
    return str

main()