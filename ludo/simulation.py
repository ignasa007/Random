import numpy as np
import matplotlib.pyplot as plt

grid_size = 100
max_rolls = 200

A = np.zeros((grid_size, grid_size))
# snakes = {31:14, 41:20, 59:37, 67:50, 92:76, 99:4}
# ladders = {2:23, 8:12, 17:93, 29:54, 32:51, 39:80, 62:78, 70:89, 75:96}
snakes = {16:6, 48:26, 49:11, 56:53, 62:19, 64:60, 87:24, 93:73, 95:75, 98:78}
ladders = {1:38, 4:14, 9:31, 21:42, 28:84, 36:44, 51:67, 71:91, 80:100}

for i in range(1, grid_size+1):
    for j in range(i+1, i+7):
        if j>100:
            A[i-1, i-1] += 1/6
        elif j in snakes:
            A[i-1, snakes[j]-1] += 1/6
        elif j in ladders:
            A[i-1, ladders[j]-1] += 1/6
        else:
            A[i-1, j-1] += 1/6
print(A[-1])

probs = np.zeros((grid_size,1))
for i in range(1, 7):
    probs[i-1] = 1/6

num_moves, probs_grid_size = [1], [probs[grid_size-1]]
for move_num in range(2, max_rolls+1):
    probs = A.T @ probs
    num_moves.append(move_num); probs_grid_size.append(probs[grid_size-1])

fontdict = {'family':'serif', 'color':'darkred', 'weight':'normal', 'size':16}
plt.figure(figsize=(12,6))
plt.xlabel('Rolls', fontdict=fontdict, labelpad=12)
plt.ylabel('Probability', fontdict=fontdict, labelpad=12)
plt.title('Ludo - Number of Rolls vs Probability of Finishing', fontdict=fontdict, pad=12)
plt.plot(num_moves, probs_grid_size, color="g")
plt.grid()
plt.show()
