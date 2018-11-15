# 算法的概述
# 算法是计算机处理信息的本质,因为计算机程序本质上是一个算法来
# 告诉计算机确切的步骤来执行一个指定的任务,一般地,当算法在处理信息时
# 会从输入设备或数据的存储地址读取数据,把结果写入输出设备或
# 某个存储地址供以后再调用

# 算法是独立存在的一种解决问题的方法和思想

# 算法的五大特征
# 1.输入: 算法具有0个或多个输入
# 2.输出: 算法至少有1个或多个输出
# 3.有穷性: 算法在有限的步骤之后会自动结束而不会无限循环
#           并且每一个步骤可以在可接受的时间内完成
# 4.确定性: 算法中的每一步都有确定的含义,不会出现二义性
# 5.可行性: 算法的每一步都是可行的,也就是说每一步都能够执行有限的次数完成






# 如题: a + b + c = 1000, 且a^2 + b^2 = c^2(a,b,c为自然数)
# 如何求出所有a, b, c可能的组合?
# 笨办法
# import time


# start_time = time.time()

# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
#                 print(a, b, c)

# end_time = time.time()
# print(end_time-start_time)
# 运行时间200秒


# 引入算法
# import time


# start_time = time.time()

# for a in range(0, 1001):
#     for b in range(0, 1001):
#         c = 1000 - a - b
#         if a ** 2 + b ** 2 == c**2:
#             print(a, b, c)

# end_time = time.time()
# print(end_time-start_time)
# 运行时间2秒
