# IV Curves

What you can find in this README
* [How to take data at the probe station](#takedata)

## Take data


## How to plot the data

Example:
```
python plot_curves.py --fileNames Data/HPK-Type-1.1-LG1-SE2-1/HPK-Type-1.1-LG1-SE2-1_2019-06-05_10.iv Data/HPK-Type-1.1-LG1-SE2-1/HPK-Type-1.1-LG1-SE2-1_2019-06-05_14.iv --grounded 1 --plotName my_HPK_plot
```

Running:
```
python plot_curves.py --help
```

will display this help:

```
optional arguments:
  -h, --help            show this help message and exit
  --fileNames [FILENAMES [FILENAMES ...]]
                        name of the files with the data to be plotted
  --plotName PLOTNAME   Name of the plot (do not include the extension)
  --grounded GROUNDED   True: grounded meas (3 columns), False: floating meas
                        (2 columns)

```