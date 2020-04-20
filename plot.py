import pandas as pd
from matplotlib import pyplot as plt

x = [10,22,45,67,99]
y = [5,10,23,45,67]
z = [3,6,9,12,15]
plt.plot(x,y)
plt.plot(x,z)
plt.title('Weekly Sales')
plt.xlabel('Sales')
plt.ylabel('Revenue')
plt.legend(['2012', '2013'])
plt.show()

