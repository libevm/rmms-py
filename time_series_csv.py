'''
Generate sample price actions following a given process
'''

from configparser import ConfigParser
import matplotlib.pyplot as plt
import numpy as np
import json, codecs

import math

def generateGBM(T, mu, sigma, S0, dt):
    '''
    Generate a geometric brownian motion time series. Shamelessly copy pasted from here: https://stackoverflow.com/a/13203189

    Params: 

    T: time horizon 
    mu: drift
    sigma: percentage volatility
    S0: initial price
    dt: size of time steps

    Returns: 

    t: time array
    S: time series
    '''
    N = round(T/dt)
    t = np.linspace(0, T, N)
    W = np.random.standard_normal(size = N) 
    W = np.cumsum(W)*np.sqrt(dt) ### standard brownian motion ###
    X = (mu-0.5*sigma**2)*t + sigma*W 
    S = S0*np.exp(X) ### geometric brownian motion ###
    S = S.tolist()
    t = t.tolist()
    json.dump(S, codecs.open('./dump.json', 'w', encoding='utf-8'), indent=4) 
    json.dump(t, codecs.open('./timestep_dump.json', 'w', encoding='utf-8'), indent=4) 
    return t, S

# T = 365
# mu = 0.00005
# sigma = 0.05
# S0 = 2700
# dt = 1
# t, S = generateGBM(T, mu, sigma, S0, dt)
# plt.plot(t, S)
# plt.show()

