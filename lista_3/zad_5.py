import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [18,6]
plt.rcParams.update({'font.size': 15})

def signal_create():    # tworzenie sygnału wraz ze sztucznym szumem
    f = np.sin(2*np.pi*50*T) + np.sin(2*np.pi*25*T) + np.sin(2*np.pi*100*T)
    f_clean = f
    f = f + np.random.randn(len(T))
    
    return f_clean,f

def f_fourier_transform(): # zastosowanie szybkiej transformaty Fouriera (FFT)
    n = len(T)
    f = signal_create()[1]
    fhat = np.fft.fft(f,n)
    PSD = fhat * np.conj(fhat) / n
    frequency = (1/(DT*n)) * np.arange(n)
    L = np.arange(1,np.floor(n/2),dtype='int')

    return frequency, L, PSD


def ploting(): # generowanie wykresów

    # pobranie danych do wygenerowania wykresów 

    f_clean,f = signal_create()
    frequency, L, PSD = f_fourier_transform()

    fig,axs = plt.subplots(2,1)

    # wykres sygnału z sztucznie wygenerowanym szumem

    plt.sca(axs[0])
    plt.plot(T,f,color='c',label='noise')
    plt.plot(T,f_clean, color='r',label='clean')
    plt.xlim(T[0],T[-1])
    plt.legend()

    # wykres częstotliwości po zastosowaniu FFT

    plt.sca(axs[1])
    plt.plot(frequency[L],PSD[L],color='c',label='noisy')
    plt.xlim(frequency[L[0]],frequency[L[-1]])
    plt.show()


# stałe używane do wykonania zadania

DT = 0.001
T = np.arange(0,1,DT)

# uruchomienie programu

signal_create()
f_fourier_transform()
ploting()
