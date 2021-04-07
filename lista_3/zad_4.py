import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [16,12]
plt.rcParams.update({'font.size': 18})

def signal_create():    # tworzenie sygnału wraz ze sztucznym szumem
    f = np.sin(3*np.pi*2*t) + np.sin(5*np.pi*t) + np.sin(5*np.pi*5*t)
    f_clean = f
    f = f + np.random.randn(len(t))
    
    return f_clean,f


def ploting():
    f_clean,f = signal_create()
    plt.plot(t,f,color='c',label='noise')
    plt.plot(t,f_clean, color='r',label='clean')
    plt.xlim(t[0],t[-1])
    plt.legend()
    plt.show() 


dt = 0.001
t = np.arange(0,1,dt)
print(signal_create())
ploting()