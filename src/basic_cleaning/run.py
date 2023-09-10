'''
This module performs basic cleaning of input data for the random
forest model.
'''

import argparse
import os
import numpy as np
import pandas as pd

def go(args):
    print(args)
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic cleaning of dataset")
    parser.add_argument(
        "--input_artifact",
        type="str",
        help="Name of input artifact to use from W&B"
    )
    parser.add_argument(
        "--artifact_name",
        type="str",
        help="Artifact name to store output in W&B"
    )
    parser.add_argument(
        "--artifact_description",
        type="str",
        help="Brief description of output artifact"
    )
    parser.add_argument(
        "--artifact_type",
        type="str",
        help="Type of output artifact"
    )

    args = parser.parse_args()

    go(args)