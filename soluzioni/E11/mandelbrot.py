
#########################################################################################
# S. Germani (stefano.germani@unipg.it)                                                 #
#                                                                                       #
# Universià degli Studi di Perugia                                                      #
# Corso di Metodi Computazionali per la Fisica                                          #
#---------------------------------------------------------------------------------------#
# Esercitazione  11 - Compilazione JIT con Numba:                                       #
#                                                                                       #
#   Definizione di un set di funzioni che calcolano gli insiemi di Madelbrot:           #
#    - con puro codice Python                                                           #
#    - con compilazione Just in Time Numba                                              #
#    - Multibrot con compilazione JIT Numba                                             #
#    Il risultato viene visualizzato garficamente                                       #
#                                                                                       #
#Derivato da C. Rossant (IPython Cookbook - https://ipython-books.github.io/):          #
#  Accelerating pure Python code with Numba and just-in-time compilation                #
#  https://ipython-books.github.io/\                                                    #
#    52-accelerating-pure-python-code-with-numba-and-just-in-time-compilation           #
#                                                                                       #
#########################################################################################

import numpy as np
import matplotlib.pyplot as plt
import time

from numba import jit

import argparse



#########################################################################################
#               Funzione per gestione opzioni (argparse)                                #
#########################################################################################

def parse_arguments():

    parser = argparse.ArgumentParser(description='Calcolo insiemi di Mandelbrot.',
                                     usage      ='python3 mandelbrot.py  --option1 --option2 ...')
    parser.add_argument('-s', '--size',         action='store',  default=500,  type=int,   help='Size')
    parser.add_argument('-it', '--iterations',  action='store',  default=100,  type=int,   help='Iterazioni')
    parser.add_argument('-m',  '--multi',       action='store',  default=2,    type=int,   help='Multibroth Power (JIT only)')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(        '--py',          action='store_true',                       help='Calcolo con puro codice Python')
    group.add_argument(        '--jit',         action='store_true',                       help='Calcolo con Numba JIT')
    
    return  parser.parse_args()





def mandelbrot_python(size, iterations):
    """Pure Python Mandelbrot set calculation.
    
    Parameters:
        size : 
            Image size (numbero of values to evaluate is size*size)

        iterations : 
            Numer of terations for each value
    """
    
    m = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            c = (-2 + 3. / size * j +
                 1j * (1.5 - 3. / size * i))
            z = 0
            for n in range(iterations):
                if np.abs(z) <= 10:
                    z = z * z + c
                    m[i, j] = n
                else:
                    break
    return m


@jit(nopython=True, cache=True)
def mandelbrot_numba(size, iterations):
    """Mandelbrot set calculation with Numba JIT.
    
    Parameters:
        size : 
            Image size (numbero of values to evaluate is size*size)

        iterations : 
            Numer of terations for each value
    """

    m = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            c = (-2 + 3. / size * j +
                 1j * (1.5 - 3. / size * i))
            z = 0
            for n in range(iterations):
                if np.abs(z) <= 10:
                    z = z * z + c
                    m[i, j] = n
                else:
                    break
    return m


@jit(nopython=True, cache=True)
def multibrot_numba(size, iterations, mb=2):
    """Multibrot set calculation with Numba JIT.
    
    Parameters:
        size : 
            Image size (numbero of values to evaluate is size*size)

        iterations : 
            Numer of terations for each value
       
        mb :
           exponent used to compute new value at each iteration
           z = z^mb + c  (default is mb=2)
    """

    m = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            c = (-2 + 3. / size * j +
                 1j * (1.5 - 3. / size * i))
            z = 0
            for n in range(iterations):
                if np.abs(z) <= 10:
                    z = z**mb + c
                    m[i, j] = n
                else:
                    break
    return m



def mandelbrot():
    """
    Main function

    """
    

    args = parse_arguments()


    m = None
    
    if args.py == True:
        tstart_py = time.time()

        m = mandelbrot_python(args.size, args.iterations)

        tstop_py  = time.time()


        dt_py = tstop_py - tstart_py
        print('dt_py', dt_py)
        



    if args.jit == True:
        #mandelbrot_numba(1, 1)

        tstart_numba = time.time()

        if args.multi == 2:
            m = mandelbrot_numba(args.size, args.iterations)
        else:
            m = multibrot_numba(args.size, args.iterations, args.multi)
            
        tstop_numba = time.time()
        dt_numba = tstop_numba - tstart_numba
        print('dt_numba', dt_numba)
        


    if not np.isscalar(m):
        fig, ax = plt.subplots(1, 1, figsize=(10, 10))
        ax.imshow(np.log(m), cmap=plt.cm.hot)
        ax.set_axis_off()
        plt.show()

        

if __name__ == "__main__":

    mandelbrot()


