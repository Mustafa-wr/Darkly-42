#!/bin/bash

# Ask for the server URL
echo "What is your Server?"
read URL

# Get the list of directories in the .hidden folder
F=`curl -L $URL/.hidden 2>/dev/null | cut -d '>' -f2 | cut -d '/' -f1 | tr '<' ' ' | tail -n +5 | head -n +26`

# Iterate through the first level directories
for i in $(echo $F | tr " " "\n"); do 
    # Get README at the first level
    curl -L $URL/.hidden/$i/README 2>/dev/null

    # Get the list of subdirectories in the first-level directories
    for n in $(curl -L $URL/.hidden/$i 2>/dev/null | cut -d '>' -f2 | cut -d '/' -f1 | tr '<' ' ' | tail -n +5 | head -n +26 | tr " " "\n"); do 
        # Get README at the second level
        curl -L $URL/.hidden/$i/$n/README 2>/dev/null

        # Get the list of subdirectories in the second-level directories
        for m in $(curl -L $URL/.hidden/$i/$n 2>/dev/null | cut -d '>' -f2 | cut -d '/' -f1 | tr '<' ' ' | tail -n +5 | head -n +26 | tr " " "\n"); do 
            # Get README at the third level
            curl -L $URL/.hidden/$i/$n/$m/README 2>/dev/null
        done
    done
done
