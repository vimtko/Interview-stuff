#!/bin/bash

echo "Starting Pipeline..."

cd scripts

./clean.sh
python3 process.py

echo "Pipeline Ended. Results in data/result.txt"