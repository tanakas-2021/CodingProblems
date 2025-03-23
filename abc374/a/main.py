import itertools

def get_department_patterns(N):
    """
    1以上N-1個以上の部署を取得するパターンをすべて取得する関数

    Args:
        N (int): 部署数

    Returns:
        list: 部署の組み合わせのリスト
    """

    departments = [i for i in range(N)]
    patterns = []

    for i in range(1, N):
        for pattern in itertools.combinations(departments, i):
            patterns.append(list(pattern))

    return patterns

N = int(input())
K = list(map(int, input().split()))
total_emp = sum(K)
ans = (10 ** 8) * 20

patterns = get_department_patterns(N)
for pattern in patterns:
    max_n_group = 0
    n_a_group = 0
    for i in pattern:
        n_a_group += K[i]
    n_b_group = total_emp - n_a_group
    max_n_group = max(n_a_group,n_b_group)
    ans = min(ans,max_n_group)

print(ans)

        
