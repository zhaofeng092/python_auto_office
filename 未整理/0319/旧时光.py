# -*- coding: UTF-8 -*-
# 公众号  ：  技术TA说
# 代码作者  ：  看门大叔
# 创建时间  ：  2020/3/19  20:16
# 文件名称  :  旧时光.py
# 开发工具  :  PyCharm
#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tensorflow as tf


# In[3]:


print("tensorflow version:{}".format(tf.__version__))


# In[4]:


import pandas as pd


# In[5]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import glob
import os


# In[6]:


from tensorflow import keras


# In[7]:


train_image_path=glob.glob('D:/train/*/*.jpg')


# In[8]:


len(train_image_path)


# In[9]:


train_image_path[-5:]





train_image_path[:6]


# In[11]:


p='D:/train\\test1\\9995.jpg'


# In[12]:


p.split('\\')[1]





int(p.split('\\')[1]=='cat')


# In[14]:


train_image_label=[int(p.split('\\')[1]=='cat')for p in train_image_path]


# In[15]:


train_image_label[:5]


# In[16]:


train_image_label[-5:]


# In[17]:


def load_preprosess_image(path,labei):
    image=tf.io.read_file(path)
    image=tf.image.decode_jpeg(image,channe1s=3)
    image=tf,image.resize(image,[256,256])
    image=tf.cast(image,tf.float32)
    image=image/255
    label=tf.reshape(labei,[1])
    return image,label


# In[18]:


#[[1],[2],[3]]


# In[19]:


#tf.image.convert_image_dtype


# In[20]:


train_image_ds=tf.data.Dataset.from_tensor_slices((train_image_path,train_image_label))


# In[21]:


AUTOTUNE=tf.data.experimental.AUTOTUNE


# In[22]:


train_image_ds=train_image_ds.map(load_preprosess_image,num_parallel_calls=AUTOTUNE)


# In[23]:


train_image_ds


# In[24]:


BATCH_SIZE=16
train_count=len(train_image_path)


# In[25]:


train_image_ds=train_image_ds.shuffle(train_count).batch(BATCH_SIZE)
train_image_ds=train_image_ds.prefetch(AUTOTUNE)


# In[26]:


imgs,labels=next(iter(train_image_ds))


# In[27]:


imgs.shape


# In[28]:


labels.shape


# In[29]:


imgs[0]


# In[30]:


plt.imshow(imgs[0])


# In[31]:


labels[0]


# In[ ]:




