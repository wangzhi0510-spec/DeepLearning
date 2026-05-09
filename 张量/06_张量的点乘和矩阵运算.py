"""
案例:
    演示张量的点乘 和 矩阵乘法操作.

点乘:
    要求: 两个张量的维度保持一致, 对应元素直接做 乘法操作.
    API:
        t1 * t2
        t1.mul(t2)          # multiply: 乘法

矩阵乘法:
    要求: 两个张量, 第一个张量 的列数, 等于 第二个张量 的行数(A列 = B行)
    结果: A行B列
    API:
        t1 @ t2
        t1.matmul(t2)
        t1.dot(t2)          扩展: 只针对于一维张量有效.
        两个形状相同的一维张量，dot计算他们对应位置相乘之和
"""

import torch

if __name__ == '__main__':
    t=torch.tensor([[1.,2.,3.],[4.,5.,6.]])
    print(t)
    tt=torch.tensor([[1.,2.,3.],[4.,5.,6.]])

    ttt=torch.tensor([[1.,2.],[4.,5.],[6.,7.]])

    #点乘
    t1=t*tt
    print(t1)

    #矩阵相乘
    t2=t @ ttt
    print(t2)


    t4 = torch.tensor([1, 2, 3])
    t5 = torch.tensor([4, 5, 6])
    t6 = t4.dot(t5)
    print(f't6: {t6}')
