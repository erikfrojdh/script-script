#Sample script to test calling another python script
import matplotlib.pyplot as plt
import numpy as np
import sys

#Put the functionallity of the script in a function (can have any name...)
def do_stuff(*args):
    print(f'Hello I\'m: {sys.executable}')
    print(f'I was called with: {args}')
    x = np.arange(10)
    y = x**2
    fig, ax = plt.subplots()
    ax.plot(x,y, 'o-')
    plt.show() #Blocks here

#If the script is called from the command line, run main and pass on the arguments
if __name__ == '__main__':
    do_stuff(*sys.argv[1:])