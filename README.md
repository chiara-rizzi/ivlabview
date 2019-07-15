# IV Curves

What you can find in this README
* [How to take data at the probe station](#takedata)
* How to plot the data starting from the LabVIEW files

## Take data

Once in the lab: 

1. Turn on computer
  * For LabView: select Windows 
  * Password: 161-lab-enter (make sure keyboard is on FRA French (Switzerland))
2. Documents —> Labview project —> cviv-daq —> double click on CVIV 

A list of options opens in LLB Manager. Select CV-IV-control.vi and click on arrow in the bar menu (to go from “modification” mode to “user” mode).

### Settings
###### Sample and environment parameters
* Device name: write sensor name 
* Select pFZ (it puts the voltage to negative) 
* Tester: put your name

###### Basic measurement conditions
* Type of measurement - choose one of these (depending on what you want to do)
  *IV: floating guard ring 
  *IV with two I-meter: grounded guard ring

###### Measurement configuration
* Start: -0
* Stop: -140 (it depends on the sensor!!) 
* Number of steps: 70 (calculate the number of steps such that you have steps of 2V) 
* Compl. Stop: ON

###### Instruments settings
* GPIB: 21
* Integration time: 3 [20 ms]
* Averaging (count): 3 
* Compliance: 1e-6 

### Start
* Remember to check that boh keithleys are powered 
* To start: Start measurement 

### Plots 
While taking the measurement, the following plots are produced:
* Total current: pad + guard ring 
* Pad current: only the sensor 
Guard ring only: difference between total and pad currents. 

*Note*: the plots from labview show the signed values, so new points (higher absolute value of voltage, but lower signed value) appear on the left.

### Where's the data?
* Data is stored in Documents —> Labview project —> cviv-daq —> CVIV folder
* Text files can be plotted with the python code described below

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