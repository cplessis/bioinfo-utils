import argparse

# =====================
#       PARSER
# =====================
def parseArgs():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('-i', '--input', required=False, help="Input FASTA", required=True)
    parser.add_argument('-o', '--output', required=False, help="Output", required=True)
    args = parser.parse_args()
    return args.input, args.output

input_path, output_path = parseArgs()


# =====================
#     FASTA READER
# =====================
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

# =====================
#       PROCESS
# =====================

# INPUT FILE
with open(input_path, "r") as infile:
    fasta = read_fasta(infile)
    print(fasta)


## OUTPUT FILE
# with open(output_path, "w") as outfile:
    # to complete
