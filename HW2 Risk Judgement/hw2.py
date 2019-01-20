#!/usr/local/anaconda/bin/python
######################################################################
# Thomas Buffard
# A05
######################################################################

# I certify that the entirety of this file contains only my own
# work. I also certify that I have not shared the contents of this
# file with anyone in any form.

######################################################################
# Replace "hawkid" in the singleton tuple in the function below with
# your own hawkid USING LOWER CASE CHARACTERS ONLY.
#
# ATTENTION: Your hawkid is your login name for ICON, it is not
# your student ID number. 
#
# Failure to correctly do so will result in a 0 grade.
######################################################################
def hawkid():
    return(("buffard",))

######################################################################
import csv
import matplotlib.pyplot as plt
from random import randint

# Fields from the input file, in same order as they appear in the file
# (ignoring respondent ID). Do not modify or change.
fields=['result','smoke','drink','gamble','skydive','speed','cheat','steak','cook','gender','age','income','education','location']
# Corresponding field values from the input file. Do not modify or change.
values=[('lottery a','lottery b'),('no','yes'),('no','yes'),('no','yes'),('no','yes'),('no','yes'),('no','yes'),('no','yes'),
        ('rare','medium rare','medium','medium well','well'),('male','female'),
        ('18-29','30-44','45-60','> 60'),
        ('$0 - $24,999','$25,000 - $49,999','$50,000 - $99,999','$100,000 - $149,999','$150,000+'),
        ('less than high school degree','high school degree','some college or associate degree','bachelor degree','graduate degree'),
        ('east north central','east south central','middle atlantic','mountain','new england','pacific',
         'south atlantic','west north central','west south central')]

######################################################################
# readData() returns a list where each element is a dictionary of each survey response.
def readData(filename='steak-risk-survey.csv', fields=fields, values=values):
    import re
    l = []

    # splitFields() is a helper function that takes a line and returnsa dictionary
    # of each field as a key and the persons response.
    def splitFields(line):
        responses = {}
        for i in range(len(fields)):
            # Checks if the response is valid. [i+1] is used because values are offset
            # 1 by the userid
            if line[i+1].lower() in values[i]:
                # Add the response to its corresponding key.
                responses[fields[i]] = line[i+1].lower()
        return(responses)

    with open(filename) as csvfile:
        # Grabs each line as a list of its elements, seperated by a comma in the CSV file.
        for line in csv.reader(csvfile, delimiter = ','):
            # Checks if the line is a survey response by looking for an id at the
            # beginning and checks if the line is useful by making sure it has
            # a response to the lottery question.
            if re.match('(^[0-9]+?)', line[0]) and line[1].lower() in values[0]:
                # Call on the helper function above to convert the list of elements
                # into a more comprehensible dictionary.
                l.append(splitFields(line))

        csvfile.close()
    return(l)

######################################################################
# showPlot() plots a chart displaying lottery preferences based on a specified
# field and its values.
def showPlot(D, field, values):
    import numpy as np
    # Compile a list of every response that includes a value for the field to be
    # plotted. This is helpful for easily determining the total respondants.
    responses = [ resp for resp in D if field in resp.keys() ]
    
    lottoA = { value:0 for value in values }
    lottoB = { value:0 for value in values }

    # Iterate through each survey response and count the amount of people who
    # responded to each lottery.
    for resp in responses:
        if resp['result'] == 'lottery a':
            lottoA[resp[field]] += 1
        elif resp['result'] == 'lottery b':
            lottoB[resp[field]] += 1

    # Divide the total amount of respondants for each value by the grand total
    # to get the % by iterating through each key.
    for key in lottoA.keys():
        lottoA[key] = lottoA[key]/len(responses)
    for key in lottoB.keys():
        lottoB[key] = lottoB[key]/len(responses)

    # Plot the graph.
    fig, ax = plt.subplots()
    index = np.arange(len(values))
    bar_width = 0.35
    opacity = 0.8
    
    rects1 = plt.bar(index, lottoA.values(), bar_width,
                 alpha=opacity,
                 color='b',
                 label='Lottery A')
 
    rects2 = plt.bar(index + bar_width, lottoB.values(), bar_width,
                     alpha=opacity,
                     color='r',
                     label='Lottery B')

    plt.xlabel('Value')
    plt.ylabel('Percentage of population')
    plt.title('Lottery preference by ' + field)
    plt.xticks(index + bar_width, values)
    plt.legend()

    plt.tight_layout()
    plt.show()
    
