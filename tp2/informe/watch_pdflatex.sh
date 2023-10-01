#!/bin/bash

# Function to compile with pdflatex
compile_pdflatex() {
    pdflatex main.tex
}

# Initialize variables
changed_file=""
debounce_delay=1  # Adjust this value as needed (in seconds)

# Watch for file system events using inotifywait
inotifywait -m -r -e close_write --format '%w%f' . |
while read -r file; do
    # Check if the file ends with .tex before running pdflatex
    if [[ "$file" == *.tex ]]; then
        echo "Detected change in $file. Waiting for potential additional changes..."
        changed_file="$file"
        sleep $debounce_delay  # Wait for additional changes
        if [ "$changed_file" == "$file" ]; then
            echo "Compiling with pdflatex..."
            compile_pdflatex
        else
            echo "Additional changes detected. Skipping compilation."
        fi
    fi
done
