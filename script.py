#Sample script to test calling another python script
import matplotlib.pyplot as plt
import numpy as np
import sys


print(f'Hello I\'m: {sys.executable}')
print(f'I was called with: {sys.argv[1:]}')
x = np.arange(10)
y = x**2
fig, ax = plt.subplots()
ax.plot(x,y, 'o-')
plt.show() #Blocks here