class BMICalc():
    '''
    Class that implements a BMI Calculator.
    '''
    def calc(self):
        '''
        Method that ask for data and calculated the BMI.

        ARGUMENTS:

        Nothing

        RETURNS:

        Nothing (BUT prints the calculated BMI)
        '''

        print("Welcome to the BMI Calculator. Enter your data balow.")

        mass = int(input("Your weight in kilograms? "))
        height = float(input("Your height in meters? "))

        BMI = mass / height**2

        print("Your BMI is %.2f" % BMI)

if __name__ == "__main__":
    oCalc = BMICalc()
    oCalc.calc()