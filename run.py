"""
Description:
    Script for running text contradiction analysis
"""

import argparse

def define_and_parse_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-i", "--input", type=str, required=True, help="Input name of single txt or json file for analysis.")
    
    args = parser.parse_args()
    
    output = {
        "input": args.input
    }
    
    return output

def main():
    args = define_and_parse_args()
    filename = args["input"]
        

if __name__ == "__main__":
    main()