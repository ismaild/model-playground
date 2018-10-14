'''
Simulates chaos, which is sensative Dependance on initial conditions. 
We conduct two runs with a small variance in the initial population. 
Systems that exhibit this behaviour are considered chaotic. This is because it is 
practically impossible to predict values of Xt
'''
from logisticmap import logisticMap

logisticMap(0,.2,4,50)

logisticMap(0,.2000010,4,50)

