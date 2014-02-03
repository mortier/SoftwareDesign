# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 17:29:01 2014

@author: dmichael
"""
cross= "+ - - - - + - - - - "
line=  "|         |         "

print cross + ('\n' +line+"|")*4 + '\n'+cross+'+' + ('\n' +line+"|")*4 + '\n'+cross+'+'

print (2*((2*cross +"+"+ ('\n' +2*line+"|")*4)+'\n'))*2 + 2*cross+'+'