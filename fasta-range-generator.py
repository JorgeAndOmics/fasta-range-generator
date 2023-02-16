import argparse
import pandas as pd
from Bio import SeqIO

def generator(input_file, output_file, start, end):
    """
    This function reads in a dataframe from a file, concatenates the amino acid residues for each peptide into a single
    string, extracts a range of amino acids from each sequence, and writes the modified sequences to a new file.
    
    Parameters:
    -----------
    input_file : str
        The path to the input file containing the sequence data
    output_file : str
        The path to the output file where the modified sequences will be written
    start : int
        The starting index of the range of amino acids to extract
    end : int
        The ending index of the range of amino acids to extract
    
    Returns:
    --------
    None
    """
    # Read in the input file using Pandas
    if input_file.endswith('.csv'):
        df = pd.read_csv(input_file)
    elif input_file.endswith('.pkl'):
        df = pd.read_pickle(input_file)
    elif input_file.endswith('.feather'):
        df = pd.read_feather(input_file)
    else:
        raise ValueError("Input file must be a CSV, pickle, or feather file.")

    # Concatenate the amino acid residues for each peptide into a single string
    df['sequence'] = df.iloc[:, 1:].apply(lambda x: ''.join(x), axis=1)

    # Extract the range of amino acids from each sequence and store the results in a new column
    df['modified_sequence'] = df['sequence'].apply(lambda x: str(x[start-1:end]))

    # Write the modified sequences to a new file using BioPython
    records = [SeqIO.SeqRecord(Seq(row['modified_sequence']), id=row['id'], description='') for i, row in df.iterrows()]
    SeqIO.write(records, output_file, "fasta")

if __name__ == '__main__':
    # Define command line arguments
    parser = argparse.ArgumentParser(description='Extract a range of amino acids from each sequence in a CSV, pickle, or feather file and write the modified sequences to a new FASTA file.')
    parser.add_argument('input_file', type=str, help='Path to input file')
    parser.add_argument('output_file', type=str, help='Path to output file')
    parser.add_argument('start', type=int, help='Starting index of the range of amino acids to extract')
    parser.add_argument('end', type=int, help='Ending index of the range of amino acids to extract')

    # Parse the command line arguments
    args = parser.parse_args()

    # Call the generator function with the command line arguments
    generator(args.input_file, args.output_file, args.start, args.end)
