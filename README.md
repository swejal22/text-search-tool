# Text Search Tool using File Handling in Python

This is a Python program that allows users to search for a specific text string within one or multiple files located in a specified directory. The search results will be written to a separate output file.

## Requirements

- Python 3.x installed on your computer

- Basic understanding of file handling in Python

- Ability to use the command-line interface

## Usage

1. Clone or download this repository to your local machine.

2. Navigate to the project directory in the terminal or command prompt.

3. Run the text_search.py script:

```bash
python text_search.py
```

4. The program will prompt you to enter the text string you want to search for.

5. Enter the input file or directory path. If you want to search in the current directory, simply press Enter.

6. Enter the output file path where the search results will be saved.

7. The program will perform the search and write the results to the output file.

## Functionality

The program contains the following functions:

1. **text_search(search_string, input_path, output_file):** This function searches for the specified text string within one or multiple files in the given input directory or file path. The search results are saved to the output file.

2. **process_file(file_path, search_string, result_file):** This function processes a single file to search for the text string and writes the file name and line number to the output file if a match is found.

3. **main():** This function handles the user input, prompts, and calls the **text_search** function with the provided parameters.

## Note

- If you provide a file path as the input, the program will search for the text string within that specific file.

- If you provide a directory path as the input, the program will search for the text string in all text files within that directory and its subdirectories.

- The program uses regular expressions to perform the text search, allowing for flexible and powerful pattern matching.

- If any errors occur during the process, the program will display informative error messages to help you troubleshoot the issue.

- The search results will be written to the output file in the format **"file_path:line_number"** for each match found.

## Contributing

Contributions to this project are welcome. Feel free to open issues or submit pull requests if you have any suggestions or improvements.