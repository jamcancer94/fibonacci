# coding:utf-8
import time
'''
斐波那契数列
1,1,2,3,5,8,13,21...
'''


# 1 普通版
# 40项 cost:38.43s
def fib1(n):
    if n in [1, 2]:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


# 2 缓存版
# 1000项 0.29s
# 1000+ RuntimeError: maximum recursion depth exceeded
def fib2(n, cache={}):
    # 注释后没有递归限制，20000项6.31s， 10000,0.77s
    # if cache is None:
    #     cache = {}
    if n in cache:
        return cache[n]
    if n in [1, 2]:
        return 1
    else:
        cache[n] = fib2(n-1, cache) + fib2(n-2, cache)
        return cache[n]


# 3 多元赋值
# 1000 0.06s
# 3000 0.53s
# 10000 10s
def fib3(n):
    a = b = 1
    while(n):
        a, b, n = b, a + b, n-1
    return a

# 4 生成器
# 1000 0.01s
# 10000 0.79s
def fib4():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    start_time = time.time()
    print [fib2(x) for x in range(1, 10000)]
    # print fib2(1000)
    # p = fib4()
    # print [p.next() for i in range(10000)]
    end_time = time.time()
    print 'cost:%.2fs' % (end_time-start_time)
