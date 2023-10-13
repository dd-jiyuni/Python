st = 'Programming'

# 자음이 나타나는 동안만 출력하는 기능
for ch in st:
    if ch in ['a','e','i','o','u']:
        break # 탈출!
    #   continue 일 경우 자음을 제외한 나머지가 모두 출력됨.
    print(ch)

print('THE END')
