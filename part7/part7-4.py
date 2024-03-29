'''
파라메트릭 서치(Parametric search)
- 최적화 문제를 결정 문제(yes or no)로 바꾸어 해결하는 기법
- 이진 탐색 기법을 사용하여 해결

떡볶이 떡 만들기
- 최소 m 만큼의 떡을 가져갈 수 있도록 자르는 높이 h를 지정해야 함
- ex) 떡 길이가 19이고 자르는 높이가 16이면 3 만큼의 떡을 가져갈 수 있음 but 떡 길이가 자르는 높이보다 낮으면 잘리지 않음
'''
n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
'''
start = arr[-1]
while True:
    start -= 1
    tmp = sum([max(0, i - start) for i in arr])
    if tmp >= m:
        print(start)
        break
'''
start, end = arr[0], arr[-1]
ans = 0
while start <= end:
    mid = (start + end) // 2
    tmp = sum([max(0, i - mid) for i in arr])
    if tmp < m:
        end = mid - 1
    elif tmp >= m:
        start = mid + 1
print(mid)
