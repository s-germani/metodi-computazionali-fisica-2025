#####################################################
# S. Germani (stefano.germani@unipg.it)             #
#                                                   #
# Universià degli Studi di Perugia                  #
# Corso di Metodi Computazionali per la Fisica      #
#---------------------------------------------------#
# Esercitazione  11 - C e Python:                   #
#                                                   #
#   Script che esegue i moduly sviluppati           #
#    per il calcolo della successione di Fibonacci  #
#    - serie   : basato sulla libreria libserie.so  #
#    - serie_py: basato  su puro codice python      #
#####################################################

import numpy as np
import serie_py
import serie

import time

import argparse


#####################################################################
#      Funzione per gestione opzioni (argparse)                     #
#####################################################################

def parse_arguments():

    parser = argparse.ArgumentParser(description='Esecuzione moduli per calcolo serie di Fibonacci.',
                                     usage      ='python3 run_serie.py  --option')
    parser.add_argument('--n',   action='store',         type=int,   required=True, help='Numero fino a cui calcolare la serie')
    parser.add_argument('--c',   action='store_true',                          help='Calcolo con modulo che utilizza libreria C')
    parser.add_argument('--py',  action='store_true',                          help='Calcolo con puro modulo Python')

    
    return  parser.parse_args()




def run_serie():


    args = parse_arguments()

    
    #### uso serie da libreria C libserie.so ####
    if args.c:

        print('----------  C  ---------------')
        start_time1 = time.time()

        print(serie.fibonacci(args.n))

        stop_time1 = time.time()

        print('>>>> {:} s'.format( stop_time1 - start_time1 ))


    #### uso serie da modulo python serie_py  #####
    if args.py:

        print('----------  Python  ----------')
        start_time2 = time.time()
        print(serie_py.fibonacci(args.n))
        
        stop_time2 = time.time()

        print('>>>> {:}'.format( stop_time2 - start_time2 ))



if __name__ == "__main__":

    run_serie()
