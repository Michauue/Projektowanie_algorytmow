import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [18, 6]
plt.rcParams.update({"font.size": 15})


def signal_create():  # tworzenie sygnału wraz ze sztucznym szumem
    f = np.sin(50 * T) + np.sin(25 * T) + np.sin(100 * T)
    f_clean = f * np.hanning(len(T * 0.01))
    f = (f * np.hanning(len(T))) + np.random.randn(len(T))  # dodanie okna czasowego von Hanna do sygnału
    return f_clean, f


def f_fourier_transform():  # zastosowanie szybkiej transformaty Fouriera (FFT)
    n = len(T)
    f = signal_create()[1]
    fhat = np.fft.fft(f, n)
    PSD = fhat * np.conj(fhat) / n
    frequency = (1 / (DT * n)) * np.arange(n)
    L = np.arange(1, np.floor(n / 2), dtype="int")

    return frequency, L, PSD, fhat


def noise_filter():  # odfiltrowanie szumów
    PSD, fhat = f_fourier_transform()[2:4]
    indices = PSD > 10
    # for i in range(1000):
    #     if indices[i] == True:
    #         z = i
    # indices[z] = False
    PSDClean = PSD * indices
    fhat = indices * fhat
    inv_filtered = np.fft.ifft(fhat)

    return inv_filtered, PSDClean


def ploting():  # generowanie wykresów

    # pobranie danych do wygenerowania wykresów

    f_clean, f = signal_create()
    frequency, L, PSD = f_fourier_transform()[0:3]
    inv_filtered, PSDClean = noise_filter()

    fig, axs = plt.subplots(3, 1)

    # wykres sygnału z sztucznie wygenerowanym szumem

    plt.sca(axs[0])
    plt.plot(T, f, color="c", label="noise")
    plt.plot(T, f_clean, color="r", label="clean")
    plt.xlim(T[0], T[-1])
    plt.legend(loc=1)

    # wykres odfiltrowanego sygnału

    plt.sca(axs[1])
    plt.plot(T, inv_filtered, color="r", linewidth=2, label="filtered")
    plt.xlim(T[0], T[-1])
    plt.legend(loc=1)

    # wykres odfiltrowanych częstotliwości

    plt.sca(axs[2])
    plt.plot(frequency[L], PSD[L], color="c", linewidth=2, label="noise")
    plt.plot(frequency[L], PSDClean[L], color="r", label="filtered")
    plt.xlim(frequency[L[0]], frequency[L[-1]])
    plt.legend(loc=1)
    plt.show()


# stałe używane do wykonania zadania

DT = 0.001
T = np.arange(0, 1, DT)

# uruchomienie programu

signal_create()
f_fourier_transform()
noise_filter()
ploting()
