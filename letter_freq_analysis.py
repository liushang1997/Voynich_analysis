import re
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from matplotlib import pyplot

f = open('VM_letter_count')
VM_letter_freq = f.read()

mid_pro = re.compile(r'\t').sub('\n', VM_letter_freq)
VM_letter_freq_list = re.split('\n', mid_pro)
del VM_letter_freq_list[-1]

VM_letter_list, VM_count_list = [], []

for i in range(len(VM_letter_freq_list)):
    if i % 2 == 0:
        VM_letter_list.append(VM_letter_freq_list[i])
    else:
        VM_count_list.append(int(VM_letter_freq_list[i]))

VM_freq_list = []

for i in range(len(VM_count_list)):
    VM_freq_list.append(float('%.2f' % (float((VM_count_list[i]/sum(VM_count_list))*100))))

print(VM_letter_list, VM_count_list, VM_freq_list)

plt.bar(VM_letter_list, VM_count_list, alpha=0.45, width=1.0, facecolor='grey', edgecolor='black')
plt.xlabel('EVA(Voynichese Transcription) Letter')
plt.ylabel('Total Count in VMS')
plt.title('VMS Letter Count Distribution')
# plt.show()
plt.savefig('VM_letter_freq.png', dpi=800)

VM_freq_list_sort = sorted(VM_freq_list, reverse=True)


def freq_file_processor(filename):
    file = open(filename)
    content = file.read()
    mid_pro_0 = re.compile(r'\t').sub('\n', content)
    mid_pro_1 = re.compile(r',').sub('.', mid_pro_0)
    split_list = re.split('\n', mid_pro_1)
    freq_list = []
    for j in range(len(split_list)):
        if j % 2 == 1:
            freq_list.append(float('%.2f' % (float(split_list[j]))))
    return freq_list


English_freq_list = freq_file_processor('English_letter_freq')
Turkish_freq_list = freq_file_processor('Turkish_letter_freq')
Russian_freq_list = freq_file_processor('Russian_letter_freq')
Latin_freq_list = freq_file_processor('Latin_letter_freq')
Hebrew_freq_list = freq_file_processor('Hebrew_letter_freq')

# plt.plot(range(len(VM_freq_list_sort)), VM_freq_list_sort, linewidth=4.0, label='Voynichese')
# plt.plot(range(len(English_freq_list)), English_freq_list, label='English')
# plt.plot(range(len(Russian_freq_list)), Russian_freq_list, label='Russian')
# plt.plot(range(len(Latin_freq_list)), Latin_freq_list, label='Latin')
# plt.plot(range(len(Hebrew_freq_list)), Hebrew_freq_list, label='Hebrew')
# plt.legend(loc='upper right')
# # plt.show()
# # plt.rcParams['savefig.dpi'] = 800
# # plt.rcParams['figure.dpi'] = 800
# plt.xlabel('Letter Rank')
# plt.ylabel('Frequency')
# plt.title('Letter Frequency Comparison in Various Languages')
# plt.savefig('letter_freq_compare.png', dpi=800)