######################################################################
# train() trains a Naive Bayes classifier to predit lottery preference. It takes a
# data set and gives the population percentages for each response value in each field.
def train(D, fields=fields, values=values):
    # Set up the framework for the function. This dictionary comprehension sets up
    # three nested dictionaries. The outer dictionary's keys are all the fields
    # and the values are a dictionary with each lottery as a key and a list of
    # possible responses (values) for the field as the value.
    P = { f:{'lottery a':{ v:0 for v in values[fields.index(f)] },
          'lottery b':{ v:0 for v in values[fields.index(f)] }}
          for f in fields[1:] }

    # Result is added outside of the comprehension because it has only one nested
    # dictionary.
    P['result']={'lottery a':0, 'lottery b':0}

    # Count the amount of responses for each possible value of each field.
    for resp in D:
        for field in resp:
            # The result field is still an exception since it only goes one
            # dictionary deep.
            if field == 'result':
                P[field][resp['result']] += 1
            else:
                P[field][resp['result']][resp[field]] += 1

    # Iterate through and add up the total amount of responses for each fields'
    # lottery pick and then divide the single amounts by the total to get the
    # final percentages. 'f' is the field. 'k' is one of the lottery choices.
    # 'r' is a value of that field.
    for f in P:
        total = 0
        # Exception for the result field.
        if f == 'result':
            # Add up the total for both lotteries.
            for r in P[f]:
                total += P[f][r]
            # Calculate the percentage of each lottery by dividing it by the total.
            for r in P[f]:
                P[f][r] = P[f][r] / total
            continue
        # Iterate through each lottery choice in the field.
        for k in P[f]:
            total = 0
            # Add up the total of the values of the field for that lottery.
            for r in P[f][k]:
                total += P[f][k][r]
            # Divide each values' total by the field's lottery grand total.
            for r in P[f][k]:
                P[f][k][r] = P[f][k][r] / total

    return(P)

######################################################################
# predict() predicts whether someone will choose lottery A or B based on
# their responses 'example' and a trained set of data 'P'.
def predict(example, P, fields=fields, values=values):
    # Set up the dictionary that will contain the probability of choosing
    # each lotto.
    prediction = {'lottery a': P['result']['lottery a'],
                  'lottery b': P['result']['lottery b']}

    # Loop through both lottery choices and find the population percentage
    # for each field in the trained data set P.
    for lotto in values[0]:
        for field in example:
            # Ignore the result field.
            if field == 'result':
                continue
            else:
                # Multiply the current prediction value with the value of the
                # example's respon to the field in the respective lottery 
                prediction[lotto] = prediction[lotto] * P[field][lotto][example[field]]

    # The bigger value is the more likely, so return that value.
    if prediction['lottery a'] >= prediction['lottery b']:
        return('lottery a')
    else:
        return('lottery b') 

######################################################################
# Predict by guessing. You're going to be about half right!
def guess(example, fields=fields, values=values):
    return(values[0][randint(0,1)]==example['result'])

######################################################################
# test() takes a data set 'D' and a trained set of values 'P' and compares
# the predicted result of the response with the actual result.
def test(D, P, fields=fields, values=values):
    right = 0

    # Iterate through all the survey reponses.
    for resp in D:
        # Predict what the value will be.
        prediction = predict(resp, P, fields, values)
        # If the predicted result is the same as the actual result, count it right.
        if prediction == resp['result']:
            right += 1

    # Return the amount of right predictions / amount of predictions
    # to get a success rate.
    return(right/len(D))

######################################################################
# Fisher-Yates-Knuth fair shuffle, modified to only shuffle the last k
# elements. S[-k:] will then be the test set and S[:-k] will be the
# training set.
def shuffle(D, k):
    # Work backwards, randomly selecting an element from the head of
    # the list and swapping it into the tail location. We don't care
    # about the ordering of the training examples (first len(D)-N),
    # just the random selection of the test examples (last N).
    i = len(D)-1
    while i >= len(D)-k:
        j = randint(0, i)
        D[i], D[j] = D[j], D[i]
        i = i-1
    return(D)

# Evaluate.
def evaluate(filename='steak-risk-survey.csv', fields=fields, values=values, trials=100):
    # Read in the data.
    D = readData(filename, fields, values)
    # Establish size of test set (10% of total examples available).
    N = len(D)//10
    result = 0
    random = 0
    for i in range(trials):
        # Shuffle to randomly select N test examples.
        D = shuffle(D, N)
        # Train the system on first 90% of the examples.
        P = train(D[:-N], fields=fields, values=values)
        # Test on last 10% of examples, chosen at random by shuffle().
        result += test(D[-N:], P, fields=fields, values=values)
        # How well would you do guessing at random?
        random += sum([ len([ True for x in D[-N:] if guess(x)])/N ])
    # Return average accuracy.
    print('NaiveBayes={}, random guessing={}'.format(result/trials, random/trials))


