"""
    Created by Sang Kim date 19/12/2018
    Email: sangkimit@gmail.com
"""
# Thư viện cần thiết để xử lý
import numpy as np
from scipy.spatial import distance

import sort_image

#Load du lieu

'''
a = np.zeros((5,3))
b = (4,5,6)
a[0] = (1,2,3)
dst = distance.euclidean(a[0],b)
print(a[0])
print(dst)

ds = [["a",3],["b",1],["c",2]]
# Them 1 phan tu vao cuoi danh sach
ds.append(["d",5])

print(ds[0][1])

'''

X = np.load("dataset.npy")
#imquery = np.load("imquery.npy")

#print("X = ", X.shape)
#print('imquery = ', imquery.shape)

def danhsach(value,anhtruyvan):
	imquery = anhtruyvan
	# Cấu trúc tên tệp
	path = 'Corel/' # path den CSDL hình ảnh
	ids = range(0,10) # 10 noi dung khac nhau 
	numbers = 1
	surfix = '.jpg'

	# Thu tu phan tu trong ma tran

	i = 0

	ds = []
	# print(type(ds))

	#Tinh khoang cach voi anh truy van, va gan ten anh kem voi khoang cach den anh truy van
	for image_id in range(0,10):
		for number in range(0,100):
			fn = path +str(image_id)+"_"+str(numbers)+surfix
			numbers+=1

			# Tinh khoang cach Euclidean
			dst = distance.euclidean(imquery,X[i])
			# Tính khoảng cách Manhattan
			#dst = distance.cityblock(imquery,X[i])
			i+=1

			# Them phần tử gồm tên và khoảng cách đến ảnh truy vấn, vào danh sách
			ds.append([fn,dst])


	#print(ds)

	# Xap xep danh sach theo tang dan khoang cach

	ds_xapxep = sort_image.xapxep(ds)
	
	#print(ds_xapxep)


	ds_trave = ds_xapxep[:value]

	print(ds_trave[:value])

	return ds_trave



