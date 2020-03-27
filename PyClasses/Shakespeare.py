# A mini script to generate a Shakespearean string

import random


def generateOne(stringlength):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    result = ''
    for i in range(stringlength):
        result = result + alphabet[random.randrange(27)]
    return result


def score(goal, teststring):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numSame += 1
    return numSame / len(goal)


def main():
    goal_string = 'methinks it is like a weasel'
    newstring = generateOne(28)
    best_score = 0
    best_string = ''
    best_iteration = ''
    newscore = score(goal_string, newstring)
    iteration = 0
    iteration_status_threshold = 100000
    while newscore < 1:
        if newscore > best_score:
            #print(newscore, newstring)
            best_score = newscore
            best_string = newstring
            best_iteration = iteration
        if iteration % iteration_status_threshold == 0 and iteration > 0:
            print(
                f'Iteration status {iteration}: "{best_string}" scored {round(100*best_score,1)} % similarity at iteration: {best_iteration}')
        newstring = generateOne(28)
        newscore = score(goal_string, newstring)
        iteration += 1


main()
