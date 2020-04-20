import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('countries.csv')
print(data.columns)
china = data[data.country == 'China']
india = data[data.country == 'India']
plt.plot(china.year, china.population / 10**6)
plt.plot(india.year, india.population / 10**6)
plt.xlabel('Years')
plt.ylabel('Population (in millions)')
plt.title('Population Graph')
plt.legend(['China', 'India'])
plt.show()