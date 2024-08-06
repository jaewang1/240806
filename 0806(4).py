import matplotlib.pyplot as plt

categories = ["Apple", 'Banana', 'Orange', 'strawberry', 'Grape']
values = [20, 30, 15, 20, 35]

plt.clf()
plt.bar(categories, values, color = 'skyblue')
plt.title("Fruit Sales")
plt.xlabel("Fruit")
plt.ylabel("sales")

plt.show()
plt.savefig("./bar.png")