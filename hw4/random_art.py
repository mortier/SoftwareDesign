# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image
from math import *


def build_random_function(min_depth, max_depth):
    # your doc string goes here
    """ creates a sudorandom function of a deapth between the min and max which you imput as an int"""
    # your code goes here
    baselist = [['x'],['y']]    
    if max_depth <= 1:
        rand_func = baselist[randint(0,1)]
        return rand_func

    x = build_random_function(min_depth-1, max_depth-1)
    y = build_random_function(min_depth-1, max_depth-1)
    
    functions = [['x'],['y'],['sin_pi',x],['cos_pi',x], ['prod', x, y]]
    if min_depth > 1:
        rand_func = functions[randint(2,4)]
        return rand_func
    elif min_depth <= 1:
        rand_func = functions[randint(0,4)]
        return rand_func

#print build_random_function(2,5)

def evaluate_random_function(f, x, y):
    # your doc string goes here
    '''this recursivly looks at the first element in a given list and evaluates down to the base x and or y'''
    # your code goes here
       
    if f[0] == 'prod':
        return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)
    if f[0] == 'cos_pi':
        return cos(pi*evaluate_random_function(f[1],x,y))
    if f[0] == 'sin_pi':
        return sin(pi*evaluate_random_function(f[1],x,y))
    if f[0] == 'x':
        return x
    if f[0] == 'y':
        return y
    
#print evaluate_random_function(['cos_pi', ['prod', ['sin_pi', ['x']], ['sin_pi', ['sin_pi', ['x']]]]], 0.3,0.4)
def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
               (b-a)(x-min)
        f(x) = ------------ + a
                 min-max
    """
    # your code goes here
    out_inter = output_interval_end - output_interval_start
    out_inter = float(out_inter)
    in_inter = input_interval_end - input_interval_start
    out_val = ((out_inter*(val-input_interval_start))/in_inter) + output_interval_start
    return out_val
    
#print remap_interval(75,50,100,0,1)

def random_art():
    ''' this takes no inputs and creats a sudorandomly genarated image'''
    im = Image.new("RGB",(350,350))
    pixel = im.load()    
    r = build_random_function(10,13)
    g = build_random_function(7,9)
    b = build_random_function(7,10)
    for x in range(350):
        xremap = remap_interval(x,0,349,-1,1)
        for y in range(350):
            yremap = remap_interval(y,0,349,-1,1)
            red = evaluate_random_function(r,xremap,yremap)
            green = evaluate_random_function(g,xremap,yremap)
            blue = evaluate_random_function(b,xremap,yremap)
            redcolor = remap_interval(red,-1,1,0,255)
            greencolor = remap_interval(green,-1,1,0,255)
            bluecolor = remap_interval(blue,-1,1,0,255)
            pixel[x,y] = (int(redcolor),int(greencolor),int(bluecolor))    
    im.show()            

random_art()
    
    
    