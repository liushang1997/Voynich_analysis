import re
import os

f = open('VM_clean_word')
VM_word = f.read()
VM_letter_con = re.compile(r'\n').sub('', VM_word)
# print(VM_letter_con)

if os.path.exists('VM_letter_count'):
    os.remove(os.getcwd() + '\VM_letter_count')
    print('Previous file removed!')
else:
    print('Does not exist the "VM_letter_count" file.')

f1 = open('VM_letter_count', 'x')

# res = {}
# for i in VM_letter_con:
#     res[i] = VM_letter_con.count(i)
# print(res)

for i in range(26):
    f1.write(chr(i + ord('a')) + '\t' + str(VM_letter_con.count(chr(i + ord('a')))) + '\n')
f1.write('?' + '\t' + str(VM_letter_con.count('?')) + '\n')


