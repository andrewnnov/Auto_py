import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidely so'
    elif answerNumber == 3:
        return 'Yes'
r = random.randint(1, 3)
fortune = getAnswer(r)
print(fortune)

print(getAnswer(random.randint(1,3)))
