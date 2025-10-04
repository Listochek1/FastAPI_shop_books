# def func(input_func):
#     def output_func():
#         print("***************")
#         input_func()
#         print("***************")
#     return output_func

# @func
# def hello():
#     print("Hello World")




# def decorator_with_args(func):
#     def wrapper(**kwargs):
        
#         print("_______________________")
#         func(kwargs)
#         print("_______________________")
#     return wrapper

# @decorator_with_args
# def greet(greeting):
#     for i in greeting.keys():
#         print(type(i))
#         print(i)
#     print(greeting.keys())
    

# greet(zalupa="Hi",wat="pidor",wathuesos="huesos")





class Mynumbers:
    def __init__(self,max):
        self.max = max
        self.num = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num >= self.max:
            raise StopIteration
        else:
            self.num +=2
            return self.num
        


# clss = Mynumbers(10)

# for i in clss:
#     print(i)


# def generator(start = 0):
#     current = start
#     while True:
#         current+=1
#         yield current
# gen = generator()
# for i in range(5):
#     print(next(gen))