import re
import matplotlib.pyplot as plt
import numpy as np
import os

f = open('VM_clean_word')
VM_word = f.read()

VM_word_list = re.split('\n', VM_word)
del VM_word_list[-1]

VM_word_dic = {}
for i in VM_word_list:
    VM_word_dic[i] = VM_word_list.count(i)
print(VM_word_dic)

res_sort = sorted(VM_word_dic.items(), key=lambda x: x[1], reverse=True)
print(res_sort)


if os.path.exists('VM_word_dic'):
    os.remove(os.getcwd() + '\VM_word_dic')
    print('Previous file removed!')
else:
    print('Does not exist the "VM_clean_word" file.')

f1 = open('VM_word_dic', 'x')

word_count_list, word_dic_list = [], []
for j in range(len(res_sort)):
    word_count_list.append(res_sort[j][1])
    word_dic_list.append(res_sort[j][0])
    f1.write(res_sort[j][0] + '\n')
print(word_count_list, word_dic_list)

plt.plot(range(len(word_count_list)), word_count_list)
plt.xlabel('Rank of Word Frequency')
plt.ylabel('Word Frequency')
plt.title('Relationship Between Rank and Frequency')
plt.savefig('word_freq.png', dpi=800)

# for i in word_count_list:
#     word_count_list[i] = word_count_list[i] + 1
# plt.plot(np.log(word_count_list)), np.log(range(1, len(word_count_list)+1, 1))
# plt.xlabel('Rank of Word Frequency')
# plt.ylabel('logarithm of Word Frequency')
# plt.title('Relationship Between Rank and Frequency(log)')
# plt.savefig('log_word_freq.png', dpi=800)
