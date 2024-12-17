import numpy as np
import matplotlib.pyplot as plt


# 2
content = ''
with open('hw4_vocab.txt', 'r') as f:
    content = f.read()
vocab = []
for row in content.split('\n'):
    vocab.append(row)
# vocab.pop()
# print(len(words))

with open('hw4_unigram.txt', 'r') as f:
    content = f.read()
unigram = []
for row in content.split('\n'):
    # print(row)
    unigram.append(int(row))
unigram = np.array(unigram)
# print(len(words))

with open('hw4_bigram.txt', 'r') as f:
    content = f.read()
bigram = []
for row in content.split('\n'):
    # print(row.split('\t'))
    bigram.append([int(row.split('\t')[0]), int(row.split('\t')[1]), int(row.split('\t')[2])])
# print(bigram)
# print(bigram[-1])
bigram_mle = []
cur = 1
cur_sum = 0
sub_sum = {}
for b in bigram:
    # print(cur)
    if cur == b[0]:
        cur_sum += b[2]
    else:
        sub_sum[cur] = cur_sum
        cur = b[0]
        cur_sum = 0
sub_sum[500] = cur_sum
print(sub_sum[4])
index = 1


# a
unigram_prob = []
unigram_prob = unigram / np.sum(unigram)
m_tokens = {vocab[i]: unigram_prob[i] for i in range(500) if vocab[i][0] == 'M'}
# print(m_tokens)

# b
# index = vocab.index('THE') + 1
# print(f"index - 1: {index - 1}, vocab: {vocab[index - 1]}")
after_the = []
for x in bigram:
    # print(x)
    if x[0] == 4:
        after_the.append([vocab[x[1]], x[2] / sub_sum[4]])  #
        # print(x[1: ])
after_the.sort(key=lambda a: a[1], reverse=True)
print(after_the[: 10])

# c
def sentence_mle(s: str):
    lu, lb = 1, 1
    last = 1
    # print(f"vocab[last]: {vocab[last]}")  # 1 for <s>
    for word in s.split(' '):
        index = vocab.index(word.upper()) + 1
        # print(f"index: {index}")
        lu *= unigram_prob[index - 1]
        # print(f"unigram p: {unigram_prob[index]}")
        found = False
        for b in bigram:
            # print(b)
            if b[0] == last and b[1] == index:
                # print(f"last: {last}, cur: {index}")
                lb *= b[2] / sub_sum[last]
                found = True
                break
        if not found:
            lb *= 0
            print(f"combination not found: last: {vocab[last - 1]}, cur: {vocab[index - 1]}")
        last = index
    return np.log(lu), np.log(lb)


sentence = "The stock market fell by one hundred points last week"
mle_unigram, mle_bigram = sentence_mle(sentence)
print(f"c: mle_unigram: {mle_unigram}, mle_bigram: {mle_bigram}")

# d
sentence = "The sixteen officials sold fire insurance"
mle_unigram, mle_bigram = sentence_mle(sentence)
print(f"d: mle_unigram: {mle_unigram}, mle_bigram: {mle_bigram}")

# e
def mix_mle(sentence, l):
    lu, lb, mix = 1, 1, 1
    last = 1
    for word in sentence.split(' '):
        index = vocab.index(word.upper()) + 1
        lu *= unigram_prob[index - 1]
        found = False
        for b in bigram:
            if b[0] == last and b[1] == index:
                lb *= b[2] / sub_sum[last]
                found = True
                break
        if not found:
            mix *= l * lu
        else:
            mix *= l * lu + (1 - l) * lb
        last = index
    # print(mix)
    return np.log(mix)

ls = np.linspace(0, 1, 100)
mle = []
for x in ls:
    mix = mix_mle(sentence, x)
    mle.append(mix)
plt.plot(ls, mle)
plt.xlabel('lambda')
plt.ylabel('Probability')
plt.title('Mix Model')
plt.show()
