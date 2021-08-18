# 입력
# N : 문제의 개수, L : 현정이의 역량, K : 현정이가 대회중에 풀 수 있는 문제의 최대 개수
N, L, K = map(int, input().split())

easy, hard = 0,0

for i in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy +=1

# hard 문제
ans = min(hard, K) * 140

# easy 
if hard < K:
    ans += min(K-hard, easy) * 100

print(ans)