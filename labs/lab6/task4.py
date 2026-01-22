def add_matrices(n, m1, m2):
    if n < 2:
        return "Error!"
    res = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(m1[i][j] + m2[i][j])
        res.append(row)
    return res

n = int(input())
if n < 2:
    print("Error!")
else:
    m1 = [list(map(int, input().split())) for _ in range(n)]
    m2 = [list(map(int, input().split())) for _ in range(n)]
    result = add_matrices(n, m1, m2)
    if result != "Error!":
        for r in result:
            print(" ".join(map(str, r)))
    else:
        print("Error!")