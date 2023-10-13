n = 7
# reversed : 내장형 함수인데 list를 역정렬해줌.
for i in reversed(range(n)):
    st = ''
    for j in range(i):
        st = st + ' '
    print(st + '#')

# 방법 2
# for i in range(n):
#     st = ''
#     for j in range (n-(i+1)):
#         st = st + ' '
#     print(st + '#')