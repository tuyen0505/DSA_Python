def main():
    t: int = int(input())
    for _ in range(t):
        n: int = int(input())
        ls: list = list(map(int, input().split()))
        ans = [1] * n
        for i in range(1, n):
            for j in range(i):
                if ls[j] < ls[i] and ans[i] <= ans[j]:
                    ans[i] = ans[j] + 1
        print(n - max(ans))

main()