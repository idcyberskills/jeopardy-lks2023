#!/bin/bash

BASE_PATH="./src"

# Compile the .java source codes
for file in $BASE_PATH/*.java; do
    # Check if there are matching files
    if [ -e "$file" ]; then
        # Process each file (replace this with your actual logic)
        echo "Processing file: $file"
        javac -source 1.8 -target 1.8 -classpath /Users/chrisandoryan/Library/Android/Sdk/platforms/android-33/android.jar $file
        echo "File: $file has been compiled to .class."
    else
        # Handle the case where no matching files are found
        echo "No *.java files found in $BASE_PATH"
    fi
done

echo "Compiling all classes into DEX..."
d8 $BASE_PATH/*.class --output $BASE_PATH

BUCKET_PATH=gs://bagpack---lksn2023.appspot.com
ENCRYPTION_KEY_HEX=$(echo -n "M9qSJqhFCKRsgIY0" | xxd -p | tr -d '\n')
ENCRYPTION_IV_HEX=$(echo -n "lYpQVWW1fOs2rVFX" | xxd -p | tr -d '\n')

# Encrypt the .class files
for file in $BASE_PATH/*.dex; do
    # Check if there are matching files
    if [ -e "$file" ]; then
        # Process each file (replace this with your actual logic)
        echo "Processing file: $file"
        
        # Output file (encrypted)
        output_file="$file.enc"

        # Encrypt the file using AES-128-CBC
        openssl enc -aes-128-cbc -salt -in $file -out $output_file -K $ENCRYPTION_KEY_HEX -iv $ENCRYPTION_IV_HEX -nosalt -base64 -A

        echo "File encrypted successfully. Encrypted file: $output_file"

        gsutil cp "$output_file" "$BUCKET_PATH/${output_file##*/}"

        echo "File has been uploaded to Storage bucket"
    else
        # Handle the case where no matching files are found
        echo "No *.class files found in $BASE_PATH"
    fi
done