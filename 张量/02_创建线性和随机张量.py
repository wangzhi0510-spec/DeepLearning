
import torch

def damo01():
    #创建随机种子，固定随机数据
    torch.manual_seed(20)
    #查看随机种子
    print(torch.initial_seed())


    #创建均匀分布在(0,1)之间的随机张量
    t1=torch.rand(2,3)
    print(type(t1))
    print(t1)

    #创建随机整数张量
    #参数 [low 最小值 high 最大值) size 形状
    tt=torch.randint(0,10,(2,3))
    print(type(tt))
    print(tt)

    #创建符合正态分布的随机张量
    t2=torch.randn(2,3)
    print(type(t2))
    print(t2)

    #创建线性张量
    #按指定步长创建
    #参数解释[start 开始,end 结束),step 步长,dtype 数据类型
    t3=torch.arange(start=0,end=11,step=2,dtype=torch.float32)
    print(type(t3))
    print(t3)

    #按指定数量创建[start 开始,end 结束],steps 元素个数,dtype 数据类型
    t4=torch.linspace(start=0,end=11,steps=4,dtype=torch.float32)
    print(type(t4))
    print(t4)



if __name__ == '__main__':
    damo01()