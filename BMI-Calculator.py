class BMICalc():
    '''
    Class that implements a BMI Calculator.
    '''
    def calc(self) -> float:
        '''
        Method that ask for data and calculates the BMI.

        ARGUMENTS:
        ----------

        Nothing

        RETURNS:
        ----------

        Nothing (BUT prints the calculated BMI)
        '''

        print("Welcome to the BMI Calculator. Enter your data balow.")

        mass = int(input("Your weight in kilograms? "))
        height = float(input("Your height in meters? "))

        BMI = mass / height**2

        return BMI
    
    def printBMI(self) -> None:
        '''
        Method that prints BMI.

        ARGUMENTS:
        ----------

        Nothing

        RETURNS:
        ----------

        Nothing (BUT prints the BMI)
        '''
        BMI = BMICalc.calc(self)
        print(f"Your BMI is {BMI:.2f}")

if __name__ == "__main__":
    oCalc = BMICalc()
    oCalc.printBMI()