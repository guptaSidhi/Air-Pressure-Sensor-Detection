import os

path = r"C:\Users\Sidhi Gupta\Desktop\PROJECTS\Air Pressure Sensor Detection\notebook\test_file.txt"
try:
    with open(path, "w") as f:
        f.write("Test content")
    print("Write operation successful.")
    os.remove(path)  # Clean up the test file after writing
except Exception as e:
    print(f"Test failed with error: {e}")