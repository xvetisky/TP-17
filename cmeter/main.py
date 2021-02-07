import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from parser import *

f = open("data.txt", 'r')
model = LinearRegression()

if __name__ == "__main__":
    clean_lines = remove_junk(f)
    final = final_data(clean_lines)
    n = len(final)
    t = np.array([final[i][1] for i in range(n)])
    t1 = t.reshape((-1, 1))
    s = np.array([final[i][2] for i in range(n)])
    c = 3.9175/(s-1.0225)

    new_model = model.fit(t1, c)
    print(f'r^2 = {model.score(t1, c)}')
    a, b = new_model.coef_, new_model.intercept_
    print(f'a = -k = {a}', f'b = {b}')
    y = a*t + b
    plt.plot(t, y, 'b-')
    plt.show()
