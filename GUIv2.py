from matplotlib import pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax2 = fig.add_subplot(1, 1, 1)
ax3 = fig.add_subplot(1, 1, 1)
ax4 = fig.add_subplot(1, 1, 1)
ax5 = fig.add_subplot(1, 1, 1)


def animate(i):
        pullData = open('measurements', 'r').read()
        dataArray = pullData.split('\n')
        xar = []
        yar = []
        yar2 = []
        yar3 = []
        yar4 = []
        yar5 = []
        for eachLine in dataArray:
                if (len(eachLine) > 1):
                        x, y, y2, y3, y4, y5 = eachLine.split(',')
                        xar.append(int(x))
                        yar.append(int(y))
                        yar2.append(int(y2))
                        yar3.append(int(y3))
                        yar4.append(int(y4))
                        yar5.append(int(y5))
        ax1.clear()
        ax2.clear()
        ax3.clear()
        ax4.clear()
        ax5.clear()
        ax1.plot(xar, yar, 'g', linewidth = 3, label = 'RPM')
        ax2.plot(xar, yar2, 'c', linewidth = 3, label = 'KM per hour')
        ax3.plot(xar, yar3, 'r', linewidth = 3, label = 'Distance(meters)')
        ax4.plot(xar, yar4, 'm', linewidth = 3, label = 'MPH')
        ax5.plot(xar, yar5, 'k', linewidth = 3, label = 'Distance(Miles)')


plt.title("Speed and Distance")
plt.ylabel("Magnitude")
plt.xlabel("Rotations")

# within the () is the figure, the function animate, and the time it takes to refresh (interval)
ani1 = animation.FuncAnimation(fig, animate, interval = 1000)
# ani2 = animation.FuncAnimation(fig, animate, interval = 1000)

plt.legend()

plt.grid(True, color = "k")

plt.show()
