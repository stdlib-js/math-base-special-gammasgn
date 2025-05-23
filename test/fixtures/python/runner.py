#!/usr/bin/env python
#
# @license Apache-2.0
#
# Copyright (c) 2022 The Stdlib Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Generate fixtures."""

import os
import json
import numpy as np
from scipy.special import gammasgn

# Get the file path:
FILE = os.path.realpath(__file__)

# Extract the directory in which this file resides:
DIR = os.path.dirname(FILE)


def gen(x, name):
    """Generate fixture data and write to file.

    # Arguments
    * `n`: degree(s)
    * `x`: domain
    * `name::str`: output filename
    # Examples
    ``` python
    python> n = 1
    python> x = linspace(-1000, 1000, 2001)
    python> gen(n, x, './data.json')
    ```
    """
    y = gammasgn(x)

    # Convert all NaN values to 0 according to our convention:
    y[np.isnan(y)] = 0

    data = {
        "x": x.tolist(),
        "expected": y.tolist()
    }

    # Based on the script directory, create an output filepath:
    filepath = os.path.join(DIR, name)

    # Write the data to the output filepath as JSON:
    with open(filepath, "w", encoding='utf8') as outfile:
        json.dump(data, outfile)


def main():
    """Generate fixture data."""
    x = np.random.uniform(-1000, 1000, 2001)
    gen(x, "data.json")


if __name__ == "__main__":
    main()
