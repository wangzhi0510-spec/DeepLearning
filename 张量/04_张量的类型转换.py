
import torch

def damo():
    t1 = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]],dtype=torch.int64)
    print(t1)
    print('-'*30)

    t2=t1.type(torch.float64)
    print(t2)

    print('-'*30)

    t3=t2.half()
    print(t3)
    print('-'*30)


if __name__ == '__main__':
    damo()