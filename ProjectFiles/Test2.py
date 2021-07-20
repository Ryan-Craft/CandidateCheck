print("Hello World")
import numpy as np
import matplotlib.pyplot as plot

array1 = np.random.randint(0,10,10)
array2 = np.random.randint(0,10,10)

print(array1, array2)

plot.scatter(array1, array2)
plot.show()
