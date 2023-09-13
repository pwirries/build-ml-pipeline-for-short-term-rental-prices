'''
This module performs basic cleaning of input data for the random
forest model.
'''

import argparse
import os
import numpy as np
import pandas as pd
import logging
import wandb

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()

def go(args):
    logging.info("Connecting to W&B and acquiring input artifact")
    run = wandb.init(job_type="basic_cleaning")
    artifact_path = run.use_artifact(args.input_artifact).file()
    data = pd.read_csv(artifact_path)
    
    # Drop outliers
    min_price = args.min_price
    max_price = args.max_price
    idx = data['price'].between(min_price, max_price)
    data = data[idx].copy()
    # Convert last_review to datetime
    data['last_review'] = pd.to_datetime(data['last_review'])

    data.to_csv("clean_sample.csv", index = False)

    artifact = wandb.Artifact(
        args.output_artifact,
        type = args.output_type,
        description = args.output_description,
    )
    artifact.add_file("clean_sample.csv")
    run.log_artifact(artifact)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic cleaning of dataset")
    parser.add_argument(
        "--input_artifact",
        type=str,
        help="Name of input artifact to use from W&B"
    )
    parser.add_argument(
        "--output_artifact",
        type=str,
        help="Artifact name to store output in W&B"
    )
    parser.add_argument(
        "--output_description",
        type=str,
        help="Brief description of output artifact"
    )
    parser.add_argument(
        "--output_type",
        type=str,
        help="Type of output artifact"
    )
    parser.add_argument(
        "--min_price",
        type=float,
        help="Minimum price for filtering outliers"
    )
    parser.add_argument(
        "--max_price",
        type=float,
        help="Maximum price for filter outliers"
    )

    args = parser.parse_args()

    go(args)
