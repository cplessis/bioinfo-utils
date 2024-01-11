import plotly.express as px
import pandas as pd
from glob import glob
import argparse

parser = argparse.ArgumentParser(description="This program convert a FASTA file to a JSON format")
parser.add_argument('-i', '--files-path', help="Path to LOG file from pear", required=True)
parser.add_argument('-o', '--output-path', help="Path to output directory", required=True)
args = parser.parse_args()

files_path, out_path = args.files_path, args.output_path

ar = "Assembled reads ."
dr = "Discarded reads ."
nar = "Not assembled reads ."

def val_dict(sample,line,val_type):
    v = line.split()
    r = int(v[-2].replace(",",""))
    v = int(v[-4].replace(",",""))
    return dict(
        sample=sample,
        total_reads=r,
        reads=v,
        ratio=v/r,
        type=val_type
    )

res_list = []
for file_path in glob(f"{files_path}/*.log"):
    print(file_path)
    sample = file_path.split("/")[-1].rstrip(".log")
    with open(file_path,"r") as file:
        for line in file:
            if line.startswith(ar):
                res_list.append(
                    val_dict(sample,line,"assembled")
                )
            elif line.startswith(dr):
                res_list.append(
                    val_dict(sample,line,"discarded")
                )
            elif line.startswith(nar):
                res_list.append(
                    val_dict(sample,line,"not_assembled")
                )
            else:
                pass


df = pd.DataFrame(res_list)
fig = px.bar(
    df, x="reads", y="sample", color='type', orientation='h',
    color_discrete_sequence=["blue", "red", "goldenrod"],
    hover_data=["reads","ratio"],
    title='PEAR STATS'
    )

fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})

fig.write_html(f"{out_path}/pear.html")
