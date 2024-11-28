import os
from unittest.mock import patch, mock_open
import pytest
from func_for_my_test import count_to_ten  # Replace 'your_script_name' with your actual file name

def test_print_numbers(capfd):
    # Test if numbers 1 to 10 and the list are printed correctly
    count_to_ten()
    captured = capfd.readouterr()
    assert captured.out == (
        "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n" #the \n acts almost as a line break
    )

@patch("os.path.exists", return_value=True)
@patch("os.chdir")
@patch("builtins.open", new_callable=mock_open)
def test_file_creation(mock_file, mock_chdir, mock_exists):
    # Test file creation and content
    count_to_ten()
    mock_chdir.assert_called_once()  # Check if os.chdir was called
    mock_file().write.assert_called_once_with("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")  # Check file content

@patch("os.path.exists", return_value=False)
def test_directory_does_not_exist(mock_exists, capfd):
    # Test when the directory does not exist
    count_to_ten()
    captured = capfd.readouterr()
    assert "Error: The directory" in captured.out
