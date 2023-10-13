n = 5

for i in range(n):
    # 역순 반복
    for j in range(n - (i + 1)):
        print(' ', end = '')
    # 홀수
    for j in range(2 * i + 1):
        print('+', end = '')
    print()

# 다른 방법
# for i in range(n):
#     print(' ' * (n - (i + 1)), end = '')
#     print('+' * (2 * i + 1))

# 출력 결과
#     +
#    +++
#   +++++
#  +++++++
# +++++++++


