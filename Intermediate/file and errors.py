import os
print("Current Working Directory:", os.getcwd())

desiredLocation = r"D:\Visual Studio Folder\Multiverse Github\contract\intermediate"  # Change to the script's directory location as it was creating the file in the parent folder contract
os.chdir(desiredLocation)                                                             # the r is needed so python can recognise the backslashes \

import os
print("Current Working Directory:", os.getcwd())


try:
    f = open("myFirstFile.txt", "x")
    f = open("myFirstFile.txt", "w")
    f.write("This is my first file.")
    f.close()
except FileExistsError:
    print('You cannot run this code again as the file already exists')
except:
    print('An error unrelated to the FileExistsError occured')

# if this code is run more than once there will be an error as the code already exists so i will add a try block. See above.