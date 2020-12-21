def add_(x):
    return x+1


def add_one(func, x):
    
    return 1+add_(x)

y = add_
print(add_one(y,3))

def add_2(x):
	return x+1