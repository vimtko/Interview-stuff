#!/bin/bash

INPUT= "../data/raw.txt"
OUTPUT= "..data/clean.txt"

echo "Cleaning data..."

grep -v "ERROR" $INPUT | grep -v "NaN" > $OUTPUT #we use grep to get every text that doesnt have "Error" or "NaN"


echo "Clean data saved on Clean.txt"