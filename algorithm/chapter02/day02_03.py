# 백준 문제번호 - 1157


words = input().upper() # applE -> APPLE
unique_words = list(set(words))  #aple

cnt_list = []
for x in unique_words : a  p  l  e
    cnt = words.count(x) #1211
    cnt_list.append(cnt) 
    # 1
    # 2
    # 1
    # 1

if cnt_list.count(max(cnt_list)) > 1 :
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list)) 
    print(unique_words[max_index])