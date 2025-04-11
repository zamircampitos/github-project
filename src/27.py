import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        return
    
    input_file = sys.argv[1]
    
    with open(input_file, "r") as file:
        lines = file.readlines()
        
        for line in lines:
            words = line.split()
            
            if len(words) > 0 and words[0] == "hello":
                print("".join(words[1:]))
                
if __name__ == "__main__":
    main()
