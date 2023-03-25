class FizzBuzz():
    '''
    Class that implements the popular FizzBuzz programming problem.
    '''
    def printFizzBuzz(self):
        '''
        Method that prints FizzBuzz.

        ARGUMENTS:

        Nothing

        RETURNS:

        Nothing (BUT prints the FizzBuzz)
        '''
        for number in range (1, 100):
            if number % 3 == 0 and number % 5 == 0:
                print("FizzBuzz")
            elif number % 3 == 0:
                print("Fizz")
            elif number % 5 == 0:
                print("Buzz")
            else:
                print(number)
                
if __name__ == "__main__":
    oFizzBuzz = FizzBuzz()
    oFizzBuzz.printFizzBuzz()