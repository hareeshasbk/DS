import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')

x=list(range(1,10))
plt.plot(x ,[y for y in x])
plt.title("linear search- time complexity is O(n)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()
