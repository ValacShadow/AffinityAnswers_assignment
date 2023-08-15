#!/bin/bash

# Define the URL and output file name
URL="https://www.amfiindia.com/spages/NAVAll.txt"
OUTPUT_FILE="mutual_fund.tsv"

# Download the file using curl and extract the relevant fields using awk by spliting line on ';'
curl -s "$URL" | awk -F ';' 'BEGIN {OFS="\t"} {print $4, $5}' > "$OUTPUT_FILE"

# Print a message upon completion
echo "Scheme Name and Asset Value fields have been extracted and saved in $OUTPUT_FILE"


