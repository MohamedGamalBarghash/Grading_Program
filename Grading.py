# Define Dictionaries to hold my Answers
myAnswers = dict()
answers = dict()
wrongAnswers = dict()

# Define variables to hold my score
rightCount = 0
wrongCount = 0

# Open the files to my answers and the right answers and fill the dictionaries
with open("MyAnswers.txt") as myAns:
    for line in myAns:
        myAnswers[int(line.split('-')[0])] = line.strip().split('-')[1]
with open("Answers.txt") as myAns:
    for line in myAns:
        answers[int(line.split('-')[0])] = line.strip().split('-')[1]

# Check for right and wrong answers
for ans in myAnswers:
    if myAnswers[ans] == answers[ans]:
        rightCount+=1
    else:
        wrongCount+=1
        wrongAnswers[ans] = myAnswers[ans]

# Assign the total number of questions
totalCount = rightCount+wrongCount

# Print my score and the answers I did wrong
print ("I got: {} right answers, and {} wrong answers, out of {}".format(rightCount, wrongCount, totalCount))
for wrongAns in wrongAnswers:
    print ("I was wrong in no.: {}, my Ans: {}, right Ans: {}".format(wrongAns, wrongAnswers[wrongAns], answers[wrongAns]))
