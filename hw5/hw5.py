import numpy as np


def log_likelihood(x, y, prob):
    product = 1
    for i in range(len(y)):
        temp = 1 - np.prod([(1 - prob[j]) ** x[i][j] for j in range(n_var)])
        if y[i] == 0:
            temp = 1 - temp
        product *= temp
    return np.log(product) / n_exp


def mistakes(x, y, prob):
    m = 0
    for i in range(n_exp):
        y_given_x = (1 - np.prod([(1 - prob[j]) ** x[i][j] for j in range(n_var)]))
        if y_given_x >= 0.5 and y[i] == 0 or y_given_x <= 0.5 and y[i] == 1:
            m += 1
    return m


spect_x = np.loadtxt('spectX-1.txt')
spect_y = np.loadtxt('spectY-1.txt')
# print(spect_x)

n_var = 23
n_exp = 267
iters = {2 ** i for i in range(9)}  # from 0 to 2^8(256)
p = np.ones(n_var) * 0.05
print(f"Before iteration: {mistakes(spect_x, spect_y, p)} mistakes, log likelihood: {log_likelihood(spect_x, spect_y, p)}")

for iteration in range(1, 257):
    # E-step
    z = np.zeros((n_exp, n_var))
    denominator = 1
    for i in range(n_exp):
        denominator = 1 - (np.prod([(1 - p[j]) ** spect_x[i][j] for j in range(n_var)]))
        for j in range(n_var):
            z[i][j] = spect_y[i] * spect_x[i][j] * p[j] / denominator
            # z[i][j] /= np.sum(spect_x[i])

    # M-step
    updated_p = np.ones(n_var)
    for i in range(n_var):
        updated_p[i] = np.sum(z[:, i]) / np.sum(spect_x[:, i]) if 1 in spect_x[:, i] else p[i]

    # mistakes and likelihood
    if iteration in iters:
        print(f"{iteration}th iteration: {mistakes(spect_x, spect_y, updated_p)} mistakes, log likelihood: {log_likelihood(spect_x, spect_y, updated_p)}")

    p = updated_p
