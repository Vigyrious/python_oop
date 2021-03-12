class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        with open("result.txt","r") as f:
            last_edit = f.readlines()
        with open("result.txt","w") as f:
            current = f"Function {self.func.__name__} was called. Result: {self.func(*args)}\n"
            last_edit.append(current)
            f.writelines(last_edit)





@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
