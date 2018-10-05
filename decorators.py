# Function decorators are simply wrappers to existing functions.
# In general, decorators are ideal for extending the behavior of
# functions that we don't want to modify


def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)


def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper


my_get_text = p_decorate(get_text)
print(my_get_text("John"))


# To decorate get_text we don't have to get_text = p_decorator(get_text).
# There is a neat shortcut for that, which is to mention the name of the
# decorating function before the function to be decorated.
# The name of the decorator should be perpended with an @ symbol.
print("\n__________Using Decorators__________")
def p_decorate(func):
    # def func_wrapper(name):
    #     return "<p>{0}</p>".format(func(name))

    # To make our decorator useful for functions and methods alike,
    # we use args and kwargs instead of passing a specific variable
    def func_wrapper(*args, **kwargs):
        return "<p>{0}</p>".format(func(*args, **kwargs))
    return func_wrapper


@p_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)


print(get_text("John"))


# Passing arguments to decorators
print("\n__________Passing arguments to decorators__________")
def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


@tags("div")
@tags("strong")
@tags("p")
def get_text(name):
    return "Hello "+name


print(get_text("John"))
# One important thing to notice here is that the order of setting our
# decorators matters. If the order was different in the example above,
# the output would have been different.
print(get_text.__name__)  # get_text
print(get_text.__doc__)  # Concatenates Hello and specified name
print(get_text.__module__)  # __main__


# Debugging decorated functions: Functools to the rescue
# At the end of the day decorators are just wrapping our functions,
# in case of debugging that can be problematic since the wrapper function
# does not carry the name, module and docstring of the original function.
# Wraps is a decorator for updating the attributes of the wrapping
# function(func_wrapper) to those of the original function(get_text).
print("\n__________Debugging decorated functions: Functools to the rescue__________")
from functools import wraps


def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


@tags("p")
def get_text(name):
    """Concatenates Hello and specified name"""
    return "Hello "+name


print(get_text.__name__)  # get_text
print(get_text.__doc__)  # Concatenates Hello and specified name
print(get_text.__module__)  # __main__
