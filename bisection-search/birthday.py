'''
Bisection Search
'''
def collision_prob(numIndices, numInsertions):
    '''
    Given the number of buckets and the number of items to insert, 
    calculates the probability of a collision.
    '''
    prob = 1.0
    for i in range(1, numInsertions):
        prob = prob * ((numIndices - i) / float(numIndices))
    return 1 - prob

x = 0.99
epsilon = 0.001
low = 0
high = 365
mid = int((high + low)/2)
while abs(collision_prob(365, mid) - x) >= epsilon:
    print 'low = ' + str(low) + ' high = ' + str(high) + ' mid = ' + str(mid) +  ' prob = ' + str(collision_prob(365, mid))
    if collision_prob(365, mid)  < x:
        low = mid
    else:
        high = mid
    mid = int((high + low)/2)
if collision_prob(365, mid) > x:
    mid -= 1
print str(mid) + ' is the smallest class where there is a probability of less than ' + str(x)
print "The probability is", collision_prob(365, mid)
