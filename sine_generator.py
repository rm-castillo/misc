import numpy as np
import matplotlib.pyplot as plt

def generate_sine(cycles = 10, resolution = 1000):
    # Number of sine cycles
    cycles = 10
    # Number of datapoints
    resolution = 1000

    length = np.pi * 2 * cycles
    my_wave = np.sin(np.arange(0, length, length / resolution))

    # add one to each value to change range from -1.0 - 1.0 to 1.0 - 2.0
    my_wave += 1

    # scale the graph by a value between 1 and 50
    #my_wave *= np.random.randint(1, 50)

    plt.plot(np.arange(0,1000), my_wave)
    print(my_wave)
    plt.show()

    return my_wave

if __name__ == '__main__':
    generate_sine()
    # sine_list = []
    # for i in range (0,8):
    #     sine_list.append(generate_sine())

    # print(len(sine_list))