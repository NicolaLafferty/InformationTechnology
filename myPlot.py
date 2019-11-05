import matplotlib.pyplot as plt

xlist = [1, 12, 34, 56, 7, 78, 90, 8, 48, 73]
ylist = ['desmond', 'jacob', 'samantha', 'juliet', 'julie', 'immogen', 'charlie', 'flynn', 'aaron', 'houdini']

plt.ylabel('This is the y label')
plt.xlabel('This is the x label')

plt.title('This is the title')

plt.barh(xlist, ylist)

plt.show()