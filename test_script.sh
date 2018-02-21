#!/bin/bash



# Find the python source file for given test number
python_file=`find "sols/python/$1/" -name "*.py"`
echo "Name of source file : $python_file"



# loop through input file directory
# and run the python script with each input file

for f in "inputs/$1"/*
do
	echo
	echo "Running command : python $python_file $f"
	python $python_file $f
	echo 
done