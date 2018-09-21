# askdjango 데코레이션 편 연습문제 풀이

def myfilter(filter_fn, alter_value):
    def wrap(fn):
        def inner(*args):
            args2 = [i if filter_fn(i) else alter_value for i in args]
            return fn(*args2) # 패킹
        return inner
    return wrap


@myfilter(lambda i: i%2==0, 0)
def mysum(a,b,c,d,e):
    return a+b+c+d+e


@myfilter(lambda i: i%2==0, 1)
def mymultiply(a,b,c,d,e):
    return a+b+c+d+e


print(mysum(1,2,3,4,5))
print(mymultiply(1,2,3,4,5))