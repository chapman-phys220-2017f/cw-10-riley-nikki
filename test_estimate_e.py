#!/usr/bin/env python3
# Name: Riley Kendall and Nikki Schwartz
# Student ID: 2274503
# Email: kenda106@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: CLASSWORK 10
import numpy as np #numeric python
import estimate_e #estimates the value of e
import randomwalk #codes for particle movement
import nose #nosetests3

def test_estimate_e():
    """test_estimate_e():
    enables 'e' numeric value to be estimated using np.random and tested for accuracy"""
    correct = np.e
    estimate = estimate_e.estimate_e(N=100000)
    np.testing.assert_almost_equal(correct, estimate,0.0001)