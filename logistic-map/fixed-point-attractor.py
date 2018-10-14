'''
Simulates a system with a fixed point attractor. The Population starts of at 20% of carrying capacity, 
with a growth rate of 2.The system will reach homeostasis/equilibrium at the fixed point attractor
Different values of R, have different fixed points. Irrespective of the starting point, 
the fixed point will always be reached.
'''
from logisticmap import logisticMap

logisticMap(0,.2,2,10)

logisticMap(0,.9,2,10)

logisticMap(0,0.01,2,15)

logisticMap(0,0.9,2,10)

logisticMap(0,0.2,2.8,30)