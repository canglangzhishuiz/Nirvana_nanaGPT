import torch

print(torch.__version__)
print(torch.cuda.is_available())
# .manual_seed():设置CPU随机种子，用来保证cpu产生的随机数一致
torch.manual_seed(1034)
print(torch.rand(1))
# .randint(low, high, size):返回一个填充了随机整数的张量，这些整数在low(默认为0)和high之间均匀生成。
# 张量的shape由变量参数size定义
b = torch.randint(1000, size=(128,))
print(b)
print(len(b), b.shape)
# 初始化指定维度的张量
c = torch.rand(1000)
print(c[5:50])







