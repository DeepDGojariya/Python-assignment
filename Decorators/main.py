from time import time

def calculate_time(func):
    def wrapper(*args,**kwargs):
        start_time = time()
        func(*args,**kwargs)
        end_time = time()
        print("Function {0} executed in {1:.4f} seconds".format(func.__name__,(end_time-start_time)))
    return wrapper

@calculate_time
def simple_func(n):
    [[(i**2) for j in range(n) for i in range(1,500)]]

if __name__ == '__main__':
    simple_func(500)
