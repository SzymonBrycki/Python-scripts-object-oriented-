import string
import random

newline = "\n"

class RandomPassword:
    '''
    A class that creates random password.
    '''

    def __init__(self):
        self.lc = string.ascii_lowercase
        self.uc = string.ascii_uppercase
        self.nr = string.digits
        self.special = string.punctuation

    def random_lowercase(self):
        '''
        Returns a random lowercase character.

        ARGUMENTS:
        ----------
        
        None

        RETURNS:
        ----------

        random_lc (char)
        '''
        random_lc = random.choice(self.lc)
        return random_lc

    def random_uppercase(self):
        '''
        Returns a random uppercase character.

        ARGUMENTS:
        ----------

        None

        RETURNS:
        ----------
        
        random_uc (char)
        '''
        random_uc = random.choice(self.uc)
        return random_uc

    def random_nr(self):
        '''
        Return a random number ( 0-9 ).

        ARGUMENTS:
        ----------

        None

        RETURNS:
        ----------
        
        random_nr (char)
        '''
        random_nr = random.choice(self.nr)
        return random_nr

    def random_special(self):
        '''
        Returns a random special character.

        ARGUMENTS:
        ----------
        
        None

        RETURNS:
        ----------
        
        random_special (char)
        '''
        random_special = random.choice(self.special)
        return random_special

    def generate_safe_password(self, size = 20):
        '''
        Generates a safe, random password (as a list !!! ). 
        The atribute of the function, unless specified otherwise, 
        will generate 20-char long pass.

        ARGUMENTS:
        ----------
        
        size - (int, default = 20)

        RETURNS:
        ----------
        
        random list - list (of characters) 
        '''

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
        '''
        Turns a list (of random characters) into a string.

        ARGUMENTS:
        ----------
        
        my_list (list)

        RETURNS:
        ----------

        my string (string)
        '''
        my_string = "".join(my_list)

        return my_string

    def final_result(self):
        '''
        Sets the final result of the computations, i.e. random password.
        
        Will generate 20-char long pass. 
        If you need a longer or shorter password, 
        use final_result_of_given_size()

        ARGUMENTS:
        ----------

        None

        RETURNS:
        ----------

        b (string)
        '''
        a = self.generate_safe_password()
        b = self.string_from_list(a)
        
        return b
    
    def final_result_of_given_size(self, size):
        '''
        Generates safe password of given size.

        ARGUMENTS:
        ----------

        size (int)

        RETURNS:
        ----------

        b (string) 
        '''

        a = self.generate_safe_password(size)
        b = self.string_from_list(a)

        return b

    def generate_n_passwords(self, n, size = 20):
        '''
        Generates n passwords of size size (by default 20)

        ARGUMENTS:
        ----------

        n (int)
        size  (int, default = 20)

        RETURNS:
        ----------

        b (string) <prints nicely!>
        '''

        counter = 0
        b = ""

        while n !=0:
            counter = counter + 1
            a = self.final_result_of_given_size(size)
            b = b + " " + str(counter) + " : " + a + newline
            n = n - 1

        return b

    
############################
# PROGRAM
############################

if __name__ == "__main__":

    mypass = RandomPassword()
    a = mypass.final_result()
    print("Your new safe password is: ", a)

    '''
    # DELETE COMMENTS TO GEN 1 pass of size 10

    mypass2 = RandomPassword()
    a = mypass2.final_result_of_given_size(10)
    print("You second password is: ", a)
    '''

    '''
    # DELETE COMMENTS TO GEN 10 passwords of size 5

    mypass3 = RandomPassword()
    a = mypass3.generate_n_passwords(10, 5)
    print(a)
    '''
