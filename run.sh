#!/bin/bash

# Function to run merge_pdfs.py with arguments
run_merge_pdfs() {
    echo "Enter arguments for merge_pdfs.py, separated by spaces (e.g., file1.pdf file2.pdf):"
    read -ra args
    python merge_pdfs.py "${args[@]}"
}

# Main menu function
main_menu() {
    echo "Select an option:"
    echo "1) Merge PDFs"
    echo "2) Quit"
    read -p "Enter your choice: " choice

    case $choice in
        1)
            echo "Running merge_pdfs.py..."
            run_merge_pdfs
            ;;
        2)
            echo "Exiting script."
            exit 0
            ;;
        *)
            echo "Invalid option!"
            main_menu
            ;;
    esac
}

# Start the script
main_menu
