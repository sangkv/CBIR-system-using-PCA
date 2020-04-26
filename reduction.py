"""
    Created by Sang Kim date 19/12/2018
    Email: sangkimit@gmail.com
"""
import numpy as np 
from scipy import misc # Thu vien cho load hinh anh
np.random.seed(1)

# Cấu trúc tên tệp
path = 'Corel/' # path den CSDL hình ảnh
ids = range(0,10) # 10 noi dung khac nhau 
numbers = 1
surfix = '.jpg'


# Kick thuoc du lieu
h = 187
w = 126
D = h * w *3 # chieu dai, chieu rong va mau RGB
N = 1000
K = 50

# Collect all data

X = np.zeros((D,N))
cnt = 0
for image_id in range(0,10):
	for number in range(0,100):
		fn = path +str(image_id)+"_"+str(numbers)+surfix
		numbers+=1
		
		"""
		# Kiểm tra ảnh đạt tiêu chuẩn chưa
		img = misc.imread(fn)
		print(fn)
		cnt+=1
		print(cnt,img.dtype, img.shape)
		temp = img.shape
		if temp != (126, 187, 3) and temp != (187, 126, 3):
			print("Stop")
			break
		"""
		
		X[:, cnt] = misc.imread(fn).reshape(D)
		cnt +=1


# Thực hiện PCA, Đào tạo mô hình học máy tương ứng với dữ liệu X
from sklearn.decomposition import PCA

pca = PCA(n_components = K) # K = 50
pca.fit(X.T)

# Dùng mô hình đã training này áp dụng với giảm chiều dữ liệu của X
X_new = pca.transform(X.T)

print("X_new.shape =",X_new.shape)


#U = pca.components_

# Luu tru CSDL dac trung
np.save("dataset", X_new)

# Lưu Model PCA
from joblib import dump, load
dump(pca, 'pca_model.joblib') 


