import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 20]

plt.plot(x, y, marker = '*', linestyle = '-', color = 'red', label = 'temp')
plt.title("dDaily temperature trend")
plt.xlabel("Time (Hour)")
plt.xlabel("Temperature (C)")
plt.legend()
plt.grid(True)
# plt.show()
plt.savefig("./linechart.png")

