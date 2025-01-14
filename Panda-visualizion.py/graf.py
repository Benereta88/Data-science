"""
Installera först:
pip3 install 

#1
import matplotlib.pyplot as plt
import numpy as np
import math
x_vals = np.linspace(0, 20, 20)
print(x_vals)
y_vals = [math.sqrt(i) for i in x_vals]
plt.plot(x_vals, y_vals)
plt.show()

#2
import matplotlib.pyplot as plt
import numpy as np
import math

x_vals = np.linspace(0, 20, 20)
print(x_vals)
y_vals = [math.sqrt(i) for i in x_vals]
plt.plot(x_vals, y_vals)
plt.show()

#3
import matplotlib.pyplot as plt
import numpy as np
import math

x_vals = np.linspace(0, 20, 20)
y_vals = [math.sqrt(i) for i in x_vals]

fig = plt.figure()
ax = plt.axes()
ax.plot(x_vals, y_vals)
plt.show()

#3
import matplotlib.pyplot as plt
import numpy as np
import math

plt.rcParams["figure.figsize"] = [8,6]

x_vals = np.linspace(0, 20, 20)
y_vals = [math.sqrt(i) for i in x_vals]
plt.plot(x_vals, y_vals)
plt.show()

# 4
import matplotlib.pyplot as plt
import numpy as np
import math

x_vals = np.linspace(0, 20, 20)
y_vals = [math.sqrt(i) for i in x_vals]
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Square Roots')
plt.plot(x_vals, y_vals)
plt.show()

# 5
import matplotlib.pyplot as plt
import numpy as np
import math


x_vals = np.linspace(0, 20, 20)
y_vals = [math.sqrt(i) for i in x_vals]
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Square Roots')
plt.plot(x_vals, y_vals, 'r')
plt.show()

# 6
import matplotlib.pyplot as plt
import numpy as np
import math


x_vals = np.linspace(0, 20, 20)
y_vals = [math.sqrt(i) for i in x_vals]
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Square Roots')
plt.plot(x_vals, y_vals, 'r', label = 'Square Root')
plt.legend(loc='upper center')
plt.show()

#7
import matplotlib.pyplot as plt
import numpy as np
import math


x_vals = np.linspace(0, 20, 20)
y_vals = [math.sqrt(i) for i in x_vals]
y2_vals = x_vals ** 3
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Square Roots')
plt.plot(x_vals, y_vals, 'r', label = 'Square Root')
plt.plot(x_vals, y2_vals, 'b', label = 'Cube')
plt.legend(loc='upper center')
plt.show()

#8
import matplotlib.pyplot as plt
labels = 'IT', 'Marketing', 'Data Science', 'Finance'
values = [500, 156, 300, 510]
explode = (0.05, 0.05, 0.05, 0.05) 

plt.pie(values, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
plt.show()
"""
import matplotlib.pyplot as plt
import numpy as np
import math

plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.title('Sepal vs Petal Length')
plt.plot(data["sepal_length"], data["petal_length"], 'b')
plt.show()



