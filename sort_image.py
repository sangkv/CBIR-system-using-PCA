"""
    Created by Sang Kim date 19/12/2018
    Email: sangkimit@gmail.com
"""
# Xap xep danh sach theo thu tu tang dan khoang cach
# Để đơn giản ta lựa chọn thuật toán: Selection sort

def xapxep(ds):
	for i in range(0,999):
		for j in range(i+1,1000):
			if ds[i][1] > ds[j][1]:
				temp = ds[i]
				ds[i] = ds[j]
				ds[j] = temp

	return ds

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)