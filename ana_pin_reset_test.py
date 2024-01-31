import getpass
# hard-coding an initial value for pin. It will change after reset.
pin = '7860'

def pin_reset():
    # variable is assigned predefined value of Mother's maiden name, attempts is initialized as 0
    # and new_pin is same as global variable pin
    mm_name = 'Shree'
    attempts = 0
    new_pin = pin
    done = False
    reset_trials = 1
    # informs user that their pin is blocked, and they should answer security question to reset it
    print('PIN blocked. \nAnswer security question to reset PIN: What is your mother\'s maiden name?')
    # the getpass() method discreetly gets answer to security question from user
    answer = getpass.getpass(prompt='Answer: ')
    # if answer is correct user is asked to enter new pin and confirm repeatedly until the two entries match
    if answer == mm_name:
        while not done:
            new_pin = getpass.getpass("Enter new PIN: ", stream=None)
            confirm_pwd = getpass.getpass("Confirm new PIN: ", stream=None)
            reset_trials += 1
            if confirm_pwd == new_pin:
                print("PIN successfully changed.")
                attempts = 3
                done = True
            elif reset_trials == 4:
                done = True
                print("Too many failed attempts. Contact customer service.")
    return new_pin, attempts


# main code
attempts_left = 3
# while loop runs three times
while attempts_left:
    # getpass() gets user input discreetly
    supplied_pin = getpass.getpass(prompt='Enter your PIN to access baking: ', stream=None)
    if supplied_pin == pin:
        print('Success!')
        break
    else:
        print(f"Incorrect PIN\n Warning: Only {attempts_left - 1} left!")
        attempts_left -= 1
        if attempts_left == 0:
            pin, attempts_left = pin_reset()
            # above line of code calls function pin_reset() which is defined prior to main code
