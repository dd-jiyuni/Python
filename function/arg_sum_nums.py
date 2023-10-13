def sum_nums(*numbers):
    sum_result = 0
    average = 0
    for n in numbers:
        sum_result += n
        average = sum_result / len(numbers)
    print(len(numbers), '개의 인자', numbers)
    return sum_result, average

# 튜플 -> 리스트로 변환 시켜놓고 인덱스 번호로 출력
sum_list = list(sum_nums(10, 20, 30))
print('합계 :', sum_list[0], ', 평균 :', sum_list[1])

sum_list = list(sum_nums(10, 20, 30, 40, 50))
print('합계 :', sum_list[0], ', 평균 :', sum_list[1])
