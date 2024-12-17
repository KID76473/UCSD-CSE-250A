import string


with open('hw1_word_counts_05-1.txt', 'r') as file:
    content = file.read()

# a
total = 0
word_list = {}

for line in content.strip().split("\n"):
    line = line.strip().split(" ")
    count = int(line[1])
    word_list[line[0]] = count
    total += count

for word in word_list:
    word_list[word] /= total

largest = sorted(word_list, key=word_list.get, reverse=True)[:15]
smallest = sorted(word_list, key=word_list.get)[:14]

print("Most frequent 15 words: ")
for key in largest:
    print(key, word_list[key] * total)

print("Least frequent 14 words: ")
for key in smallest:
    print(key, word_list[key] * total)

# b
letters = {letter: 0 for letter in string.ascii_uppercase}

# 1 _____
for word in word_list:
    for letter in set(word):
        letters[letter] += word_list[word]
max_key = max(letters, key=letters.get)
print(1, max_key, letters[max_key])

# 2 _____ xxx{E, A}xxx
for key in letters:
    letters[key] = 0

denom = 0
for word in word_list:
    if 'E' not in word and 'A' not in word:
        denom += word_list[word]
# print(f"denominator: {denom}")

for word in word_list:
    if 'E' not in word and 'A' not in word:
        P_of_W_given_E = word_list[word] / denom
        for letter in set(word):
            letters[letter] += P_of_W_given_E
max_key = max(letters, key=letters.get)
print(2, max_key, letters[max_key])

# 3 A___S xxx{}xxx
for key in letters:
    letters[key] = 0

denom = 0
for word in word_list:
    if word[0] == 'A' and word[-1] == 'S' and 'A' not in word[1: -1] and 'S' not in word[1: -1]:
        denom += word_list[word]

for word in word_list:
    if word[0] == 'A' and word[-1] == 'S' and 'A' not in word[1: -1] and 'S' not in word[1: -1]:
        P_of_W_given_E = word_list[word] / denom
        for letter in set(word[1: -1]):
            letters[letter] += P_of_W_given_E
max_key = max(letters, key=letters.get)
print(3, max_key, letters[max_key])

# 4 A___S xxx{I}xxx
for key in letters:
    letters[key] = 0

denom = 0
for word in word_list:
    if word[0] == 'A' and word[-1] == 'S' and 'A' not in word[1: -1] and 'S' not in word[1: -1] and 'I' not in word:
        denom += word_list[word]
# print(denom)

for word in word_list:
    if word[0] == 'A' and word[-1] == 'S' and 'A' not in word[1: -1] and 'S' not in word[1: -1] and 'I' not in word:
        P_of_W_given_E = word_list[word] / denom
        for letter in set(word[1: -1]):
            letters[letter] += P_of_W_given_E
max_key = max(letters, key=letters.get)
print(4, max_key, letters[max_key], '*')
# print(letters)

# 5 __O__ xxx{A, E, M, N, T}xxx
for key in letters:
    letters[key] = 0

denom = 0
for word in word_list:
    if word[2] == 'O' and 'O' not in word[: 2] + word[3:] and 'A' not in word and 'E' not in word and 'M' not in word and 'N' not in word and 'T' not in word:
        denom += word_list[word]

for word in word_list:
    if word[2] == 'O' and 'O' not in word[: 2] + word[3:] and 'A' not in word and 'E' not in word and 'M' not in word and 'N' not in word and 'T' not in word:
        P_of_W_given_E = word_list[word] / denom
        for letter in set(word[: 2] + word[3:]):
            letters[letter] += P_of_W_given_E
max_key = max(letters, key=letters.get)
print(5, max_key, letters[max_key])

# 6 _____ xxx{E, O}xxx
for key in letters:
    letters[key] = 0

denom = 0
for word in word_list:
    if 'E' not in word and 'O' not in word:
        denom += word_list[word]

for word in word_list:
    if 'E' not in word and 'O' not in word:
        P_of_W_given_E = word_list[word] / denom
        letter_set = set()
        for letter in set(word):
            letters[letter] += P_of_W_given_E
max_key = max(letters, key=letters.get)
print(6, max_key, letters[max_key], '*')

# 7 D__I_ xxx{}xxx
for key in letters:
    letters[key] = 0

denom = 0
for word in word_list:
    if word[0] == 'D' and word[3] == 'I' and 'D' not in word[1: 3] + word[-1] and 'I' not in word[: 3] + word[-1]:
        denom += word_list[word]

for word in word_list:
    if word[0] == 'D' and word[3] == 'I' and 'D' not in word[1: 3] + word[-1] and 'I' not in word[: 3] + word[-1]:
        P_of_W_given_E = word_list[word] / denom
        for letter in set(word[1: 3] + word[-1]):
            letters[letter] += P_of_W_given_E
max_key = max(letters, key=letters.get)
print(7, max_key, letters[max_key])

# 8 D__I_ xxx{A}xxx
for key in letters:
    letters[key] = 0

denom = 0
for word in word_list:
    if word[0] == 'D' and word[3] == 'I' and 'D' not in word[1: 3] + word[-1] and 'I' not in word[: 3] + word[-1] and 'A' not in word:
        denom += word_list[word]

for word in word_list:
    if word[0] == 'D' and word[3] == 'I' and 'D' not in word[1: 3] + word[-1] and 'I' not in word[: 3] + word[-1] and 'A' not in word:
        P_of_W_given_E = word_list[word] / denom
        for letter in set(word[1: 3] + word[-1]):
            letters[letter] += P_of_W_given_E
max_key = max(letters, key=letters.get)
print(8, max_key, letters[max_key], '*')

# 9 _U___ xxx{A, E, I, O, S}xxx
for key in letters:
    letters[key] = 0

denom = 0
for word in word_list:
    if word[1] == 'U' and'U' not in word[0] + word[2: ]and 'A' not in word and 'E' not in word and 'I' not in word and 'O' not in word and 'S' not in word:
        denom += word_list[word]

for word in word_list:
    if word[1] == 'U' and'U' not in word[0] + word[2: ]and 'A' not in word and 'E' not in word and 'I' not in word and 'O' not in word and 'S' not in word:
        P_of_W_given_E = word_list[word] / denom
        for letter in set(word[0] + word[2:]):
            letters[letter] += P_of_W_given_E
max_key = max(letters, key=letters.get)
print(5, max_key, letters[max_key])
