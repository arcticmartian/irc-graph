import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as tck
# Installing python libraries:
# pip install matplotlib pandas
# python -m pip <library> linux
# py -m pip <library> Windows


# Opens file, must be located in the same directory as the .py file
file_name = 'IRC_Glu-Asp.csv' # The file in this directory

# Reads the file as a pandas data file
data = pd.read_csv(file_name, delimiter=';')


# Set the colors in hexadecimal or in english in case of basic colors 
axis_color = 'black'
data_color = '#1f77b4' # Blue
data_color2 = 'red'

# Create a figure and a set of subplots
fig, ax = plt.subplots()
# minor stiks 
ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
ax.xaxis.set_minor_locator(tck.AutoMinorLocator())

# Set the columns in pandas. data.iloc[:,0] = column 0
#x = data.iloc[:,0]
#y1 = data.iloc[:,1]
#y2 = data.iloc[:,2]

# Represents the graphs
# ax.plot(x, y, linestyle='', marker='', markersize='', color='', label='')
ax.plot(data.iloc[:,0], data.iloc[:,1], linestyle='-', marker='.', markersize=1, color='#FB6F6F', label='Glu')
ax.plot(data.iloc[:,0], data.iloc[:,2], linestyle='-', marker='.', markersize=1, color='#F9A686', label='Glu-2TS')
ax.plot(data.iloc[:,0], data.iloc[:,3], linestyle='-', marker='.', markersize=1, color='#008080', label='Asp')
ax.plot(data.iloc[:,0], data.iloc[:,4], linestyle='-', marker='.', markersize=1, color='#80ACA3', label='Asp-2TS')

# First and last value of the first column.
#x1 = (data.iloc[:,0][0])
#x2 = (data.iloc[:,0][len(data.iloc[:,0]) - 1])
#y1 = (data.iloc[:,1][0])
#y2 = (data.iloc[:,1][len(data.iloc[:,1]) - 1])

# Also first and last value of the first column
column = data.iloc[:,0]
x1 = (column[0])
x2 = (column[len(column) - 1])
column = data.iloc[:,1]
y1 = (column[0])
y2 = (column[len(column) - 1])

# Graph limits
ax.set_xlim(-14, 714)
ax.set_ylim(-39, 27)

# Aspect ratio, (x/y)/(aspect/ratio), if we want an aspect ratio of 16:9,
# 1) We calculate the difference between the limits in x (671 - 1) and multiply it by 9
# 2) We calculate the difference between the limits in y (67 - -40) and multiply it by 16
# (670/107)/(16/9).
ax.set_aspect((733/63)/(20/9))

# Labels
ax.set_xlabel('Intrinsic Reaction Coordinate', color=axis_color)
#ax.set_xlabel(data.columns[0], color=axis_color)
ax.set_ylabel('ΔE (kcal/mol)', color=axis_color)
ax.legend(frameon=False)

# Saves the generated graph in the same directory as the .py file
fig.savefig("irc.svg")
# Shows the graph in the terminal
plt.show()