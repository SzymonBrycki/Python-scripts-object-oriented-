import string
import random

class RandomPassword:

    def __init__(self):
        self.lc = string.ascii_lowercase
        self.uc = string.ascii_uppercase
        self.nr = string.digits
        self.special = string.punctuation

    def random_lowercase(self):
        random_lc = random.choice(self.lc)
        return random_lc

    def random_uppercase(self):
        random_uc = random.choice(self.uc)
        return random_uc

    def random_nr(self):
        random_nr = random.choice(self.nr)
        return random_nr

    def random_special(self):
        random_special = random.choice(self.special)
        return random_special

    def generate_safe_password(self, size = 20):
        random_list = list()

        while size != 0:
            random_step = random.randint(1,4)
            if random_step == 1:
                x = self.random_lowercase()
                random_list.append(x)
            elif random_step == 2:
                x = self.random_uppercase()
                random_list.append(x)
            elif random_step == 3:
                x = self.random_nr()
                random_list.append(x)
            else:
                x = self.random_special()
                random_list.append(x)
            
            size = size - 1
        
        return random_list

    def string_from_list(self, my_list):
        my_string = "".join(my_list)

        return my_string

    def final_result(self):
        a = self.generate_safe_password()
        b = self.string_from_list(a)
        
        return b
    
############################
# PROGRAM
############################

if __name__ == "__main__":

    mypass = RandomPassword()
    a = mypass.final_result()
    print("Your new safe password is: ", a)
