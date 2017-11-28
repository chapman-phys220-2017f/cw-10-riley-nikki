#!/usr/bin/env python3
# Name: Riley Kendall and Nikki Schwartz
# Student ID: 2274503
# Email: kenda106@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CLASSWORK 10
import randomwalk
import numpy as np

#estimating the value of e
def estimate_e(N=100000):
        '''estimate_e(N)
    Estimating the value of 'e' using np.random
        N(int) : N amount of random x and y coordinents
    Returns:
        np.exp(xs).sum()/N +1 (int) : The estimated numeric value for e'''
    xs = np.random.uniform(0,1,N)
    return np.exp(xs).sum()/N +1