
user = {
    'name' : 'unknown',
    'password' : 'unknown',
    'totalwins' : 0,
    'totalgames' : 0
}

# user = dict.fromkeys(['name', 'passwords'], 'unknown')

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
        if user.items == User.items() :
            print('log in successful. wellcome,' + user['name'] + '.')
            

