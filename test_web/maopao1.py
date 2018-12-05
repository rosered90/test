import random


def bubblesort(target):
	length = len(target)
	for i in range(length - 1):
		for j in range(length - 1 - i):
			if target[j] > target[j + 1]:
				target[j], target[j + 1] = target[j + 1], target[j]
	return target


if __name__ == '__main__':
	a = [random.randint(1, 1000) for i in range(100)]
	print(bubblesort(a))

# a = [10,8,4,7,5]
# print(bubblesort(a))
