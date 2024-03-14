# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 21:00:17 2022

@author: rober
"""

def confirma(pergunta,tentativas=3,reclamacao='Sim ou não por favor:'):
    while True:
        x=input(pergunta).lower()
        if x in ('s','sim'):
            return True
        elif x in ('n','não','nao'):
            return False
        tentativas-=1
        if tentativas ==0:
            print('O usuário não quer colaborar!')
            exit()
        print(reclamacao)
    
if confirma(pergunta='Continua? <s/n>', reclamacao='s ou n por favor!', tentativas=5):
    print("Respondeu sim!")
else:
    print("Respondeu não!")


input()
