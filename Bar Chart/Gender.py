import numpy as np
import matplotlib.pyplot as plt
count = [5, 6, 2, 0]
bars = ('Female', 'Male', 'Prefer not to say', 'Other')
y_pos = np.arange(len(bars))
plt.bar(y_pos, count, color=['red', 'green', 'blue', 'cyan'],edgecolor='blue')
plt.xticks(y_pos, bars)
plt.title('Gender')
plt.show()