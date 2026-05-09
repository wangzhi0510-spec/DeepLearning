"""
案例:
    演示张量常用的运算函数.
涉及到的 API(函数) 如下:
    sum(), max(), min(), mean()                     -> 都有 dim 参数, 0表示列, 1表示行
    pow(), sqrt(), exp(), log(), log2(), log10()    -> 没有dim参数
掌握的函数:
    sum(), max(), min(), mean()
"""

import torch

if __name__ == '__main__':
    torch.random.manual_seed(1)
    t=torch.randint(20,50,size=(3,4))
    print(t)

    print(t.sum()) #整 体 求和
    print(t.sum(dim=0))# 按 列 求和
    print(t.sum(dim=1))# 按 行 求和
