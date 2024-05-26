import os
import sys
import pandas as pd
from japanmap import picture
import matplotlib.pyplot as plt
import argparse

def map_draw(
    csv_path,
):
    title = os.path.splitext(os.path.basename(csv_path))[0]
    df = pd.read_csv(csv_path, index_col = 0)
    cmap = plt.get_cmap('Reds')
    norm = plt.Normalize(vmin=df.value.min(), vmax=df.value.max())
    fcol = lambda x: '#' + bytes(cmap(norm(x), bytes=True)[:3]).hex()
    
    fig, ax = plt.subplots()
        
    plt.colorbar(plt.cm.ScalarMappable(norm,
        cmap,
        # cax=ax.inset_axes([0.95, 0.1, 0.05, 0.8])
    ))
    plt.imshow(picture(df['value'].apply(fcol)))
    plt.title(title, fontname="Hiragino sans")
    plt.savefig(title)
    plt.show()


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='draw color japan map from csv file')    

    parser.add_argument('csv_path', help='path to csv file')    

    args = parser.parse_args() 

    if os.path.splitext(os.path.basename(args.csv_path))[1]!='.csv':
        print('Input_error')
        sys.exit()

    map_draw(args.csv_path)