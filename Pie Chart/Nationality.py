import matplotlib.pyplot as plt
labels = 'India', 'Russia', 'Bangladesh', 'Pakistan', 'Albania'
sizes = [2, 1, 2, 2,1]
colors = ['gold','orange', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0, 0, 0,0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', startangle=140)
plt.title('Nationality')
plt.axis('equal')
plt.show()