# Corso di Metodi Computazionali per la Fisica
## Descrizione delle Soluzioni per le Esercitazioni in Laboratorio.

* Cartella [E02](E02) (Esercitazione 2 - Basi di Python)
  * `somma_100.py` : somma pirmi 100 numeri naturali
  * `somma_n.py`   : somma primi N numeri naturali
  * `myage.py`     : calcolo età
  * `lists.py`     : liste e dizionari

* Cartella [E03](E03) (Esercitazione 3 - Moduli Python ad uso scientifico)
  * `kepler.py`: curva di luce transito esopianeta da missione Keplere/K2
  * `exoplanets.py`: grafici sugli esopianeti
  * `kepler_fold.py`: grafico curva di luce transito esopianeta riferita al periodo (folding)

* Cartella [E05](E05) ( Esercitazione 5 - Funzioni, Metodi e Classi ):
  * `somme.py`                 : file python con esempio di definizione del modulo somme (Esercizi 0 e 1 - Funzioni e Moduli)
  * `uso_somme.py`             : script python che utilizza le funzioni del modulo somme (Esercizi 0 e 1 - Funzioni e Moduli)
  * `reco.py`                  : file per la definzione del modulo reco con le classi Hit (Esercizio 2 - Classi)
  * `events_reconstruction.py` : script python per l'analisi degli Hit attraverso il modulo reco (Esercizio 2 - Classi)

* Cartella [E06](E06) ( Esercitazione 6 - Integrali e Derivate ):
  * `calcolo_distanza.py`       : script python per leggere il file csv con i dati  e calcolare l'integrale della distanza percorsa dalla velocià
  * `oscillatore_anarmonico.py` : script python per calcolare il periodo dell'oscillatore anarmonico
  * `signal_times.py`           : script python per il calcolo delle derivate dei segnali dell'oscilloscopio

* Cartella [E07](E07) ( Esercitazione  - Equazioni Minimizzazione ): 
  * `jpsimass_fit.py` : script python per il fit della massa invariante della J/psi

* Cartella [E08](E08) ( Esercitazione  - Equazioni Differenziali ): 
  * `oscillatore_forzato.py`  : script python per la soluzione dell'equazione differenziale dell'oscillatore forzato
  * `pendulum.py`             : script python per la soluzione dell'equazione differenziale del pendolo
  * `oscillatore2D.py`        : script python per la soluzione dell'equazione differenziale dell'oscillatore armonico 2D

* Cartella   [E09](E09) ( Esercitazione  - Trasformate di Fourier ):
  * `noise_fft.py`       :  script python per l'analisi di Fourier dei vari tipi di rumore
  * `lightcurves_fft.py` :  script python per l'analisi di Fourier delle curve di luce gamma dei blazar

* Cartella   [E10](E10) ( Esercitazione  - Metodi Monte Carlo     ):
  * `probx2.py`        : script python sulle distribuzioni di probabilità  con il metodo Hit or Missa e della cumulativa
  * `diffusione_2d.py` : script python per i grafici sulla diffusione 2D 
  * `mymwpc.py`        : modulo python con la definizione della classe myMWPC (simulazione MWPC)
  * `mymwpcev.py`      : modulo python con la definizione della classe myMWPCev (eventi MWPC)
  * `run_mymwpc.py`    : script python per eseguire la simulazione della MWPC

* Cartella   [E11](E11) ( Esercitazione  - C e Python             ):
  * `compile.sh`       : script shell con comandi per la compilazione delle librerie condivise
  * `serie.c`          : file C con definizione della serie di Fibonaggi (da compilare per generare il file libserie.so)
  * `serie.py`         : modulo python che utilizza la libreria condivisa serie
  * `serie_py.py`      : modulo python che calcola la successione di Fibonacci solo tramite codice python (per confronto prestazioni 
  * `run_serie.py`     : script python per eseguire i moduli sulla successione di Fibonacci
  * `mycamera.py`      : modulo python che utilizza la libreria condivisa mycamera
  * `run_mycamera.py`  : script python che utilizza il modulo mycamera per acquisire l'immagine della fotocamera
  * `mycamerac.py`     : modulo python che utilizza la libreria condivisa mycamera definendo la classe myCamera 
  * `run_mycamerac.py` : script python che utilizza il modulo mycamerac per acquisire l'immagine della fotocamera
  * `mandelbrot.py`    : script python per il calcolo e la visulalizzazione degli insiemi di mandelbrot con compilazione JIT numba
  