# import random
# import numpy
# import random
#
#
# def appearTime(time, mean):
#     while True:
#         element = time + int(numpy.random.poisson(mean))
#         if element > time:
#             return element
#
#
# class Client:
#     appear = 0
#     timeInMealPlace = 0
#     timeInCash = 0
#     timeSystem = 0
#
#     def __init__(self, time, mean):
#         self.appear = appearTime(time, mean)
#
#     def timeInSystem(self, time):
#         self.timeSystem = time - self.appear
#
#
# class Place:
#     client = []
#
#     def checkTime(self, time):
#         try:
#             if time == self.client.timeInMealPlace:
#                 return True
#         except AttributeError:
#             return False
#
#     def checkTime1(self, time):
#         try:
#             if time == self.client.timeInCash:
#                 return True
#         except AttributeError:
#             return False
#
#
# def createVariables(meal, cash, cashQueue):
#     mealPlace = []
#     queueToMeal = []
#     timeInmealPlace = []
#     queueToCash = []
#     cashRegister = []
#     timeinCash = []
#     for i in range(meal):
#         mealPlace.append(0)  # queue to below place
#         queueToMeal.append([])  # place where meal is put for client
#         timeInmealPlace.append(0)  # how long
#
#     for i in range(cashQueue):
#         queueToCash.append([])
#
#     for i in range(cash):
#         cashRegister.append(0)
#         timeinCash.append(0)
#     return mealPlace, queueToMeal, timeInmealPlace, queueToCash, cashRegister, timeinCash
#
#
# def mainLoop(timestart, timeend, meal, cash, cashQueue):
#     mealPlace1 = [Place()]
#     cashRegister1 = [Place()]
#     clientList = []
#     clientList1 = []
#     mealPlace, queueToMeal, timeInMealPlace, queueToCash, cashRegister, timeinCash = createVariables(meal, cash,
#                                                                                                      cashQueue)
#     clientNumber = 0
#     queueNumber = 0
#     clientList1.append(Client(timestart, 60))
#
#     for time in range(int(timestart), int(timeend) + 1):
#         if any(client.appear == time for client in clientList1):
#             clientNumber += 1
#             min(queueToMeal, key=len).append(clientList1[-1])  # client go to smallest queue
#             clientList1.append(Client(time, 10))
#             clientList.append(time)  # get time when client appear
#
#         for i in range(len(mealPlace)):
#             if mealPlace1[i].checkTime(time):
#                 min(queueToCash, key=len).append(mealPlace1[i])
#                 mealPlace1[i].client = []  # client gets his meal
#
#             if mealPlace1[i].client == [] and len(queueToMeal[i]) != 0:
#                 mealPlace1[i].client = queueToMeal[i][0]
#                 mealPlace[i] = queueToMeal[i][0]  # client move from queue to meal
#                 mealPlace[i].timeInMealPlace = appearTime(time, 20)
#                 queueToMeal[i].pop(0)  # del client from queue
#
#         for i in range(len(cashRegister)):
#             if cashRegister1[i].checkTime1(time):
#                 # clientList[cashRegister[i]-1] = time - clientList[cashRegister[i]-1]            #get how much time client stay in our queue's
#                 cashRegister1[i].client[0].timeInSystem(time)
#                 cashRegister1[i] = 0
#
#             if cashRegister[i] == 0 and any(len(Queue) != 0 for Queue in queueToCash):
#                 while len(queueToCash[queueNumber]) == 0:
#                     queueNumber = queueNumber + 1 if queueNumber < len(queueToCash) - 1 else 0
#                 cashRegister1[i] = queueToCash[queueNumber][0]  # move client from queue to cash
#                 cashRegister1[i].timeInCash = appearTime(time, 20)  # get how long client stay in cash
#                 queueToCash[queueNumber].pop(0)  # delet client from queue
#
#     print(clientList1[0].timeSystem)
#
#     return sum(len(x) for x in queueToMeal) + sum(x is not 0 for x in mealPlace), \
#            sum(len(x) for x in queueToCash) + sum(x is not 0 for x in cashRegister), \
#            round(numpy.mean(clientList), 2)
#
#
# '''
# TODO LIST:
#     1- random events:
#         - zacięcie kasy
#         - przerwa kasierki
#         - uzupełnienie jedzenia na stanowisku do nakładania
#         - zwiększona średnia liczba klientów co 1,5h przez 10 min
#
#     2 - Klient nie przychodzi, jeśli najkrótsza kolejka jest dłuższa niż 30 osób
#
#     3 - testy
#
#     4 - kryterium jakości
#         - ilość osób które odeszły z powodu zbyt długich kolejek
#         - ilość obsłużonych klientów
#         - maksymalna długości jakielkowiek kolejki w systemie
#         - jak dlugo kasa stoi pusta
#
#     5 - różne scenariusze testowe
#         - różna ilość stanowisk do nakładania
#         - różna ilość kas
#         - różna ilość kolejek do kas
#         - różna częstotliwość pojawiania się klientów
#         - różny czas przy stanowisku i kasie
#
# '''
#
# start = 8.00  # time when sks is opening
# end = 18.00  # time when sks is closing
# mealPlace = 1  # how many mealplace we have
# cashRegister = 1  # how many cash register
# queueToCash = 1  # how many queue to cash register
# queueToMeal, queueToCash, mean = mainLoop(start * 3600, end * 3600, mealPlace, cashRegister, queueToCash)
#
# print("klienci którzy zostali przy oddawaniu posiłku na koniec dnia: ", queueToMeal)
# print("klienci którzy zostali przy kasie na koniec dnia: ", queueToCash)
# print("Średni czas przebywania klientów w systemie: ", mean, " sekund")



