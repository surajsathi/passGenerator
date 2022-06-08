import time
import random

def password_generator(num):
    global password
    password = ''
    a1 = 'abcdefghijklmnopqrstuvwxyz'
    a2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a3 = '0123456789'
    a4 = '!@#$%^&*()+-='
    pass1 = []
    for i in range(num):
        if i%4==0:
            pass1.append(random.choice(a1))
        elif i%4==1:
            pass1.append(random.choice(a2))
        elif i%4==2:
            pass1.append(random.choice(a3))
        elif i%4==3:
            pass1.append(random.choice(a4))
        else:
            break
        i+=1
    random.shuffle(pass1)
    password = ''.join(pass1)
    print("Password: ",password)
    return password


def text_printer():
    try:
        saveas = input('Save as ? Enter name of text file:\n')
        directory = str(input('Directory you want to save in :\n'))
        label = input('Label for the password:\n')
        location = directory.upper()
        location += ':\ '
        location = location.replace(' ', saveas)
        location += '.txt'
        print(location)
        try:
            file = open(location, 'x')
            print('Creating new file:')
            time.sleep(0.5)
            file.write(str(label) + ': ' + str(password) + '\n')
            file = open(location, 'r')
            print(file.readlines()[-1])
            file.close()
        except FileExistsError:
            a = open(location, 'a')
            print('File already exists...')
            time.sleep(0.5)
            print('Writing at the end of file')
            time.sleep(0.5)
            a.write(str(label)+': '+str(password)+' \n')
            a.close()
            a = open(location, 'r')
            print(a.readlines()[-1])
            a.close()
        except ValueError:
            print('Something went wrong.')
        finally:
            print('Password is written')
    except ValueError:
        print('Invalid Input')


z = True
while z:
    try:
        num1 = int(input('how long password do you want?\n'))
        password_generator(int(num1))
        save = str(input('Do you want to save this password?(Y to save // any other key to exit).\n'))
        try:
            if save == 'Y' or save == 'y':
                text_printer()
                again =input('go again?(Y for again)\n')
                if again=='Y' or again=='y':
                    continue
                else:break
            else:
                print('Thank you')
                again = input('go again?(Y for again)\n')
                if again == 'Y' or again == 'y':
                    continue
                else:
                    break
        except NameError:
            print('Unknown Error')

    except ValueError:
        print("enter valid input:")




