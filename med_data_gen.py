import numpy as np
import matplotlib.pyplot as plt
from skimage import measure
from medtools import *
from skimage.morphology import erosion, dilation, opening, closing, white_tophat
from skimage.morphology import disk
from scipy import ndimage
import math



# a = np.array([[0,0,1,0,0],
# 	          [0,0,2,0,0],
# 	          [0,0,3,0,0],
# 	          [0,1,4,1,0],
# 	          [0,0,5,0,0]])

# a = np.delete(a, [0,2,4], 0)




label = np.load('../data/labels.npy').astype(np.int32)
data = np.load('../data/datas.npy').astype(np.float32)
print "The total number of training data is:"
print data.shape

data,label = remove_empty_label(data,label)
print data.shape



d_train = data[6,:,:,0]
l_train = label[6,:,:,0]

# d_test = data[11,:,:,0]
# l_test = label[11,:,:,0]
 
print d_train.shape
print l_train.shape


SDMmap_corp_norm_train, SDM_vec_train = get_SDMmap(l_train)
dialited_label_mask = generate_mask(l_train,offset = 15)
SDMmap_corp_gradient = get_gradient_SDMmap(SDMmap_corp_norm_train)
SDMmap_vec_gradient = get_gradient_SDMmap(SDM_vec_train)

# plt.imshow(SDMmap_gradient,cmap = 'gray',interpolation = 'nearest')
# plt.show()

points_list =  iterate_mask(dialited_label_mask)
test_patch, test_vecs = corp_accdTo_mask(d_train,SDMmap_corp_gradient,SDMmap_vec_gradient,points_list) # negatative Y toward norm!!!!!!!



# plt.imshow(test_patch[101,:,:],cmap = 'gray',interpolation = 'nearest')
# plt.show()
# print test_vecs[101]
# print "---------"
# print test_patch.shape
# print test_vecs.shape


np.save('../data/patches_SDM_train.npy', test_patch)
np.save('../data/vecs_SDM_train.npy', test_vecs)



















































# FIRST DIREVITIVE !!!

# selem = disk(e)
# dilated_train = dilation(l_train, selem)
# dilated_test = dilation(l_test, selem)

# dd_train = ndimage.binary_fill_holes(dilated_train).astype(int)
# dd_test = ndimage.binary_fill_holes(dilated_test).astype(int)

# contours_train = measure.find_contours(dd_train, 0.8)
# contours_test = measure.find_contours(dd_test, 0.8)

# cc_train = np.array(contours_train)
# cc_train = cc_train[0,:,:]

# cc_test = np.array(contours_test)
# cc_test = cc_test[0,:,:]



# keep_index_train = []
# for i in range(0,len(cc_train),30):
#   keep_index_train.append(i)

# keep_index_test = []
# for i in range(0,len(cc_test),30):
#   keep_index_test.append(i)
    
# # a = np.delete(cc,del_index,0)
# a_train = cc_train[keep_index_train]
# a_test = cc_test[keep_index_test]


# ini_m_train = PtToMap(a_train,size = l_train.shape)
# ini_m_test = PtToMap(a_test,size = l_test.shape)

# norm_train = get_norm_by_spline_first_derivitive(list(a_train))
# norm_test = get_norm_by_spline_first_derivitive(list(a_test))

# an_train = normToAngel(norm_train)
# an_test = normToAngel(norm_test)

# dd_train = get_vecF_from_label_relative(list(a_train),l_train,an_train)
# dd_test = get_vecF_from_label_relative(list(a_test),l_test,an_test)



# patch_l_train = []
# for i,j in zip(a_train,an_train):
#   x,y = i
#   pat = corp(d_train,j,x,y,patch_size)
#   patch_l_train.append(pat)

# patch_l_test = []
# for i,j in zip(a_test,an_test):
#   x,y = i
#   pat = corp(d_test,j,x,y,patch_size)
#   patch_l_test.append(pat)

# patchs_train = np.array(patch_l_train)
# distances_train = np.array(dd_train)

# patchs_test = np.array(patch_l_test)
# distances_test = np.array(dd_test)

# # np.save('patches_train.npy', patchs_train)
# # np.save('vecs_train.npy', distances_train)

# # np.save('patches_test.npy', patchs_test)
# # np.save('vecs_test.npy', distances_test)


# update_vecs = np.load('results.npy').astype(np.float32)
# update_vecs = np.array([[0,1],
# 	                    [1,0]])
# update_an = np.array([90,90])




# corrected_vec = rotate_vectors(dd_test,an_test)
# corrected_vec = rotate_vectors(update_vecs,an_test)
# # print corrected_vec
# new_pos = a_test - corrected_vec

# new_m_test=PtToMap(new_pos,size = l_test.shape)


# plt.imshow(l_test + ini_m_test + new_m_test,cmap = 'gray',interpolation = 'nearest')
# plt.show()




