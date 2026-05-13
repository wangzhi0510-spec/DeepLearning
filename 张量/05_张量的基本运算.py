"""
案例:
    演示张量的基本运算.

涉及到的API:
    add(), sub(), mul(), div(), neg()       -> 加减乘除, 取反, substract, multiply, divide
    add_(), sub_(), mul_(), div_(), neg_()  -> 功能同上, 只不过可以修改源数据, 类似于 Pandas部分的 inplace = True

需要你记忆的:
    1. 可以用 +, -, *, / 符号来替代 上述的 加减乘除函数.
    2. 如果是张量 和 数值运算, 则: 该数值会和张量中的每个值依次进行 对应的运算.
"""


import torch


if __name__ == '__main__':

    #创建张量
    t=torch.Tensor([[1,2,3],[4,5,6],[7,8,9]])

    #加法
    t2=t.add(2)
    print(t2)
    #改变原数据，
    t2.add_(3) #==  t2+=3
    print(t2)
    t3=t+2
    print(t3)



