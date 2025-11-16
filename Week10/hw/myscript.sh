#!/bin/bash

echo "Enter URL: "
read URL
echo "Downloading from $URL"
wget $URL
touch log.txt
echo $URL >> log.txt
