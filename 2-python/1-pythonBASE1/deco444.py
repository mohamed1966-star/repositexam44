name = input('Enter your name :')
password  = input('Your password :')
def logged_in(function):
    def inner():
        if name == "jamal" and password == "123456":
            function()
        else:
            print('please login')
            return
    return inner    
@logged_in
def get_account():
    print("You are logged in, user name",name, "password",password)
get_account()


