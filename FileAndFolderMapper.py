import os

class Mapper():
    '''
    Class that prints map of subfolders and files in a givne folder.
    '''

    BaseFolder = None # LATER: input("Enter the PATH towards the base file: ")

    main_list = list()
    main_string = None

    double_space = "  "
    new_line = "\n"

    def __init__(self):
        self.FilesSUM = 0
        self.DirectoriesSUM = 0

    def findLastSlash(self, my_string):
        '''
        Finds last slash in a given string. 
        
        ARGUMENTS:
        ----------
        
        my_string (str).
        
        RETURNS:
        ----------
        
         x <which is minus number being the index of lash found slash> (int)
        '''
        
        slash = "\\"
        x = -1
        for char in my_string:
            if my_string[x] == slash:
                return x
            else:
                x = x-1
                
            # WEEEEEE! It's working! :3

    def countSlashes(self, base):
        '''
        Counts all slashes in a given argument.
        
        ARGUMENTS:
        ----------
        
        base (str).
        
        RETURNS:
        ----------
        
        numberOfSlashes (int)
        '''
        
        numberOfSlashes = base.count("\\")
        return numberOfSlashes	

    def determineFinalSlashes(self, base):
        '''
        Function that determines how many double spaces should be entered.

        ARGUMENTS:
        ----------
        
        base (str)

        RETURNS:
        ----------
        
        slashes_final (int)
        '''
        slashes = Mapper().countSlashes(base) # number of slashes in current folder
        slashes_minus = Mapper().countSlashes(BaseFolder) # number of slashes in the Base Folder 
        slashes_final = slashes - slashes_minus # number of slashes that's a difference between BaseFolder and current folder

        return slashes_final
    
    def sliceToLastElement(self, base):
        '''
        A function which strips the string of all adress of a file/folder into it's last element (the file/folder itself).

        ARGUMENTS:
        ----------
        
        base (str) [the adress of a file/folder]

        RETURNS:
        ----------
        
        my_new_string
        '''
        beginning_of_string = Mapper().findLastSlash(base) # the number of last slash in given folder, counted from the back

        my_new_string = base[beginning_of_string:] # string from the last slash till beginning of folder name

        return my_new_string

    def addNicelyFolders(self, base):
        '''
        A function which add folders in this program to main_list in a nice fashion. 
        
        ARGUMENTS:
        ----------
        
        base (str)
        
        RETURNS:
        ----------
        
        appends main_string with my_new_string_2
        '''
        
        # global new_line
        # global double_space

        new_string = Mapper().sliceToLastElement(base)
        slashes_final = Mapper().determineFinalSlashes(base)

        if base == BaseFolder:
            my_new_string_2 = new_string + Mapper().new_line # ... at the beginning of new print
        else:
            my_new_string_2 = (Mapper().double_space * slashes_final) + new_string + Mapper().new_line # add additional double space in case of non-BaseFolder folders
        
        slashes_of_main = Mapper().countSlashes(BaseFolder)
        slashes_compare = Mapper().countSlashes(base)

        Mapper().main_list.append(my_new_string_2)

    def printTheMainList(self):
        '''
        Function that prints the main_list, so we can see what's in there.

        ARGUMENTS:
        ----------

        None

        RETURNS:

        None (but prints the main string)
        ----------
        '''
        global main_string

        main_string = " ".join([str(item) for item in Mapper().main_list])

        print(main_string)

    def findingSlash(self, my_list): # it needs to be list[1], list[-1] etc !!!
        '''
        Function that checks if there is a slash in a given list

        ARGUMENTS:
        ----------
        
        my_list (list[nr])

        RETURNS:
        ----------
        
        False if no slash or position of slash (if contains one)
        '''

        # searched_thing = my_list.join()

        searched_thing = " ".join(map(str, my_list))

        boolean = searched_thing.find("\\")

        if boolean == -1:
            return False 
        else:
            return boolean

    def spacesPrevious(self, my_list):
        '''
        Function that finds number of spaces in the previous list member.

        ARGUMENTS:
        ----------
        
        my_list (list)

        RETURNS:
        ----------
        
        number_of_formated_spaces (int) (being formatted - it should work no matter id double_space is 1, 2 or 4 spaces)
        '''
        previous_list = my_list[-1]
        searched_thing = " ".join(map(str, previous_list))
        # searched_thing = previous_list.join() WRONG???

        space_counter = 0

        for char in searched_thing:
            if char == " ":
                space_counter = space_counter + 1
            else:
                break

        number_of_formatted_spaces = int(space_counter / 4)

        return number_of_formatted_spaces

    def finalStringOfFiles(self, file):
        '''
        A function to determine the final string that a file adress should have been.

        ARGUMENTS:
        ----------
        
        file (str)

        RETURNS:
        ----------
        
        string_with_file (str)
        '''
        previous_entry = Mapper().main_list[-1]

        if Mapper().findingSlash(previous_entry) is False:
            spaces = Mapper().spacesPrevious(Mapper().main_list)
        else:
            spaces = Mapper().spacesPrevious(Mapper().main_list) + 1

        string_with_file = (Mapper().double_space * spaces) + Mapper().sliceToLastElement(file)
        return string_with_file

    def addNicelyFiles(self, file):
        '''
        A function that add files to main_list in a nice fashion.

        ARGUMENTS:
        ----------
        
        file (str)

        RETURNS:
        ----------
        
        appends main_list (with my_string)
        '''
        my_string = Mapper().finalStringOfFiles(file) + Mapper().new_line

        Mapper().main_list.append(my_string)

    def run(self):
        '''
        Runs the program.

        ARGUMENTS:
        ----------

        None

        RETURNS:
        ----------

        None (but runs the program)
        '''
        
        print("")
        print("Printing folders nicely!")
        print("")
        
        global BaseFolder
        BaseFolder = input("Enter the PATH towards the base file: ")

        print("") # just a nice space

        for base, dirs, files in os.walk(BaseFolder):
            Mapper().addNicelyFolders(base) # put here function "printNicelyFolders
            # for name in files:
                # printNicelyFiles(name)
            for directory in dirs:
                self.DirectoriesSUM = self.DirectoriesSUM + 1
            for file in files:
                Mapper().addNicelyFiles(file)
                self.FilesSUM = self.FilesSUM + 1

        Mapper().printTheMainList()
                
        print("")
        print("Total number of files:", self.FilesSUM)
        print("Total number of directories:", self.DirectoriesSUM)
        print("Total items:", self.FilesSUM + self.DirectoriesSUM)
        print("")

        while True:
            Yes_no = input("Do you wish to save the result of the program? Y/N ")

            print("")

            if Yes_no.upper() == "Y":
                name = input("Enter the name of file you wish to save OR leave blank for default name ")

                print("")
                
                if len(name) == 0:
                    name = "FileAndFolderMapper.txt"

                else:
                    name = name + ".txt"

                f = open(name, "w")
                opening = "Snapshot of a folder created in FileAndFolderMapper.py "

                from datetime import date, datetime

                today = date.today()

                today_formatted = today.strftime("%d-%b-%Y")

                now = datetime.now()

                now_formatted = now.strftime("%H:%M:%S") 

                date_of_creation = "File created on: " + today_formatted + " " + now_formatted

                file_buffer = [opening, new_line, date_of_creation, new_line, new_line, BaseFolder, new_line, main_string]

                # f.writelines("%s\n" % line for line in file_buffer)
                f.writelines(file_buffer)

                cwd = os.getcwd()
                cwd_2 = cwd + "\\" + name 

                print("File saved under the following destination: ")

                print("")
                print(cwd_2)

                break
            
            elif Yes_no.upper() == "N":
                print("Finishing the program without saving. ")

                break

            else:
                print("Unknown command (must be Y/N). Try again. ")


        print("")
        iks = input("Enter any character to finish... ")
        exit() 

if __name__ == "__main__":
    oMapper = Mapper()
    oMapper.run()