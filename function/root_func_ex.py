radius = 10


def circle_area_circum(radius):
    area = 3.14 * radius ** 2
    circum = 2 * 3.14 * radius
    print('반지름 {} 인 원의 면적은 {:.1f}, 원의 둘레는 {:.1f}'.format(radius, area, circum))


circle_area_circum(radius)
