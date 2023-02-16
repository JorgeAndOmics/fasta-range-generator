# Fasta Range Generator

Fasta Range Generator is a Python script that extracts a range of amino acids from a set of protein sequences and writes the modified sequences to a new file in the FASTA format.

## Table of Contents

-   Installation
-   Usage
-   Usage Example
-   Examples
-   Contributing
-   License

## Installation

To use this script, you will need to have Python 3.6 or later installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Once you have Python installed, you can download and run the script using the following command:

`git clone https://github.com/your-username/fasta-range-generator.git
cd fasta-range-generator
python fasta-range-generator.py input_file output_file start end` 

## Usage

The Fasta Range Generator script takes the following command line arguments:

-   `input_file`: the path to the input file containing the sequence data (CSV, pickle, or feather file)
-   `output_file`: the path to the output file where the modified sequences will be written (FASTA file)
-   `start`: the starting index of the range of amino acids to extract (integer)
-   `end`: the ending index of the range of amino acids to extract (integer)

To run the script, open a terminal or command prompt, navigate to the directory containing the `extract_aa_range.py` file, and enter the following command:

sqlCopy code

`python fasta-range-generator.py input_file output_file start end` 

Replace `input_file`, `output_file`, `start`, and `end` with the appropriate values for your input file and desired range of amino acids.

## Usage Example

Suppose we have a CSV file named `my_sequences.csv` containing the following protein sequences:



We want to extract amino acids 2-4 from each sequence and write the modified sequences to a new file named `modified_sequences.fasta`. We can do this using the following command:
| id | aa1 | aa2 | aa3 | aa4 | aa5 |
|----|----|----|----|----|----|
| 1 | A | V | L | G | S |
| 2 | S | L | E | K | V |
| 3 | K | G | A | Y | F |
| 4 | V | T | I | D | E |

We want to extract amino acids 2-4 from each sequence and write the modified sequences to a new file named `modified_sequences.fasta`. We can do this using the following command:

    python fasta-range-generator.py my_sequences.csv modified_sequences.fasta 2 4

The script will read in the `my_sequences.csv` file, concatenate the amino acid residues for each peptide into a single string, extract aminoacid residues 2-4 from each sequence, and write the modified sequences to the `modified_sequences.fasta` file in the FASTA format. The resulting file will contain the following sequences:

    >1
    VLG
    >2
    LEK
    >3
    GAY
    >4
    TID

## Examples

Here are some example command line invocations of the script:

Extract amino acids 2-4 from a CSV file containing protein sequences:

    python fasta-range-generator.py my_sequences.csv modified_sequences.fasta 2 4

Extract amino acids 10-20 from a pickle file containing protein sequences:

    python fasta-range-generator.py my_sequences.pkl modified_sequences.fasta 10 20 

Extract amino acids 5-15 from a feather file containing protein sequences:

    python fasta-range-generator.py my_sequences.feather modified_sequences.fasta 5 15

## Contributing

If you would like to contribute to the Fasta Range Generator script, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the terms of the MIT license. See the `LICENSE` file for more information.
