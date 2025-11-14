#####################################################
# S. Germani (stefano.germani@unipg.it)             #
#                                                   #
# Universià degli Studi di Perugia                  #
# Corso di Metodi Computazionali per la Fisica      #
#---------------------------------------------------#
# Esercitazione 6 - Integrazione e Derivazione:     #
#                                                   #
#   Distanza percorsa da velocità                   #
#                                                   #
#####################################################



import sys,os
import numpy as np
import pandas as pd

from scipy import integrate

import matplotlib.pyplot as plt

import argparse

##---------------------------------------------

def parse_arguments():
    parser = argparse.ArgumentParser(description='Calcolo distanza percorsa da velocità.')
    parser.add_argument('-f',  '--file',    action='store',      default='vel_vs_time.csv', help='File di input')
    parser.add_argument('-v',  '--vel',     action='store_true',                            help='Grafico Velocità vs Tempo')
    parser.add_argument('-d',  '--dist',    action='store_true',                            help='Grafico Distanza Totale'  )
    parser.add_argument('-dt', '--dvst',    action='store_true',                            help='Grafico Distanza vs Tempo')
    return  parser.parse_args()



##---------------------------------------------

def distanza():


    args = parse_arguments()

    print(args)
    
    # Lettura file 
    veldf = pd.read_csv(args.file)

    # Colonne Data Frame
    print('Colonne File:', veldf.columns)

    # Vel vs t
    if args.vel == True:

        ## grafico velocità vs tempo
        plt.plot(veldf['t'], veldf['v'])
        plt.xlabel('tempo [s]')
        plt.ylabel('velocità [m/s]')
        plt.show()


        
    # Distanza Totale 
    if args.dist == True:
        # Integrale distanza totale
        dist = integrate.simpson(veldf['v'].values,   dx=0.5)
        print('Distanza Totale Percorsa: {:}'.format(dist))
              

    # Distanza vs tempo
    if args.dvst == True:

        # Array distanze da cilco for con list comprehention
        dists = np.array( [ integrate.simpson(veldf['v'][:iv],   dx=0.5) for iv in range(1, len(veldf['v'])+1) ] )

        ## grafico distanza vs tempo
        plt.plot(veldf['t'], dists)
        plt.xlabel('tempo [s]')
        plt.ylabel('distanza percorsa [m]')
        plt.show()




###########################################################################

if __name__ == "__main__":

    distanza()

