import numpy as np
import matplotlib.pyplot as plt
import scipy
from signalGeneration import Generator


generator = Generator()

num_miscroseconds = 100
num_samples= 10000

X = np.linspace(0,num_miscroseconds, num_samples)
Y = generator.get_PMT_signal(A = 300, T = X, t_0 = -10, Tao_fall=2.5, Tao_rise=0.7, Tao_fall_spe = 8 , Tao_rise_spe = 1.5)

plt.plot(X,Y)
plt.show() 
