import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [4, 6, 3, 7, 2]
plt.plot(x, y)
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Matplotlib - Save plot but dont show")
plt.savefig("filename.png")
plt.close()