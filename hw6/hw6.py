import numpy as np
import matplotlib.pyplot as plt


initial = np.loadtxt('initialStateDistribution.txt')  # (27,)
transition = np.loadtxt('transitionMatrix.txt')  # (27, 27)
emission = np.loadtxt('emissionMatrix.txt')  # (27, 2)
observation = np.loadtxt('observations.txt')  # (430000,)

N = len(initial)
T = len(observation)

# value max
l = np.zeros((N, T))  # (27, 430000)
l[:, 0] = np.log(initial) + np.log(emission[:, int(observation[0])])
for i in range(1, T):
    l[:, i] = np.max(l[:, i - 1][:, np.newaxis] + np.log(transition), axis=0) + np.log(emission[:, int(observation[i])])

# arg max
s = np.zeros(T, dtype=int)
s[-1] = np.argmax(l[:, -1])
for i in range(T - 1, 0, -1):
    s[i - 1] = np.argmax(l[:, i - 1] + np.log(transition[:, s[i]]), axis=0)

no_duplicate = [int(s[0])]
for i in range(1, T):
    if s[i] != s[i - 1]:
        no_duplicate.append(int(s[i]))

letters = {i: chr(97 + i) for i in range(26)}
letters[26] = ' '

message = ''.join([letters[state] for state in no_duplicate])
print(message)

plt.plot(range(T), s)
plt.xlabel('Time')
plt.ylabel('Most Probable State')
plt.title('Most Likely State')
plt.show()
