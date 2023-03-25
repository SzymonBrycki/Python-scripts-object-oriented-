import time

class Epoch():
    '''
    Class that finds, formats and print the beginning of Epoch on a given computer
    '''
	
    def epochBeginning(self):
        '''
        Method that finds the beginning of epoch on a computer.

        ARGUMENTS:

        Nothing

        RETURNS:

        epoch2 (str)
        '''
        time_string = "The epoch on this computer begins with %A, %d %b %Y"
        epoch = time.gmtime(0)
        epoch2 = time.strftime(time_string, epoch)
        # print(type(epoch2)) # returns str
        return epoch2

    def printEpoch(self):
        '''
        Method which prints beginning of epoch (found by Method epochBeginning())

        ARGUMENTS:

        Nothing

        RETURNS:

        Nothing (BUT prints the epoch beginning!)
        '''
        print(Epoch().epochBeginning())

if __name__ == "__main__":
    oEpoch = Epoch()	
    oEpoch.printEpoch()