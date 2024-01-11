import plotly.express as px
import pandas as pd
from glob import glob
import argparse

parser = argparse.ArgumentParser(description="This program export LOGs from PEAR to HTML report.")
parser.add_argument('-i', '--files-path', help="Path to LOG file from pear", required=True)
parser.add_argument('-o', '--output-path', help="Path to output directory", required=True)
parser.add_argument('-t', '--out-type', help="Row number of reads (reads) or % (ratio)", default="reads", choices=["reads", "ratio"])
args = parser.parse_args()

files_path, out_path, out_type = args.files_path, args.output_path, args.out_type

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
    df, x=out_type, y="sample", color='type', orientation='h',
    color_discrete_sequence=["#6495ED", "#DE3163", "#FF7F50"],
    hover_data=["reads","total_reads","ratio"],
    title='PEAR STATS',
    text=df['ratio'].apply(lambda x: f"{x*100:.1f}%")
    )

fig.update_layout(
    xaxis_title="Reads number", yaxis_title="Sample name",
    template='gridon',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)'
)

print("Writing HTML ...")
fig.write_html(f"{out_path}/pear.html")
