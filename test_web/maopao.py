import random


def bubblesort(target):
    length = len(target)
    while length > 0:
        length -= 1
        cur = 0
        while cur < length: #拿到当前元素
            if target[cur] < target[cur + 1]:
                target[cur], target[cur + 1] = target[cur + 1], target[cur]
            cur += 1
    return target
if __name__ == '__main__':
    a = [random.randint(1,1000) for i in range(100)]
    print (bubblesort(a))


# bubblesort(45,56,34,34,23,23,67,9,0,4,2,123,45,21,13,23)