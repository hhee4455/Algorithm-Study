def function(i):
    if i <= 0:  # 종료 조건: i가 0 이하이면 종료
        return
    for j in range(i):
        print("재귀함수", j, "번째 입니다.")
        function(i-1)  # i를 감소시켜 재귀 호출
i = int(input())
function(i)