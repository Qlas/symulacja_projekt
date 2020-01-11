import random
import numpy

def appearTime(time, mean, dev):
    while True:
        element = time + int(numpy.random.normal(mean, dev))
        if element > time:
            return element

def mainLoop(timestart, timeend):
    clientNumber = 0
    queueToMeal = [[], []]                                          #queue to below place
    mealPlace = [0, 0]                                              #place where meal is put for client
    timeInmealPlace = [0, 0]

    queueToCash = [[], []]
    cashRegister = [0, 0, 0, 0]
    timeinCash = [0, 0, 0, 0]
    queueNumber = 0

    nextClientAppear = appearTime(timestart, 6, 3)

    for time in range(int(timestart), int(timeend)+1):
        if nextClientAppear == time:
            clientNumber += 1
            min(queueToMeal, key=len).append(clientNumber)          #client go to smallest queue
            nextClientAppear = appearTime(time, 60, 30)             #get time when another client appear

        for i in range(len(mealPlace)):
            if timeInmealPlace[i] == time:
                min(queueToCash, key=len).append(mealPlace[i])
                mealPlace[i] = 0                                    #client gets his meal
                timeInmealPlace[i] = 0


            if mealPlace[i] == 0 and len(queueToMeal[i]) != 0:
                mealPlace[i] = queueToMeal[i][0]                    #client move from queue to meal
                queueToMeal[i].pop(0)                               #del client from queue
                timeInmealPlace[i] = appearTime(time, 20, 10)

        for i in range(len(cashRegister)):
            if timeinCash[i] == time:
                cashRegister[i] = 0
                timeinCash[i] = 0

            if cashRegister[i] == 0 and any(len(Queue) != 0 for Queue in queueToCash):
                while len(queueToCash[queueNumber]) == 0:
                    queueNumber = queueNumber+1 if queueNumber < len(queueToCash)-1 else 0
                timeinCash[i] = appearTime(time, 20, 10)            #get how long client stay in cash
                cashRegister[i] = queueToCash[queueNumber][0]       #move client from queue to cash
                queueToCash[queueNumber].pop(0)                     #delet client from queue


    print(mealPlace)
    print(timeInmealPlace)
    print(queueToMeal)
    print(timeinCash)
    print(cashRegister)
    print(queueToCash)

    return sum(len(x) for x in queueToMeal) + sum(x is not 0 for x in cashRegister), \
           sum(len(x) for x in queueToCash) + sum(x is not 0 for x in mealPlace)








start = 8.00
end = 18.00
queueToMeal, queueToCash = mainLoop(start*3600, end*3600)

print("klienci którzy zostali przy oddawaniu posiłku na koniec dnia: ", queueToMeal)
print("klienci którzy zostali przy kasie na koniec dnia: ", queueToCash)