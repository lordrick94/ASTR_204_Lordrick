import numpy as np
import matplotlib.pyplot as plt
import time
import math
import rebound as rb

units_dic = {'length': 'AU', 
             'time': 'yr',
             'mass': 'Msun'}

sim = rb.Simulation()

sim.units = units_dic
G = sim.G

M_star = 1. # Msun
star = rb.Particle(simulation=sim, m=M_star, x=0., y=0., z=0.)
sim.add(star)


tpr = 1.0 # AU
tp_v0 = np.sqrt(G*M_star/tpr)
test_part = rb.Particle(simulation=sim, x=tpr, y=0., z=0., 
                        vx=0, vy=tp_v0, vz=0)
sim.add(test_part)