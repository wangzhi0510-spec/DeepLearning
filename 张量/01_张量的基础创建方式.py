
import torch
import numpy as np


def damo1():
    #张量的两种创建方式 tensor Tensor
    #创建矢量张量
    t1=torch.tensor(1)
    print(type(t1))
    print(t1)
    print('-'*30)

    #二维列表转换成张量
    data=[[1,2,3],[4,5,6]]
    print(type(data))
    t2=torch.tensor(data)
    print(type(t2))
    print(t2)
    print('-'*30)

    #numpy np数组转换成张量
    np1=np.random.randint(1,10,size=(2,3))
    print(type(np1))
    t3=torch.tensor(np1,dtype=torch.float)
    print(type(t3))
    print(t3)
    print('-'*30)

    #Tensor 创建2行3列的张量
    t4=torch.Tensor(2,3)
    print(type(t4))
    print(t4)
    print('-'*30)

    #IntTensor
    t5=torch.IntTensor(2,3)
    print(type(t5))
    print(t5)


if __name__ == '__main__':
    damo1()