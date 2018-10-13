import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    count_matches = 0
    n = 0
    while n < numTrials:
        urn = ['R','R','R','G','G','G']
        ball_set = set()
        n += 1
        for x in range(3):
            ball = random.choice(urn)
            urn.pop(urn.index(ball))
            ball_set.add(ball)
        if len(ball_set) == 1:
            count_matches += 1
        print 'trials:', n, 'set:', ball_set, 'urn:', urn, '# All balls the same:', count_matches
return count_matches/float(numTrials)
