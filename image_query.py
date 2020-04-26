"""
    Created by Sang Kim date 19/12/2018
    Email: sangkimit@gmail.com
"""
# Cac thu vien can su dung
import numpy as np 
from scipy.misc import imread, imresize, imsave
# from sklearn.decomposition import PCA 		# Load model da luu nen khong can thu vien nay nua
np.random.seed(1)


#Load model
from joblib import dump, load
pca = load('pca_model.joblib') 


def imquery(path):
	# Kick thuoc du lieu
	h = 187
	w = 126
	D = h * w *3 # chieu dai, chieu rong va mau RGB
	N = 1
	K = 50

	# Tao mot mang 2 chieu
	x= np.zeros((D,N))
	x[:, 0] = imread(path).reshape(D)
	# su dung PCA trich xuat dac trung giam chieu du lieu
	#pca = PCA(n_components = K) # K = 50
	x_new = pca.transform(x.T)
	
	print("x_new.shape = ",x_new.shape)

	# Định lưu lại vector đặc trưng ảnh truy vấn, khi dùng thì load nên, nhưng thực sự không cần thiết như thế
	#np.save("imquery",x_new)

	# sau khi su dung PCA dao chieu lai matran
	#v = pca.components_
	#np.save("image_query",v)
	#return v
	return x_new


	
