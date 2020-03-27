# Lamba functionsare are simple 1-line functions, trying to save space and time
# Lambda functions are useful for higher order functions (functions taking other functions as input)


# classical function
def double(x):
    return x * 2


# same idea expressed as a lambda function (VSCode rewrites it though)
# double2 = lambda x: x * 2 will rework to:
def double2(x): return x * 2
