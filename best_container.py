a = [1, 8, 6, 2, 5, 4, 8, 3, 7]

def area(a):
    p1 = 0
    p2 = len(a) - 1
    max_area = 0
    for i in range(len(a)-1):
        current_area  = min(a[p1], a[p2]) * (p2-p1)
        max_area = max(max_area, current_area)

        if a[p1] < a[p2]:
            p1+=1
        else:
            p2-=1
    return max_area
answer = area(a)
print(answer)
