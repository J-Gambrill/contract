import os

def count_to_ten():
    num = 0
    while num < 10:
        num += 1
        print(num)
   
    numberList = list(range(1, 11))
    print(numberList)
    
    desiredLocation = r"D:\Visual Studio Folder\Multiverse Github\contract\intermediate"
    
    if not os.path.exists(desiredLocation):
        print("Error: The directory does not exist")
        return  # Exit the function if the directory doesn't exist
    
    os.chdir(desiredLocation)      

    with open("1to10.txt", "w") as f:
        f.write("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
