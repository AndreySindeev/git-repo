import matplotlib.pyplot as plt
import numpy as np
from matplotlib import mlab

a = int(input("Enter value for CIFS-SMB capacity on 3100 Applince : "))
b = int(input("Enter value for SMB-2 capcity on 3100 Applince : "))
c = int(input("Enter value for ISCSI capacity on 3100 Applince : "))
d = int(input("Enter value for HTTP capacity on 3100 Applince : "))


#список гистограмм по оси X
X = [i for i in (a, b, c, d)]
#длинна оси Y высчитывается по максимальному значения оси Х
Y = np.arange(len(X))
#цвета гистограмм
colors = ['red', 'orange', 'green', 'yellow']
#список с названиями протоколов,для каждой гистограммы
LIST_VALUE = ['CFS-SMB', 'SMB-2', 'ISCSI', 'HTTP']
#функция создания гистограмм, с параметрами
#plt.bar(Y,X, align = 'center', color = colors, edgecolor = colors)
#передача оси Y списка названий протоколов


plt.subplot(4, 3, 1)
plt.bar(Y,X, align = 'center', color = colors, edgecolor = colors)
plt.xticks(Y, LIST_VALUE)
plt.title("1")

plt.subplot(4, 3, 3)
plt.bar(Y,X, align = 'center', color = colors)
plt.xticks(Y, LIST_VALUE)
plt.title("2")

plt.show()
