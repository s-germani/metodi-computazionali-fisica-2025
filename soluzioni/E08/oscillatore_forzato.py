############################################################################
# S. Germani (stefano.germani@unipg.it)                                    #
#                                                                          #
# Universià degli Studi di Perugia                                         #
# Corso di Metodi Computazionali per la Fisica                             #
#--------------------------------------------------------------------------#
# Esercitazione 8 - Equazioni Dfferenziali:                                #
#                                                                          #
#   Oscillatore forzato                                                    #
#                                                                          #
############################################################################

import numpy as np
from scipy import integrate, constants
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import argparse



############################################################################
#      Funzione per Equazione Differenziale Oscillatore  Forzato           #
############################################################################

def drdt_molla(r, t, k, m, C,  F, pf, A0):
    """
    drdt_molla(r, t, gamma, omega0, m, F, parf) derivate per equazine differenziale del moto oscillante attenuato di una molla 
    r : vettore con variabili r(x,dx/dt)
    t : variabile tempo
    k : costante eleastica molla
    m : massa molla
    C : costante di attenuazione 
    F : funzione per definzione forza F(t) 
    pf: parametro della funzione F(t) 
    A0: parameteo ampiezza oscillazione Forza 
    -------------------------------------------------------
    Equazione differenziale:
    d^2/dx^2 +2 gamma omega0 dx/dt +omega0^2 x -F(t)/m = 0

    gamma = C/(2*m)
    omega0 = k/m
    """
    
    gamma = C/(2*m)
    omega0 = k/m
    
    dxdt = r[1]
    dydt = -2 * gamma * r[1] - omega0**2 *r[0] + F(t, pf, A0)/m
    return (dxdt, dydt)




############################################################################
#    Funzioni  Forza  F(t)                                                #  
############################################################################

def fsin(t, o, A0):
    """
    Funzione Forza sinusoidale
    fsin(t, o)
    
    return: A0*sin(o*t)
    """
    return A0*np.sin(o*t)



### ------------------------------------------------
def fsin2(t, o, A0):
    """
    Funzione Forza con due componenti sinusoidali
    fsin2(t, o)
    
    return: A0*sin(o*t) + 2*A0*sin(3*o*t)
    """

    return A0*np.sin(o*t) + 2*A0*np.sin(3*o*t)



### ------------------------------------------------
def fimpulse(t, tau, A0):
    """
    Funzione Forza con singolo impulso
    fimpulse(t, tau)
    
    return: A0*(t/tau)^2 *e^(-t/tau)
    """
    
    return A0*(t/tau)**2 *np.exp(-t/tau)




#########################################################################################
# Funzione per definizione opzioni (argparse)                                          #
#########################################################################################
def parse_arguments():

    parser = argparse.ArgumentParser(description='Soluzione equazione differenziale per oscillatore forzato.',
                                     usage      ='python3 oscillatore_forzato.py  --opzione [--par val]'                              )
    parser.add_argument('--sin',     action='store_true',                         help='Risultati per Forza sinusoidale'                       )
    parser.add_argument('--sin2',    action='store_true',                         help='Risultati per Forza con due componenti sinusoidali'    )
    parser.add_argument('--impulse', action='store_true',                         help='Risultati per Forza con singolo impulso'               )
    parser.add_argument('--A0',      action='store',    default=2.0, type=float,  help='Parametro per ampiezza Forza (opzionale - default=2.0)')
    parser.add_argument('--par',     action='store',    default=1.0, type=float,  help='Parametro per funzione Forza (opzionale - default=1.0)')
    
    return  parser.parse_args()




############################################################################
#    Funzione principale  per oscillatore forzato                          #  
############################################################################

def oscliialtore_forzato():

    # Parser 
    args = parse_arguments()

    
    # Array Tempi 
    dt = 0.01 # s
    otimes = np.arange(0, 60, dt)

    #Assegno funzione Forza sulla base dell'opzione specificata
    F = None
    if args.sin:
        F = fsin
    elif args.sin2:
        F = fsin2
    elif args.impulse:
        F = fimpulse
    else:
        print('Nessuna opzione specificata per F(t)')
        print('usare opzione --help per maggiori info')
        return


    # Ampiezza Forza
    A0 = args.A0

    # Condizioni iniziali
    x0  = 0
    v0  = 0
    oinit = (x0, v0)



    # Costanti dell'equazione
    m_molla  = 0.5 # kg
    k_molla  = 2  # N/m
    c_visc   = 0.4  # N s/m


    #--------------------------------------------------------------------------------#
    #               grafico in funzopne dle tempo                                    #
    #--------------------------------------------------------------------------------#

    # parametro forza per grafico in funzopne dle tempo
    fpar = args.par

    # Soluzioni
    sol  = integrate.odeint(drdt_molla, oinit, otimes, args=(k_molla, m_molla, c_visc, F, fpar, A0))


    # Grafico soluzione
    fig,ax = plt.subplots(3,1, figsize=(12,10), sharex=True)
    ax[0].plot(otimes, F(otimes, fpar, A0),  color='darkred')
    ax[1].plot(otimes, sol[:,0],         color='cornflowerblue')
    ax[2].plot(otimes, sol[:,1],         color='orange')
    ax[2].set_xlabel('time [s]')
    ax[0].set_ylabel('F    [N]')
    ax[1].set_ylabel('x    [m]')
    ax[2].set_ylabel('v    [m/s]')
    plt.show()



    #--------------------------------------------------------------------------------#
    #          Scansione ampiezza massima in funzione del parametro della forza      #
    #--------------------------------------------------------------------------------#

    # Lista ampiezze massime
    A = []
    fmax = []
    
    # array per  valori parametro forza
    of = np.logspace(-1, 2, 100)
    
    # Ciclo soluzione in funzione del parametro della forza
    for oo in of: 
        sol  = integrate.odeint(drdt_molla, oinit, otimes, args=(k_molla, m_molla, c_visc, F, oo, A0))
        A += [np.max(np.abs(sol[:,0]))]

        
    
    # Grafico Ampiezza vs parametro forza
    fig,ax = plt.subplots(figsize=(12,10))
    plt.plot(of, A, lw=2, color='royalblue')
    plt.xlabel(r'$par_F$',       fontsize=16)
    plt.ylabel(r'$A_{max}$ [m]', fontsize=16)
    plt.xscale('log')
    plt.ylim(0, max(A)*1.1)
    plt.show(), 

    


############################################################################
#         main                                                             #
############################################################################

if __name__ == "__main__":

    oscliialtore_forzato()
    
