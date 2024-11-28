import os
from file_and_errors import my_first_file

def test_my_first_file():
    # Change to a specific directory where you want the file created
    desired_location = r"D:\Visual Studio Folder\Multiverse Github\contract\intermediate"
    os.chdir(desired_location)
    
    # Remove the file if it exists from previous runs to ensure a clean test
    if os.path.exists("myFirstFile.txt"):
        os.remove("myFirstFile.txt")
    
    # Run the function
    my_first_file()
    
    # Check if the file was created
    assert os.path.exists("myFirstFile.txt"), "The file was not created"
    
    # Verify the file content
    with open("myFirstFile.txt", "r") as f:
        content = f.read()
    assert content == "This is my first file.", "File content does not match"
