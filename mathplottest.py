#line plot

import matplotlib.pyplot as plt

year=[1983,1984,1985,1986,1987]
tot=[8989007,8954152,8954518,8956741,8943721]

plt.plot(year,tot)
plt.title("Year vs pop")
plt.xlabel("year")
plt.ylabel("Tot")
plt.show()

#scatter plot

import matplotlib.pyplot as plt

temp=[30,32,33,28.5,35,29,29]
ice=[100,115,115,75,125,79,89]

plt.scatter(temp,ice)
plt.title("temp vs ice")
plt.xlabel("temp")
plt.ylabel("sold ice")
plt.show()

#box plot

import matplotlib.pyplot as plt

val=[1,2,5,6,6,7,7,8,8,8,9,10,21,100]

plt.boxplot(val)
plt.ylabel("value")
plt.show()

#histogram plot

import matplotlib.pyplot as plt

numbs=[0.1,0.5,1,1.5,2,4,5.5,6,8,9]

plt.hist(numbs,bins=3)
plt.xlabel("num")
plt.ylabel("frequency")
plt.show()

#bar plot

import matplotlib.pyplot as plt

labels=["java","javascrpit","python","C#"]
usage=[69.8,45.3,38.8,34.4]
y_pos=range(len(labels))
plt.bar(y_pos,usage)
plt.xticks(y_pos,labels)
plt.ylabel("Usage(%)")
plt.title("Pgrogramming language usuage ")
plt.show()

#pie plot

import matplotlib.pyplot as plt

sizes=[25,20,45,10]
labels=["CAt","Dog","Tiger","Goat"]

plt.pie(sizes,labels=labels,autopct="%.2f")
plt.axes().set_aspect("equal")
plt.show()
