"""
Description:
    Script for training model.
"""

import argparse
import tensorflow as tf
import tensorflow_datasets.public_api as tfds
import pandas as pd

def define_and_parse_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-i", "--input", type=str, required=True, help="Input name of single txt or json file for training.")
    
    args = parser.parse_args()
    
    output = {
        "input": args.input
    }
    
    return output

def load_data(filename: str):
    json_obj = pd.read_json(path_or_buf=filename, lines=True)
    return json_obj

def create_model():
    pass

def train_model():
    pass

def main():
    # Get user args
    args = define_and_parse_args()
    filename = args["input"]
    
    # Load data
    data = load_data(filename)
    
    # Create model
    model = create_model()
    
    # Train model
    trained_model = train_model()

if __name__ == "__main__":
    main()
