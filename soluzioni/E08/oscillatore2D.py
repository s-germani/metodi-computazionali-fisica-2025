
############################################################################
# S. Germani (stefano.germani@unipg.it)                                    #
#                                                                          #
# Universià degli Studi di Perugia                                         #
# Corso di Metodi Computazionali per la Fisica                             #
#--------------------------------------------------------------------------#
# Esercitazione 8 - Equazioni Dfferenziali:                                #
#                                                                          #
#   Oscillatore 2D                                                         #
#                                                                          #
############################################################################

import numpy as np
from scipy import integrate, constants
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import argparse


############################################################################
#    Funzione per animazione                                               #  
############################################################################

def animate(i, x, y, dt, line, mass, text):

    """
    Funzione pe animazione pendolo

    Assegna la posizione  istante per istante  agli ogetti da animare
    Il fulcro del pendolo è posizionato alle coordinate (0,0)

    Parametri
    ----------

    i    : indice del frame da rappresenare (obbligatorio con FuncAnimatuin)
    x    : array con coordinate x della massa del pendolo in funzione del tempo
    y    : array con coordinate y della massa del pendolo in funzione del tempo
    dt   : distanza temporale fra i punti dell'array dei tempi con cui si è risolta l'equazione del moto
    line :
    mass : oggetto grafico  che rappresenta la massa del pendolo   (plt.plot(   x[i],    yi[i] ))
    text : testo con tempo che scorre

    Output
    -----------
    return line, mass, text
    """
    
    line_x = x[:i]
    line_y = y[:i]
    line.set_xdata(line_x)
    line.set_ydata(line_y)

    mass_x = x[i]
    mass_y = y[i]
    mass.set_xdata(mass_x)
    mass.set_ydata(mass_y)

    time_template = 'time = %.1fs'
    text.set_text(time_template % (i*dt))

    return line, mass, text
    

############################################################################
#      Funzione per Equazione Differenziale Oscillatore  2D                #
############################################################################

def odeqn2d(rv, t, omegax, omegay):
    """
    drdt(rv, t, omega) derivate per equazione differenziale dell'oscillatore 2D
    rv : vettore con variabili r(x,y,dx/dt,dy/dt)
    t  : variabile tempo
    omegax : pulsazione propria dell'oscillatore per la variabile x
    omegay : pulsazione propria dell'oscillatore per la variabile y
    """
    dxdt = rv[2]
    dydt = rv[3]
    dvxdt = -omegax**2 * rv[0]
    dvydt = -omegay**2 * rv[1]
        
    return (dxdt, dydt, dvxdt, dvydt)


############################################################################
#    Funzione principale  per oscillatore 2D                               #  
############################################################################

def oscliialtore2D():
    
    # Array Tempi 
    dt = 0.01 # s
    otimes = np.arange(0, 60, dt)

    # Pulsazioni X,Y
    omegaX = 1.0
    omegaY = 4.5

    # Condizioni iniziali
    x0  =  4.5
    y0  = -3
    v0X =  1
    v0Y =  5

    odinit2d = (x0, y0, v0X, v0Y)


    # Soluzione
    solXY  = integrate.odeint(odeqn2d, odinit2d, otimes, args=(omegaX,omegaY))



    # Grafico soluzione vs tempo
    fig,ax = plt.subplots(2,1, figsize=(12,10), sharex=True)
    ax[0].plot(otimes, solXY[:,0], color='cornflowerblue' , label='X')
    ax[0].plot(otimes, solXY[:,1], color='orange' ,         label='Y')
    ax[0].set_xlabel('time [s]')
    ax[0].set_ylabel('X/Y  [m]')
    ax[0].legend()
    ax[1].plot(otimes, solXY[:,2], color='cornflowerblue')
    ax[1].plot(otimes, solXY[:,3], color='orange')
    ax[1].set_xlabel('time [s]')
    ax[1].set_ylabel('v    [m/s]')
    plt.show()




    # Grafico soluzione XY
    plt.plot(solXY[:,0], solXY[:,1], color='cornflowerblue')
    plt.plot(x0,y0, 'o', color='red')
    plt.xlabel('X [m]')
    plt.ylabel('Y [m]')
    plt.show()



    #------------------- Animazione  ------------------------------------#

    # Figura per animazione 
    fig = plt.figure(figsize=(9,8))
    ax  = fig.add_subplot(111, autoscale_on=False, xlim=(-6, 6), ylim=(-6, 6))

    # Oggetti da animare (linea, massa, testo)
    line, = ax.plot([], [], '-', lw=1,   color='slategray')
    mass, = ax.plot([x0], [y0], 'o',        markersize=15, color='darkred'  )
    time_text      = ax.text(0.05, 0.9, '', transform=ax.transAxes, fontsize=16)

    # Animazione 
    ani = animation.FuncAnimation(
        fig,                                                      # Figura per animazione
        animate,                                                  # Funzione per animazione con calcolo oggetti ad ogni istante
        np.arange(1, len(otimes)),                                # valori su cui iterare ( corripondnete all'indice i in animate)
        fargs=( solXY[:,0],solXY[:,1],dt, line, mass, time_text), # argomenti aggiuntivi della funzione animate
        interval=5,                                               # Intervallo fra due frame successivi (ms)
        blit=True)                                                # Ottimizzazione grafica

    plt.xlabel('X [m]')
    plt.ylabel('Y [m]')
    plt.show()


############################################################################
#         main                                                             #
############################################################################

if __name__ == "__main__":

    oscliialtore2D()
    
