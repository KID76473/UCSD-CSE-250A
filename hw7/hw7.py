import numpy as np


ids = np.array([])
with open('hw7_ids-2.txt', 'r') as f:
    for line in f.readlines():
        ids = np.append(ids, line.strip())
n_students = np.size(ids)

movies = np.array([])
with open('hw7_movies-1.txt', 'r') as f:
    for line in f.readlines():
        movies = np.append(movies, line.strip())
n_movies = np.size(movies)

probR = np.loadtxt('hw7_probR_init.txt')
probZ = np.loadtxt('hw7_probZ_init.txt')
ratings = []
with open('hw7_ratings-1.txt', 'r') as f:
    for line in f.readlines():
        ratings.append(line.strip().split())
ratings = np.array(ratings)

# a
rec = np.zeros(n_movies)
for i in range(n_movies):
    cur_sum = 0
    cur_total = 0
    for j in range(n_students):
        cur_sum += 1 if ratings[j][i] == '1' else 0
        cur_total += 1 if ratings[j][i] != '?' else 0
    rec[i] = cur_sum / cur_total
sorted_indices = np.argsort(rec)[::-1]
ranking = movies[sorted_indices]
print("Movies ranked from least to most popular:")
for i in ranking:
    print(i)


# e
def calculate_log_likelihood(pz, pr, rates, n_s, n_m, k):
    res = 0
    for t in range(n_s):
        student_likelihood = 0
        for i in range(k):
            p = pz[i]
            for j in range(n_m):
                if rates[t, j] != '?':
                    r_tj = int(rates[t, j])
                    p *= pr[j][i] ** r_tj * (1 - pr[j][i]) ** (1 - r_tj)
            student_likelihood += p
        res += np.log(student_likelihood)
    res /= n_s
    return res


n_movies = np.size(movies)
n_students = np.size(ids)
k = probZ.shape[0]
# print(f"before EM: {calculate_log_likelihood(probZ, probR, ratings, n_students, n_movies, k)}")

num_iterations = 256
log_likelihoods = []

# EM
for iteration in range(num_iterations):
    # E-step
    rho = np.zeros((k, n_students))
    for t in range(n_students):
        denom = 0
        for i in range(k):
            prob = probZ[i]
            for j in range(n_movies):
                if ratings[t][j] != '?':
                    if ratings[t][j] == '1':
                        prob *= probR[j][i]
                    else:
                        prob *= 1 - probR[j][i]
            rho[i, t] = prob
            denom += prob
        for i in range(k):
            rho[i, t] /= denom

    # M-step
    for i in range(k):
        probZ[i] = np.sum(rho[i, :]) / n_students

        for j in range(n_movies):
            num = 0
            for t in range(n_students):
                if ratings[t][j] != '?':
                    if ratings[t][j] == '1':
                        num += rho[i, t]
                else:
                    num += rho[i, t] * probR[j][i]
            denom = np.sum(rho[i, :])
            probR[j][i] = num / denom

    log_likelihood = calculate_log_likelihood(probZ, probR, ratings, n_students, n_movies, k)
    log_likelihoods.append(log_likelihood)

    if iteration in [0, 1, 3, 7, 15, 31, 63, 127, 255]:
        print(f"Iteration {iteration + 1}, Log-Likelihood: {log_likelihood:.4f}")

# f
student_index = 28
my_rate = ratings[student_index]
expected_ratings = np.zeros(n_movies)
for j in range(n_movies):
    if my_rate[j] == '?':
        expected_rating = 0
        for i in range(probZ.shape[0]):
            expected_rating += rho[i, student_index] * probR[j][i]
        expected_ratings[j] = expected_rating

# Sort movies by expected ratings
unseen_movies_indices = [j for j in range(n_movies) if my_rate[j] == '?']
sorted_unseen_indices = sorted(unseen_movies_indices, key=lambda x: expected_ratings[x], reverse=True)
print("Personal movie recommendations ranked by expected rating:")
for idx in sorted_unseen_indices:
    print(f"{movies[idx]} {expected_ratings[idx]:.4f}")
