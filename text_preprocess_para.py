import re
import os

f = open("VM.txt")
VM_origin = f.read()
f.close()

VM_1 = re.compile(r'<\$>').sub('\n', VM_origin)
VM_2 = re.compile(r'<[^>]+>').sub('', VM_1)
VM_3 = re.compile(r' ').sub('', VM_2)
VM_4 = re.compile(r'\n\n\n').sub('\n\n', VM_3)
VM_5 = re.compile(r'#+\n').sub('', VM_4)
VM_6 = re.compile(r'#.+\n').sub('', VM_5)
VM_7 = re.compile(r'\.').sub(' ', VM_6)
VM_8 = re.compile(r'[a-z]\n').sub('', VM_7)
VM_9 = re.compile(r'\n\n').sub('\n', VM_8)

VM_clean_para = VM_9

# print(VM_clean_para)

if os.path.exists('VM_clean_para'):
    os.remove(os.getcwd() + '\VM_clean_para')
    print('Previous file removed!')
else:
    print('Does not exist the "VM_clean_para" file.')

f1 = open('VM_clean_para', 'x')
f1.write(VM_clean_para)

VM_para_list = re.split('\n', VM_clean_para)
del VM_para_list[0]
del VM_para_list[-1]

print(VM_para_list)


