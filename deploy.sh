#!/bin/bash

# Run the Python script
echo "Running main.py..."
python3  /Users/aljazvidmar/Documents/Mars\ Hill\ University/finalProject/Main.py

# Check if the Python script ran successfully
if [ $? -ne 0 ]; then
    echo "main.py encountered an error. Exiting."
    exit 1
fi

# Run the PHP script and redirect output to server.html
echo "Running txtFileGenerator.php..."
php /Users/aljazvidmar/Documents/Mars\ Hill\ University/finalProject/txtFileGenerator.php > /Users/aljazvidmar/Documents/Mars\ Hill\ University/finalProject/server.html

# Check if the PHP script ran successfully
if [ $? -ne 0 ]; then
    echo "txtFileGenerator.php encountered an error. Exiting."
    exit 1
fi

# Sync the server.html with the server using rsync
echo "Syncing with the server..."
rsync -avr  /Users/aljazvidmar/Documents/Mars\ Hill\ University/finalProject/server.html aljaz_vidmar@cs.mhu.edu:./public_html/finalProject/finalProjectWebScraper/  
# Check if rsync was successful
if [ $? -ne 0 ]; then
    echo "Rsync failed. Exiting."
    exit 1
fi

echo "Deployment completed successfully!"
