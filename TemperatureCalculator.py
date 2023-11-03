class TemperatureCalculator():
    '''
    This class contains Methods for calculating temperature.
    '''
    
    return_string = None

    def calcCtoK(self, celcius: float) -> float:
        '''
        Calculates C to K.

        ARGUMENTS:
        ----------

        celcius (float)

        RETURNS:
        ----------

        kelvin (float)
        '''
        kelvin = 273.15 + celcius
        return kelvin

    def calcCtoF(self, celcius: float) -> float:
        '''
        Calculates C to F.

        ARGUMENTS:
        ----------

        celcus (float)

        RETURNS:
        ----------

        fahrenheit (float)
        '''
        fahrenheit = 32 + ( 9 / 5 * celcius)
        return fahrenheit

    def calcKtoC(self, kelvin: float) -> float:
        '''
        Calculates K to C.

        ARGUMENTS:
        ----------

        kelvin (float)

        RETURNS:
        ----------

        celcius (float)
        '''
        celcius = kelvin - 273.15
        return celcius

    def calcKtoF(self, kelvin: float) -> float:
        '''
        Calculates K to F.

        ARGUMENTS:
        ----------

        kelvin (float)

        RETURNS:
        ----------

        fahrenheit (float)

        '''
        fahrenheit = 1.8 * (kelvin - 273) + 32
        return fahrenheit

    def calcFtoC(self, fahrenheit: float) -> float:
        '''
        Calculates F to C.

        ARGUMENTS:
        ----------

        fahrenheit (float)

        RETURNS:
        ----------

        celcius (float)
        '''
        celcius = (fahrenheit - 32) * 5 / 9
        return celcius

    def calcFtoK(self, fahrenheit: float) -> float:
        '''
        Calculates F to K.

        ARGUMENTS:
        ----------

        fahrenheit (float)

        RETURNS:
        ----------

        kelvin (float)
        '''
        kelvin = (fahrenheit + 459.67) * 5 / 9
        return kelvin

    def getReturnString(self, type_of_degrees: str) -> None:
        '''
        Changes global return_string depending on the choice - C, F or K

        ARGUMENTS:
        ----------

        type_of_degrees (str)

        RETURNS:
        ----------

        None (but changes return_string global)
        '''

        global return_string

        if type_of_degrees.upper() == "C":
            return_string = "C"
        elif type_of_degrees.upper() == "F":
            return_string = "F"
        else:
            return_string = "K"

    def printResults(self, temperature_value: float) -> None:
        '''
        Prints the results.

        ARGUMENTS:
        ----------

        temperature_value (float)

        RETURNS:
        ----------

        Nothing (but prints stuff)
        '''
        if return_string.upper() == "C":
            print(temperature_value, "Celcius is", TemperatureCalculator().calcCtoK(temperature_value), "Kelvin")
            print(temperature_value, "Celcius is", TemperatureCalculator().calcCtoF(temperature_value), "Fahrenheit")
        elif return_string.upper() == "F":
            print(temperature_value, "Fahrenheit is", TemperatureCalculator().calcFtoC(temperature_value), "Celcius")
            print(temperature_value, "Fahrenheit is", TemperatureCalculator().calcFtoK(temperature_value), "Kelvin")
        elif return_string.upper() == "K":
            print(temperature_value, "Kelvin is", TemperatureCalculator().calcKtoC(temperature_value), "Celcius")
            print(temperature_value, "Kelvin is", TemperatureCalculator().calcKtoF(temperature_value), "Fahrenheit")

    def main(self) -> None:
        '''
        The main part of the program. 

        ARGUMENTS:
        ----------

        None

        RETURNS:
        ----------

        None (but runs all the stuff)
        '''
        print("Welcome to the temperature calculator! Enter the temperature below to find its value in different degrees!")

        type_of_degrees = str(input("What kind of degrees you wanna recalculate? [C/F/K] "))

        if type_of_degrees.upper() != "C" and type_of_degrees.upper() != "F" and type_of_degrees.upper() != "K":
            raise Exception("Wrong value! Should be C or F or K!")

        temperature_value = int(input("Enter the number of degrees "))

        TemperatureCalculator().getReturnString(type_of_degrees)
        TemperatureCalculator().printResults(temperature_value)

if __name__ =="__main__":
    oCalc = TemperatureCalculator()
    oCalc.main()