# -*- coding:utf-8 -*-

import numpy as np

def comp_pi(n_shots):
    """Compute π with Monte-Carlo, n_shots are used"""
    rand_shots = np.random.random_sample((2, n_shots))
    x, y = rand_shots[0], rand_shots[1]
    n_ins = np.sum(np.sqrt(x*x + y*y) < 1)
    pi = 4*n_ins/(n_shots)
    return pi

if __name__ == '__main__':
    pi = comp_pi(10**7)
