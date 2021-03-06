# -*- coding: utf-8 -*-
"""final code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ohranvGUIx9YNEou0DmIhRZohyUAHBqi
"""

import tensorflow as tf

# Commented out IPython magic to ensure Python compatibility.
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torch.utils.data as Data

import matplotlib.pyplot as plt
# %matplotlib inline

import numpy as np
import imageio


torch.manual_seed(1)    # reproducible

from google.colab import files
uploaded = files.upload()

import pandas as pd

x=torch.from_numpy(np.array(pd.read_csv('Book1.csv')))
y = torch.from_numpy(np.array(pd.read_csv('permeability.csv')))

print(len(x))

print(len(y))

# torch can only train on Variable, so convert them to Variable
x, y = Variable(x), Variable(y)
print(x.size())
print(y.size())



# this is one way to define a network
class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)   # hidden layer
        self.predict = torch.nn.Linear(n_hidden, n_output)   # output layer

    def forward(self, x):
        x = F.relu(self.hidden(x))      # activation function for hidden layer
        x = self.predict(x)             # linear output
        return x

net = Net(n_feature=11, n_hidden=1, n_output=1)     # define the network
# print(net)  # net architecture
optimizer = torch.optim.SGD(net.parameters(), lr=0.2)
loss_func = torch.nn.MSELoss()  # this is for regression mean squared loss



# train the network
for t in range(200):
  
    prediction = net(x.float())     # input x and predict based on x

    loss = loss_func(prediction, y.float())     # must be (1. nn output, 2. target)

    optimizer.zero_grad()   # clear gradients for next train
    loss.backward()         # backpropagation, compute gradients
    optimizer.step()        # apply gradients

import pandas as pd

from google.colab import files
uploaded = files.upload()

df = pd.read_csv("Book1H.csv")

df.shape

#import pandas as pd

x1=torch.from_numpy(np.array(pd.read_csv('HF1.csv')))
#y = torch.from_numpy(np.array(pd.read_csv('permeability.csv')))

prediction = net(x[0].float()) 
print(prediction)



prediction = net(x1.float()) 
print(prediction)





#########################################################################################

from google.colab import files
uploaded = files.upload()

from google.colab import files
uploaded = files.upload()

df1=pd.read_csv("Book1.csv")
df2= pd.read_csv("permeability.csv")
df3=pd.read_csv("Book2.csv")

import numpy as np
import pandas as pd
import keras
import keras.backend as kb
import tensorflow as tf

model = keras.Sequential([
    keras.layers.Dense(32, activation=tf.nn.relu, input_shape=[7]),
    keras.layers.Dense(32, activation=tf.nn.relu),
    keras.layers.Dense(32, activation=tf.nn.relu),
    keras.layers.Dense(1)
  ])

optimizer = tf.keras.optimizers.RMSprop(0.0099)
model.compile(loss='mean_squared_error',optimizer='adam')
model.fit(df1,df2,epochs=500)

model.predict([df3])

