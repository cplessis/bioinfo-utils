import argparse, json

# COLORS
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# =====================
#       PARSER
# =====================
def parseArgs():
    parser = argparse.ArgumentParser(description="This program convert a FASTA file to a JSON format")
    parser.add_argument('-i', '--input', help="Input FASTA", type=argparse.FileType('r'), required=True)
    parser.add_argument('-o', '--output', help="Output", type=argparse.FileType('w'), required=True)
    args = parser.parse_args()
    return args.input, args.output

input_file, output_file = parseArgs()

if input_file.name.split(".")[-1] != "fasta":
    print(f"\n{col.FAIL}Error : file {col.WARNING}{input_file.name}{col.FAIL} not in FASTA format.{col.ENDC}\n")
    exit()
if output_file.name.split(".")[-1] != "json":
    print(f"\n{col.FAIL}Error : file {col.WARNING}{output_file.name}{col.FAIL} not in JSON format.{col.ENDC}\n")
    exit()

# =====================
#     FASTA READER
# =====================
def read_fasta(in_file):
    fasta_dict = dict()
    seq = ""
    name = ""
    n = 0
    for line in in_file:
        line = line.rstrip("\n")
        if line[0] == ">":
            n +=1
            seq = ""
            line = line.replace(">","")
            name = line
            print(n, name)
        else:
            seq += line
            fasta_dict[name] = seq
    return fasta_dict

# =====================
#       PROCESS
# =====================
print(f"\nProcessing {col.OKGREEN}{input_file.name}{col.ENDC} ...\n")

fasta = read_fasta(input_file)
json.dump(fasta, output_file, indent = 4)

# CLOSE ALL FILES
input_file.close()
output_file.close()

print(f"\nFile successfully exported as {col.OKGREEN}{output_file.name}{col.ENDC}")