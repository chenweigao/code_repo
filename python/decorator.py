from functools import wraps


def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction1():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction1


# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

# a_function_requiring_decoration()

@a_new_decorator
def a_function_requiring_decoration():
    print("this is func using decoration!")


a_function_requiring_decoration()

print(a_function_requiring_decoration.__name__)
