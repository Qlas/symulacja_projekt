import random
import numpy

def appearTime(time, mean, dev):
    while True:
        element = time + int(numpy.random.normal(mean, dev))
        if element > time:
            return element

def createVariables(meal, cash, cashQueue):
    mealPlace = []
    queueToMeal = []
    timeInmealPlace = []
    queueToCash = []
    cashRegister = []
    timeinCash = []
    for i in range(meal):
        mealPlace.append(0)                                     #queue to below place
        queueToMeal.append([])                                  #place where meal is put for client
        timeInmealPlace.append(0)                               #how long

    for i in range(cashQueue):
        queueToCash.append([])

    for i in range(cash):
        cashRegister.append(0)
        timeinCash.append(0)
    return mealPlace, queueToMeal, timeInmealPlace, queueToCash, cashRegister, timeinCash



def mainLoop(timestart, timeend, meal, cash, cashQueue):

    mealPlace, queueToMeal, timeInMealPlace, queueToCash, cashRegister, timeinCash = createVariables(meal, cash, cashQueue)
    clientNumber = 0
    queueNumber = 0

    nextClientAppear = appearTime(timestart, 60, 30)

    for time in range(int(timestart), int(timeend)+1):
        if nextClientAppear == time:
            clientNumber += 1
            min(queueToMeal, key=len).append(clientNumber)          #client go to smallest queue
            nextClientAppear = appearTime(time, 60, 30)             #get time when another client appear

        for i in range(len(mealPlace)):
            if timeInMealPlace[i] == time:
                min(queueToCash, key=len).append(mealPlace[i])
                mealPlace[i] = 0                                    #client gets his meal
                timeInMealPlace[i] = 0


            if mealPlace[i] == 0 and len(queueToMeal[i]) != 0:
                mealPlace[i] = queueToMeal[i][0]                    #client move from queue to meal
                queueToMeal[i].pop(0)                               #del client from queue
                timeInMealPlace[i] = appearTime(time, 20, 10)

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
    print(timeInMealPlace)
    print(queueToMeal)
    print(timeinCash)
    print(cashRegister)
    print(queueToCash)

    return sum(len(x) for x in queueToMeal) + sum(x is not 0 for x in mealPlace), \
           sum(len(x) for x in queueToCash) + sum(x is not 0 for x in cashRegister)








start = 8.00
end = 18.00
mealPlace = 2
cashRegister = 4
queueToCash = 1
queueToMeal, queueToCash = mainLoop(start*3600, end*3600, mealPlace, cashRegister, queueToCash)

print("klienci którzy zostali przy oddawaniu posiłku na koniec dnia: ", queueToMeal)
print("klienci którzy zostali przy kasie na koniec dnia: ", queueToCash)