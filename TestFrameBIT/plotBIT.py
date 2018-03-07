import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    plt.plot([2,4,6,8,10])
    plt.ylabel('amp')
    plt.show()
    
    plt.plot([1,2,3,6],[2,3,4,5], 'ro')
    plt.axis([0, 10, 0, 10])
    plt.xlabel('freq')
    plt.ylabel('amp')
    plt.show()
    
    t = np.arange(0.,5.,0.2)
    plt.plot(t, t, '--r', t, t**2, 'bs', t, t**3, 'g^')
    
    # Categorical vars
    names = ['group_A', 'group_B', 'group_C']
    values = [1, 10, 100]
    plt.figure(1, figsize=(9,3))
    
    plt.subplot(131)
    plt.bar(names, values)
    plt.subplot(132)
    plt.scatter(names, values)
    plt.subplot(133)
    plt.plot(names, values)
    
    plt.show()

   