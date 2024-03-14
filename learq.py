# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 22:12:20 2022

@author: rober
"""

arq=open('dados.txt')
for linha in arq:
    print (linha.rstrip())