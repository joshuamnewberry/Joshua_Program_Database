#!/bin/bash

# Script to easily backup files to a backup folder
# Can create a backup folder, or use a specified folder
# Can copy all surface level files in a directory
# Or can copy by type or by keyword in the file

# Default flag variables
file_name=""
file_type=""
default_dest_dir=""

# Grab flags
while getopts 'n:t:d:' flag; do
	case "$flag" in 
		n) file_name=$OPTARG;;
		t) file_type=$OPTARG;;
		d) default_dest_dir=$OPTARG;;
	esac
done

# Shift so we can skip flags in $@
shift $((OPTIND - 1))

# Go through all arguments
for src_dir in "$@"; do
	if [[ ! -d "$src_dir" ]]; then
		echo "Skipping non-directory: $src_dir"
		continue
	fi

	src_path=$(dirname "$src_dir")
	src_name=$(basename "$src_dir")

	# If -d wasn't used create a backup folder
	if [ "$default_dest_dir" == "" ]; then
		dest_dir="$src_path/${src_name}_backup"
		mkdir $dest_dir
		echo "Creating backup directory: $dest_dir"
	# If the specified directory doesn't exist then make it
	elif [[ ! -d "$default_dest_dir" ]]; then
		mkdir $default_dest_dir
		dest_dir=$default_dest_dir
		echo "Creating specified destination: $dest_dir"
	# Use what already exists and was specified
	else
		dest_dir=$default_dest_dir
		echo "Using specified destination: $dest_dir"
	fi

	# Copy each file within the directory
	for file in "$src_dir"/*"$file_name"*"$file_type"; do
		# Skip all non files
		if [[ ! -f $file ]]; then
			echo "Skipping directory: $file"
			continue
		fi

		# Copy the file to the destination
		cp "$file" "$dest_dir"
		echo "Copying file: $file into: $dest_dir"

	done
done