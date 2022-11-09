"""
Description:
    Script for training model.
"""

import argparse
import tensorflow as tf
import tensorflow_datasets.public_api as tfds
import pandas as pd

def define_and_parse_args():
    pass

def download_data(dataset: str):
    """Load data from tensor flow dataset api"""
    tfds.load(
        name = dataset,
        data_dir="./data"
    )
    
def load_data():
    pass

def create_model():
    pass

def train_model():
    pass

def main():
    # Load data
    dataset = "snli"
    data = load_data(dataset)
    print(type(data))
    
    # Create model
    model = create_model()
    
    # Train model
    trained_model = train_model()

if __name__ == "__main__":
    main()
