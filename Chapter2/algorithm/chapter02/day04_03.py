# 백준 문제번호 - 2805

N, M = map(int, input().split())                # N: 나무 수 / M: 필요한 나무 길이
tree = list(map(int, input().split()))          # tree : 나무 높이
start, end = 1, max(tree)                       # 이분탐색 검색 범위 설정

while start <= end:                             # 적절한 벌목 높이를 찾는 알고리즘
    mid = (start + end) // 2                   
    
    log = 0                                     

    for i in tree:
        if i > mid:
            log += i - mid                      # log = log + i - mid
                                            
    # 벌목 높이를 이분탐색
    if log >= M:                             
        start = mid + 1
    else:
        end = mid - 1

print(end)