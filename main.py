import numpy as np
from matplotlib import pyplot as plt
k = 1
liambda = 1
n = 2
liambda_old = 9999999
var_old = 9999999

def get_erlang(liambda, k, n):
    erlang_s = np.random.exponential(1/liambda, n)
    for _ in range(k-1):
        erlang_s += np.random.exponential(1/liambda, n)
    return list(erlang_s)
liambda_new = np.array([])
var_new = np.array([])
tliambda = 1/(k/liambda)
tvar = (k/liambda**2)**0.5/(k/liambda)
while True:
    sample = get_erlang(liambda, k, n)
    s_mean = np.mean(sample)
    liambda_new = np.concatenate([liambda_new, [1/s_mean]])
    var_new = np.concatenate([var_new, [np.std(sample) / s_mean]])
    if (abs((liambda_new[-1] - liambda_old) / liambda_old) > 0.01 or abs((var_new[-1] - var_old) / var_old) > 0.01):
        n = 2*n
        liambda_old = liambda_new[-1]
        var_old = var_new[-1]
    else:
        break
plt.figure()
plt.plot(np.full(2**len(liambda_new), tliambda), color = 'grey', ls = '--', lw = 2)
plt.plot(np.geomspace(2, 2**len(liambda_new), num = len(liambda_new), dtype = np.int64), liambda_new, color = 'red', lw = 2)
plt.xscale('log', basex = 2)
plt.title('График зависимости интенсивности потока от объёма выборки')
plt.grid(True)
plt.show()
plt.figure()
plt.plot(np.full(2**len(var_new), tvar), color = 'grey', ls = '--', lw = 2)
plt.plot(np.geomspace(2, 2**len(var_new), num = len(var_new), dtype = np.int64), var_new, color = 'red', lw = 2)
plt.xscale('log', basex = 2)
plt.title('График зависимости коэффициента вариации от объёма выборки')
plt.grid(True)
plt.show()
