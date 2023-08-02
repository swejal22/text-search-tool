import os
import re


def text_search(search_string, input_path, output_file):
    try:
        with open(output_file, "w") as result_file:
            if os.path.isfile(input_path):
                process_file(input_path, search_string, result_file)
            elif os.path.isdir(input_path):
                for root, _, files in os.walk(input_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        process_file(file_path, search_string, result_file)
    except Exception as e:
        print(f"Error: {e}")
        raise


def process_file(file_path, search_string, result_file):
    try:
        with open(file_path, "r") as file:
            for line_number, line in enumerate(file, 1):
                if re.search(search_string, line):
                    result_file.write(f"{file_path}:{line_number}\n")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        raise


def main():
    try:
        search_string = input("Enter the text string to search for: ")
        input_path = input(
            "Enter the input file or directory path (Press Enter for current directory): "
        ).strip()
        output_file = input("Enter the output file path: ")

        if not input_path:
            input_path = "."  # Use the current directory if no path is provided

        text_search(search_string, input_path, output_file)
        print("Search results have been written to", output_file)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
