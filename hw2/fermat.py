# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 17:55:43 2014

@author: dmichael
"""

def check_fermat(a,b,c,n):
    if a**n + b**n == c**n:
        print "Holy smokes. Fermat was wrong!"
    else:
        print "No, That doesnt work."

def fermat_values(a,b,c,n):
    check_fermat(int(a),int(b),int(c), int(n))