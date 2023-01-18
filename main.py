import random
import re
import datetime
import responsesList as RL

# calculate probability that parent message prompts the child response
def messageProbability(parentMessage = "", keyWords = [], isErrorMessage = False):
    # error message has probability of 0 so if all other responses have probability of -1 (no keywords for any of the
    # responses) error message will send
    if isErrorMessage == True:
        return 0
    messageCertainty = 0

    # count how many keywords are in message
    for word in parentMessage:
        if word in keyWords:
            messageCertainty += 1
    # if no keywords are present in message, response will have the lowest probability (-1) and won't be chosen
    if messageCertainty == 0:
        percentAccurate = -1
    else:
        # percent of words in the message that are keywords = message probability
        percentAccurate = float(messageCertainty)/float(len(parentMessage))

    return percentAccurate

# map child response to the probability that the parent message prompts that response
def messageMap(scenario, message):
    # each scenario has different map
    if scenario == 0:
        messageProbList[RL.goodWeatherResponse] = messageProbability(message, RL.goodWeather)
        messageProbList[RL.badWeatherResponse] = messageProbability(message, RL.badWeather)
        messageProbList[RL.outsideResponse] = messageProbability(message, RL.outside)
        messageProbList[RL.insideResponse] = messageProbability(message, RL.inside)
        messageProbList[RL.thanksResponse] = messageProbability(message, RL.thanks)
    elif scenario == 1:
        messageProbList[RL.cookingResponse] = messageProbability(message, RL.cooking)
        messageProbList[RL.restaurantResponse] = messageProbability(message, RL.restaurant)
        messageProbList[RL.earlyResponse] = messageProbability(message, RL.early)
        messageProbList[RL.sameTimeResponse] = messageProbability(message, RL.sameTime)
        messageProbList[RL.lateResponse] = messageProbability(message, RL.late)
        messageProbList[RL.activityResponse] = messageProbability(message, RL.activity)
        messageProbList[RL.agreementResponse] = messageProbability(message, RL.agreement)
    else:
        messageProbList[RL.otherCountResponse] = messageProbability(message, RL.otherCount)
        messageProbList[RL.sameCountResponse] = messageProbability(message, RL.sameCount)
        messageProbList[RL.beenLongBeforeResponse] = messageProbability(message, RL.beenLongBefore)
        messageProbList[RL.beenRecentlyResponse] = messageProbability(message, RL.beenRecently)
        messageProbList[RL.plansResponse] = messageProbability(message, RL.plans)
        messageProbList[RL.agreeResponse] = messageProbability(message, RL.agree)
    messageProbList[RL.byeResponse[random.randrange(3)]] = messageProbability(message, RL.bye)
    messageProbList[RL.errorMessageResponse[random.randrange(3)]] = messageProbability(isErrorMessage=True)


# returns the child response that has the highest probability of being prompted by the parent message
def bestAnswer(message):
    messageMap(randScenario, message)
    return max(messageProbList, key=messageProbList.get)

# take parent message and find the best child response
def getResponse(parentInput):
    # parse parent input using common punctuation and blank space
    parseResponse = re.split(r'[-!?;/.,\s]\s*', parentInput.lower())
    response = bestAnswer(parseResponse)
    return response

# text at 4pm (16:00 military time)
alarmHour = 16
alarmMin = 0
alarmSec = 0

# keep program running
while True:
    #if it is 4pm send the text
    if alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute and \
           alarmSec == datetime.datetime.now().second:
        # 0=weather, 1=cooking, 2=travel
        randScenario = random.randrange(3)

        # create map for possible responses and their probabilities
        messageProbList = {}

        # send initial question from child
        if randScenario == 0:
            print('Child: Hey, how is the weather where you are?')
        elif randScenario == 1:
            print('Child: Hi, what are you planning on cooking for dinner?')
        else:
            print('Child: Hello, are you going to travel to another continent soon? If so, which one?')

        talk = True
        while talk:
            childResponse = getResponse(input('Parent: '))
            print('Child: ' + childResponse)
            # end conversation after child says bye
            if childResponse == "Talk to you later." or childResponse == "Bye. Love you!" or childResponse == "Take care!":
                talk = False
                print('-----------------------------------------------------------------------------------------------')
