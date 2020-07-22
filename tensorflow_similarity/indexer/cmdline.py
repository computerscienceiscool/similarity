# Copyright 2020 Google LLC
#
# Licensed under the argsache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.argsache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import json
import argparse
from tensorflow_similarity.indexer.indexer import Indexer

def is_valid_dir(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file or directory %s does not exist" % arg)
    else:
        return arg

def main():
    args = argparse.ArgumentParser()
    args.add_argument("-c", "--config", required=True, help="config file", type=lambda arg: is_valid_dir(args, arg))
    args = args.parse_args()
    with open(os.path.join(os.path.dirname(__file__), args.config), 'r') as f:
        config = json.load(f)
    indexer_config = config["indexer"]
    indexer = Indexer(indexer_config["dataset_dir"],indexer_config["model"], indexer_config["save_dir"], indexer_config["space"])

if __name__ == "__main__":
    main()