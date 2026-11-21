# image function
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# image=mpimg.imread('banner.png')
# fig,ax=plt.subplots()      
# ax.set_title('school image')
# ax.set_xlabel('x-axis')
# ax.set_ylabel('y-axis')
# plt.imshow(image)
# plt.show()


# axis functions
# from matplotlib import pyplot as plt
# import numpy as np
# x=np.array(['2020','2021','2022','2023'])
# y=np.array([90,60,80,75])
# plt.plot(x,y)
# plt.xlabel('year')
# plt.ylabel('pass percentages')
# plt.title('result')
# plt.show()


# 1. Axes
# Graph बनाने के लिए plotting area (Axes) create करता है।
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots()
# ax.plot([1, 2, 3], [10, 20, 30])
# plt.show()

# 2. Text
# Graph के अंदर किसी भी जगह text लिखने के लिए text() का उपयोग करते हैं।
# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3], [10, 20, 30])
# plt.text(2, 20, 'Hello Students')
# plt.show()


# 3. Title
# Graph के ऊपर heading लिखने के लिए।
# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3], [10, 20, 30])
# plt.title('Student Performance')
# plt.show()


# 4. Xlabel
# X-axis का नाम लिखने के लिए।
# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3], [10, 20, 30])
# plt.xlabel('Students')
# plt.show()


# 5. Xlim
# X-axis की minimum और maximum range set करने के लिए।
# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3], [10, 20, 30])
# plt.xlim(0,5)
# plt.show()

# 6. Xticks
# X-axis पर numbers की position set करने के लिए।

# import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4,5], [10, 20, 30, 40,50])

# plt.xticks([1, 2, 3,4,5])

# plt.show()


# 7. Ylabel
# Y-axis का नाम लिखने के लिए।

# import matplotlib.pyplot as plt

# plt.plot([1, 2, 3], [10, 20, 30])

# plt.ylabel('Marks')

# plt.show()


# 8. Yscale
# Y-axis का scale बदलने के लिए।
# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4], [10, 100, 1000, 10000])
# plt.yscale('log')
# plt.show()

# 9. Yticks
# Y-axis पर numbers की position set करने के लिए।

# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4], [10, 20, 30, 40])
# plt.yticks([10, 20, 30, 40])
# plt.show()


# import matplotlib.pyplot as plt
# Data
# x = [1, 2, 3, 4, 5]
# y = [10, 100, 1000, 10000, 100000]
# # Create Axes
# fig, ax = plt.subplots()
# # Plot Graph
# ax.plot(x, y, marker='o')
# # Title
# ax.set_title('Student Performance')
# # X-axis Label
# ax.set_xlabel('Students')
# # Y-axis Label
# ax.set_ylabel('Marks')
# # X-axis Limit
# ax.set_xlim(0, 6)
# # X-axis Ticks
# ax.set_xticks([1, 2, 3, 4, 5])
# # Y-axis Scale
# ax.set_yscale('log')
# # Y-axis Ticks
# ax.set_yticks([10, 100, 1000, 10000, 100000])
# # Text
# ax.text(2, 100, 'Student Data')
# # Show Graph
# plt.show()


# figure function Python Matplotlib में plt.figure() एक नई Figure (चित्र या कैनवास) बनाने का function है, जिसके अंदर हम graph, chart, title, text आदि बना सकते हैं।

import matplotlib.pyplot as plt
fig=plt.figure(figsize=[5,4])
plt.figtext(0.5,0.9,'example of figure function')
x=[1,2,3,4,5]
y=[10,8,6,4,2]
plt.plot(x,y, marker='o',label='line')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.savefig('banner.png')
plt.show()
plt.close(fig)