import random
import numpy
import time

def appearTime(time, mean):
    while True:
        element = time + int(numpy.random.poisson(mean))
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



def mainLoop(timestart, timeend, meal, cash, cashQueue, clientmean):

    mealPlace, queueToMeal, timeInMealPlace, queueToCash, cashRegister, timeinCash = createVariables(meal, cash, cashQueue)
    clientNumber = 0
    queueNumber = 0
    clientList = []
    escapeClients = 0
    nextClientAppear = appearTime(timestart, clientmean)

    for time in range(int(timestart), int(timeend)+1):
        if nextClientAppear == time:
            if len(min(queueToMeal, key=len)) > 30:
                escapeClients += 1
            else:
                clientNumber += 1
                clientList.append(time)
                min(queueToMeal, key=len).append(clientNumber)          #client go to smallest queue
            nextClientAppear = appearTime(time, clientmean)             #get time when another client appear

        for i in range(len(mealPlace)):
            if timeInMealPlace[i] == time:
                min(queueToCash, key=len).append(mealPlace[i])
                mealPlace[i] = 0                                    #client gets his meal
                timeInMealPlace[i] = 0


            if mealPlace[i] == 0 and len(queueToMeal[i]) != 0:
                mealPlace[i] = queueToMeal[i][0]                    #client move from queue to meal
                queueToMeal[i].pop(0)                               #del client from queue
                timeInMealPlace[i] = appearTime(time, 20)

        for i in range(len(cashRegister)):
            if timeinCash[i] == time:
                clientList[cashRegister[i] - 1] = time - clientList[cashRegister[i] - 1]  # get how much time client stay in our queue's
                cashRegister[i] = 0
                timeinCash[i] = 0

            if cashRegister[i] == 0 and any(len(Queue) != 0 for Queue in queueToCash):
                while len(queueToCash[queueNumber]) == 0:
                    queueNumber = queueNumber+1 if queueNumber < len(queueToCash)-1 else 0
                timeinCash[i] = appearTime(time, 20)            #get how long client stay in cash
                cashRegister[i] = queueToCash[queueNumber][0]       #move client from queue to cash
                queueToCash[queueNumber].pop(0)                     #delet client from queue

    clientList = [x for x in clientList if x < timeend-timestart]
    # return sum(len(x) for x in queueToMeal) + sum(x is not 0 for x in mealPlace), \
    #        sum(len(x) for x in queueToCash) + sum(x is not 0 for x in cashRegister), \
    return  round(numpy.mean(clientList), 2), \
            escapeClients








start = 8.00
end = 18.00
mealPlace = [1,2,3]
cashRegister = 2
queueToCash = 1
clientAppearMean = [15, 16, 17, 18, 19, 20]

systemMean = []
escape = []
timestart = time.time()
for j in mealPlace:
    mean1 = []
    esc1 = []
    for i in clientAppearMean:
        mean = []
        esc = []
        for n in range(10):                                                                                          #n repeat
            a, b = mainLoop(start*3600, end*3600, j, cashRegister, queueToCash,i)
            mean.append(a)
            esc.append(b)
        mean1.append(mean)
        esc1.append(esc)
    systemMean.append(mean1)
    escape.append(esc1)

systemMean = [round(numpy.mean(a),2) for a in systemMean]
escape = [round(numpy.mean(a),2) for a in escape]
print(systemMean)
print(escape)
print("czas trwania: ", time.time()-timestart)
# print("klienci którzy zostali przy oddawaniu posiłku na koniec dnia: ", queueToMeal)
# print("klienci którzy zostali przy kasie na koniec dnia: ", queueToCash)
# print("Średni czas przebywania klientów w systemie: ", mean, " sekund")
# print("Klienci którzy zrezygnowali z powodu zbyt dużej liczby osób w kolejce: ", escape)