import numpy as np
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import argparse
import sys

# header 1: bias [V]    Total Current [A]    Pad Current [A]
# header 2: bias [V]        Current [A]

parser = argparse.ArgumentParser(description='Plot IV Curves from LabVIEW')
parser.add_argument('--fileNames', type=str, nargs='*',
                    default=['Data/HPK-Type-1.1-LG1-SE2-1/HPK-Type-1.1-LG1-SE2-1_2019-06-05_10.iv'],
                    help='name of the files with the data to be plotted')
parser.add_argument('--plotName', type=str,
                    default='plot',
                    help='Name of the plot (do not include the extension)')
parser.add_argument('--grounded', type=int,
                    default=1,
                    help='True: grounded meas (3 columns), False: floating meas (2 columns)')
args = parser.parse_args()

def pretty_name(f):
    f=f.split('/')[-1].split('_2019')[0]
    return f

colors = cm.rainbow(np.linspace(0, 1, len(args.fileNames)))
for count,f in enumerate(args.fileNames):
    with open(f) as myfile:
        contents = myfile.read()
    # keep only the part with the numbers we care about, and remove 'END'
    contents = contents.split('BEGIN')[-1].replace('END','')
    #print(contents)

    df = pd.read_csv(StringIO(contents), delim_whitespace=True, skip_blank_lines=True, header=None)

    grounded = args.grounded
    if (len(df.columns) < 3 and grounded) or (len(df.columns) >2 and not grounded):
        print('Attention! Check grounded parameter ')
        sys.exit()

    print('grounded?')
    print(grounded)
        
    if grounded: 
        df.columns=['bias [V]', 'Total Current [A]', 'Pad Current [A]']
        df['Guard Ring Current [A]'] = df['Total Current [A]'] - df['Pad Current [A]']
    else: df.columns=['bias [V]', 'Current [A]']

    # we want to visualize the absolute values 
    df=df.abs()

    #print(df)
    if count == 0:
        fig1, ax1 = plt.subplots()
        #ax1.grid(True)
    df.plot(kind='scatter',x=df.columns[0],y=df.columns[1], logy=True, color=colors[count], label=pretty_name(f), ax=ax1)    

    if grounded:
        if count == 0:
            fig2, ax2 = plt.subplots()
            fig3, ax3 = plt.subplots()
        df.plot(kind='scatter',x=df.columns[0],y=df.columns[2], logy=True, ax=ax2, color=colors[count], label=pretty_name(f))
        df.plot(kind='scatter',x=df.columns[0],y=df.columns[3], logy=True, ax=ax3, color=colors[count], label=pretty_name(f))

ax1.grid(True)
if grounded:
    ax2.grid(True)
    ax3.grid(True)
fig1.savefig(args.plotName+'_total.pdf')
fig2.savefig(args.plotName+'_pad.pdf')
fig3.savefig(args.plotName+'_guardring.pdf')

