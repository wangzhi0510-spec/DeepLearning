
import torch

def damo():
    #创建全1张量
    t1=torch.ones(2,3)
    print(t1)
    print('-'*30)

    #根据一个张量形状创建一个相同形状全1张量
    t_test=torch.tensor([[1,2,3],[4,5,6],[7,8,9]],dtype=torch.float)
    print(t_test)
    print('-'*30)

    t2=torch.ones_like(t_test)
    print(t2)
    print('-'*30)

def damo1():


    # 创建全0张量
    t1 = torch.zeros(2, 3)
    print(t1)
    print('-'*30)

    # 根据一个张量形状创建一个相同形状全0张量
    t_test = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(t_test)
    print('-'*30)

    t2 = torch.zeros_like(t_test)
    print(t2)
    print('-'*30)

def damo2():
    # 根据指定值创建全10张量
    t1 = torch.full(size=(2, 3), fill_value=10)
    print(t1)
    print('-'*30)

    # 根据一个张量形状创建一个相同形状全指定值张量
    t_test = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(t_test)
    print('-'*30)

    t2 = torch.full_like(input=t_test, fill_value=10)
    print(t2)


if __name__ == '__main__':
    damo()
    damo1()
    damo2()