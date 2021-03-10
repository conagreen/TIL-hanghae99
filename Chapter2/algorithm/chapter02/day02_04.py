# 백준 문제번호 - 2941

a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
b = input()
for i in a:
    b = b.replace(i, " ")
print(len(b)) 