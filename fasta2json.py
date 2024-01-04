# import argparse
# from sys import stdin,stdout

# # parse arguments
# def parseArgs():
#     parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
#     parser.add_argument('-i', '--input', required=False, type=argparse.FileType('r'), default=stdin, help="Input FASTA")
#     parser.add_argument('-o', '--output', required=False, type=argparse.FileType('w'), default=stdout, help="Output")
#     args = parser.parse_args()
#     return args.input, args.output


file_path = "/home/clement/projects/UTILS/test.fasta"


def read_fasta(in_file):
    fasta_dict = dict()
    seq = ""
    name = ""
    for line in in_file:
        line = line.rstrip("\n")
        if line[0] == ">":
            seq = ""
            line = line.replace(">","")
            name = line
        else:
            seq += line
            fasta_dict[name] = seq
    return fasta_dict


with open(file_path, "r") as f:
    fasta = read_fasta(f)
    print(fasta)

