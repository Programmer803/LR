
user = {
    'name' : 'unknown',
    'password' : 'unknown',
}

register = False

while register == False :
    print('register. ')
    name = input('please enter your name: ')
    password = input('please enter your pasword: ')
    User = {
    'name' : name,
    'password' : password
    }
    user.update(User)
    register = True
    if register == True :
        print('register successful. ')
        break

print(user)
print(User)

while register == True :
    print('log in. ')
    name = input('please enter your name: ')
    password = input('please enter your pasword: ')
    User = {
    'name' : name,
    'password' : password
    }
    while not user.values() == User.values() :
        print('invalid password/name. ')
        name = input('please enter your name: ')
        password = input('please enter your pasword: ')
        User = {
        'name' : name,
        'password' : password
        }
        if user.values() == User.values() :
            print('log in successful. wellcome,' + user['name'] + '.')
            


            

