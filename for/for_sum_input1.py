n = int(input('합계를 구할 수를 입력하시오 : '))

s = 0

for i in range(0,n):
    s = s + (i+1)

print('1부터 {}까지의 합은 {}'.format(n,s))
