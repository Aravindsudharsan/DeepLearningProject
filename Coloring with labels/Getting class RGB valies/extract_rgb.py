import os
import glob
import numpy as np
import scipy.io
import scipy.misc

data_path="D:\\Academics\\UCSB\\Spring 2018\\ECE194N Deep Learning\\Project\\101_ObjectCategories\\"
f=os.listdir(data_path)
for folder_path_ in f:
    folder_path=''
    folder_path=data_path+str(folder_path_)+'\\*.jpg'  
    count=0
    dict={}
    r_sum,g_sum,b_sum=0,0,0
    for image_path in glob.glob(folder_path): #Access each image path from the folder
        count=count+1
        for image in glob.glob(image_path): #Read each image from the image path
            img=scipy.misc.imresize(scipy.misc.imread(image).astype(np.float),[128,128,3]) #Read image as flot values
            if(np.shape(img)==(128,128)):
                img1=np.ones((128,128,3))
                img1[:,:,0],img1[:,:,1],img1[:,:,2]=img,img,img
                img=img1
            r,g,b=0,0,0
            for i in range(128):
                for j in range(128):
                    r,g,b=r+img[i][j][0],g+img[i][j][1],b+img[i][j][2]
        
            r,g,b=r/(128*128),g/(128*128),b/(128*128)
        r_sum,g_sum,b_sum=r_sum+r,g_sum+g,b_sum+b
    
    category=folder_path.split("\\")[7]
    r_avg,g_avg,b_avg=r_sum/count,g_sum/count,b_sum/count
    count=0
    dict.update({category:(r_avg,g_avg,b_avg)})
    print(dict)

    


