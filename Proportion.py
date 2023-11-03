class Proportion():
    '''
    Class that calculates mathematical proportions.
    '''
    def calcA(self) -> None:
        '''
        Method that calculates A.

        ARGUMENTS:
        ----------

        Nothing

        RETURNS:
        ----------

        Nothing (BUT prints A)
        '''
        B = input("Enter B(%) ")
        C = input("Enter C ")
        D = input("Enter D(%) ")
		
        B = int(B)
        C = int(C)
        D = int(D)
		
        result = (B*C)/D
		
        print("")
        print("A is equal to: ", result)

    def calcB(self) -> None:
        '''
        Method that claculates B.

        ARGUMENTS:
        ----------

        Nothing

        RETURNS:
        ----------

        Nothing (BUT prints B)
        '''
        A = input("Enter A ")
        C = input("Enter C ")
        D = input("Enter D(%) ")
		
        A = int(A)
        C = int(C)
        D = int(D)
		
        result = (A*D)/C
		
        print("")
        print("B is equal to: ", result, "%")
	
    def calcC(self) -> None:
        '''
        Method that calculates C.

        ARGUMENTS:
        ----------

        Nothing

        RETURNS:
        ----------

        Nothing (BUT prints C)
        '''
        A = input("Enter A ")
        B = input("Enter B(%) ")
        D = input("Enter D(%) ")
		
        A = int(A)
        B = int(B)
        D = int(D)
		
        result = (A*D)/B
		
        print("")
        print("C is equal to: ", result)
	
    def calcD(self) -> None:
        '''
        Method that calculates D.

        ARGUMENTS:
        ----------

        Nothing

        RETURNS:
        ----------

        Nothing (BUT prints D)
        '''
        A = input("Enter A ")
        B = input("Enter B(%) ")
        C = input("Enter C ")
		
        A = int(A)
        B = int(B)
        C = int(C)
		
        result = (B*C)/A
		
        print("")
        print("D is equal to: ", result, "%")

    def wrongLetter(self) -> None:
        '''
        Method that runs if some other input than A, B, C or D is entered.

        ARGUMENTS:
        ----------

        Nothing

        RETURNS:
        ----------

        Nothing
        '''
        print("")
        print("Wrong input. Try again.")
        Proportion().run()
	
    def run(self) -> None:
        '''
        Method that's the main loop of the program.

        ARGUMENTS:
        ----------

        Nothing

        RETURNS:
        ----------

        Nothing
        '''
        print("Welcome to my proportions calculator!")
        print("Below is the proportion equation.")
        print("Enter the number you are looking for and then all other data.")
        print("The program will calculate the unknown.")
        print("")
        print("A = B%")
        print("C = D%")
        print("")
        print("A*D% = C*B%")
        print("")
            
        letter = input("What to calculate? A/B/C/D ")

        letter = letter.upper()

        if letter == "A":
            Proportion().calcA()
        
        elif letter == "B":
            Proportion().calcB()
	    
        elif letter == "C":
            Proportion().calcC()
		
        elif letter == "D":
            Proportion().calcD()
	    
        else:
            Proportion().wrongLetter()

if __name__ == "__main__":
    oProportion = Proportion()
    oProportion.run()