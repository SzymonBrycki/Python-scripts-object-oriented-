import platform

class SysData():
    '''
    Class that prints computer system data.

    METHODS:
    ----------

    printData()
    '''

    def printData(self) -> None:
        '''
        Method that prints computer system data.
        
        ARGUMENTS:
        ----------

        Nothing

        RETURNS:
        ----------

        Nothing (BUT prints the data)
        '''

        print("System information:")

        SysInfo = platform.uname()

        print("OS: {}".format(SysInfo[0]))
        print("OS release: {}".format(SysInfo[2]))
        print("OS version: {}".format(SysInfo[3]))
        print("Machine type: {}".format(SysInfo[4]))
        print("Machine name: {}".format(SysInfo[1]))

if __name__ == "__main__":
    oSysData = SysData()
    oSysData.printData()

