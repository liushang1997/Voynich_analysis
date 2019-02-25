import re
import os

f = open("VM.txt")
VM_origin = f.read()
f.close()

VM_1 = re.compile(r'<[^>]+>').sub('', VM_origin)
VM_2 = re.compile(r' ').sub('', VM_1)
VM_3 = re.compile(r'\n\n').sub('\n', VM_2)
VM_4 = re.compile(r'#+\n').sub('', VM_3)
VM_5 = re.compile(r'#.+\n').sub('', VM_4)
VM_6 = re.compile(r'\.').sub('\n', VM_5)

VM_clean_word = VM_6

if os.path.exists('VM_clean_word'):
    os.remove(os.getcwd() + '\VM_clean_word')
    print('Previous file removed!')
else:
    print('Does not exist the "VM_clean_word" file.')

f1 = open('VM_clean_word', 'x')
f1.write(VM_clean_word)

VM_word_list = re.split('\n', VM_clean_word)
del VM_word_list[-1]

print(VM_word_list)
