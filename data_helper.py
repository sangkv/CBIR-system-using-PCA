"""
    Created by Sang Kim date 19/12/2018
    Email: sangkimit@gmail.com
"""
import os
import traceback
import numpy as np
from scipy.misc import imread, imsave, imresize


def read_image(img_path, mode):
    img = imread(img_path, mode=mode)
    img = resize_image(img)
    arr = np.array(img)
    arr = arr.flatten()
    return arr


def read_data(folders, mode='RGB'):
    paths = []
    datas = []
    labels = []
    for folder in folders:
        for file in os.listdir(folder):
            if not file.endswith('.jpg'):
                continue
            arr = read_image(os.path.join(folder, file), mode=mode)
            datas.append(arr)
            paths.append(os.path.join(folder, file))
            labels.append(int(file.split('_')[0]))
    datas = np.array(datas)
    labels = np.array(labels)
    return datas, labels, paths


def resize_image(img):
    if img.shape[0] > img.shape[1]:
        img = imresize(img, (187, 126))
    else:
        img = imresize(img, (126, 187))
    return img


def resize_images(data_folder, output_folder, gray=False):
    for file in os.listdir(data_folder):
        try:
            if not file.endswith('.jpg'):
                continue
            if gray:
                img = imread(os.path.join(data_folder, file), mode='L')
            else:
                img = imread(os.path.join(data_folder, file), mode='RGB')
            img = resize_image(img)
            imsave(os.path.join(output_folder, file), img)
        except:
            print(file)
            traceback.print_exc()
            pass


def data_separate(data_folder, output_folder):
    for file in os.listdir(data_folder):
        src_path = os.path.join(data_folder, file)
        des_dir = os.path.join(output_folder, file.split('_')[0])
        if not os.path.exists(des_dir):
            os.mkdir(des_dir)
        os.rename(src_path, os.path.join(des_dir, file))


def train_test_split(data_folder, test_folder):
    if not os.path.exists(test_folder):
        os.mkdir(test_folder)
    for folder in os.listdir(data_folder):
        dst = os.path.join(test_folder, folder)
        os.mkdir(dst)
        folder = os.path.join(data_folder, folder)
        for file in os.listdir(folder)[:20]:
            os.rename(os.path.join(folder, file), os.path.join(dst, file))


if __name__ == '__main__':
    ###- Prepocess and generate RGB image -###
    resize_images('data/raw_data', 'data/temp', False) # Tôi Đã sử dụng cái này
    # data_separate('data/temp', 'data/train')

    ###- Prepocess and generate gray image -###
    # resize_images('raw_data', 'temp', True)
    # data_separate('data/temp', 'data/gray_image')
    # # Remove temp folder
    # os.rmdir('data/temp')

    ###- Split rbg image to train and test -###
    train_test_split('data/train', 'data/test')

    # Rename folder as what you want :))
