'''
Logistic Map 
Used to model non-linear dynamical systems. 
https://en.wikipedia.org/wiki/Logistic_map

Xt+1 = R(Xt-Xt^2)
R=Growth Rate
t=timestep
Xt=Population at Time (t)
Xt=Nt/K
K=Carrying Capacity 
'''

def logisticMap(timestep=0,population=.2, growthrate=2, maxtimestep=10):
  if timestep==0:
    print("-"*10)
    print("Growth Rate: {0}, Timesteps: {1}".format(growthrate, maxtimestep))
  if timestep == maxtimestep:
    return 0
  else:
    print("Timestep: {0}, Population: {1}".format(timestep, population))
    population = growthrate*(population-(population*population))
    return logisticMap(timestep+1,population, growthrate, maxtimestep)
    