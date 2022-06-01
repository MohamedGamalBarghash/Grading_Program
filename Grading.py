import argparse
# Create a parser to take input as extra arguments from the terminal
parser = argparse.ArgumentParser(description="Input files names.")
parser.add_argument('MyAnswersFile', help='the my answers file name and extension')
parser.add_argument('AnswersFile', help='the right answers file name and extension')

args = parser.parse_args()

# Open the files to my answers and the right answers and fill the dictionaries
def Read_Files (fileName, theDict):
    with open(fileName) as myAns:
        for line in myAns:
            theDict[int(line.split('-')[0])] = line.strip().split('-')[1]

# Define Dictionaries to hold my Answers
myAnswers = dict()
answers = dict()
wrongAnswers = dict()

# Define variables to hold my score
rightCount = 0
wrongCount = 0

# Read the files with inputs from terminal
Read_Files(args.MyAnswersFile, myAnswers)
Read_Files(args.AnswersFile, answers)

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
