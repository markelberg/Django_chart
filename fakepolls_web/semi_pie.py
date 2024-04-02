import matplotlib.pyplot as plt

# data
label = ["A", "B", "C"]
val = [1,2,3]

# append data and assign color
label.append("")
val.append(sum(val))  # 50% blank
colors = ['red', 'blue', 'green', 'white']

# plot
fig = plt.figure(figsize=(8,6),dpi=100)
ax = fig.add_subplot(1,1,1)
ax.pie(val, labels=label, colors=colors)
ax.add_artist(plt.Circle((0, 0), 0.6, color='white'))
fig.show()