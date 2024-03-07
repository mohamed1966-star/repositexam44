
def decorator(func):
    print('***********************')
    return func


@decorator
def hello():
    print("Hello !")

#hello=decorator(hello)


@decorator
def hi():
    print("Hi !")


hello()
#hello=decorator(hello)

#hi=decorator(hi)
hi()

print('***************************************')

user_logged = True


def check_user_logged(func):
    def wrapper():
        if user_logged:
            print('You are login')
            return func()
        else:print("try again.......")
    return wrapper


@check_user_logged
def profile():
    print(" Le profile membre ...")


@check_user_logged
def articles():
    print(' Les articles........')


profile()
articles()

print('***************************************')

user_logged = "jason"


def check_user(username):
    def decorator(func):
        def wrapper():
            if user_logged == username:
                print('You are login')
                return func()
            else:
                print("try again")
        return wrapper
    return decorator


@check_user("mp")
def profile():
    print(" Le profile membre ...")


profile()
print('===================================')

user_logged = "jason"
import functools


def check_user(username):
    def decorator(func):
        @functools.wraps(func)
        def wrapper():
            
            """
            le wrapper........
            """
            if user_logged == username:
                print('You are login')
                return func()
            else:
                print("try again")
        return wrapper
    return decorator


@check_user("jason")
def profile():
    """
    page d'acces au profil de l'utilisateur
    """
    print(" Le profile membre ...")


help(profile)



