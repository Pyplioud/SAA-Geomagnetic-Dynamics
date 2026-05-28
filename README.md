# SAA Geomagnetic Dynamics

## Description
A project aiming to analyse the South Atlantic Anomaly by creating a mechanism to display its behaviours in a graphical way, as well as infering results based off of such results. 
The full project can be accessed in the ipynb file

## Objective
- Creating a Python program to understand the South Atlantic Anomaly in an accessible way.
- Organizing and infering different informations and conclusions by analysing the results obtained.
- Researching the scientific background behind the South Atlantic Anomaly to understand the topic through scientific research.
- Comparing the research with the inferences made, aiming to analyse the intersection between theorical findings and practical projects
  
## Scientific Background
The South Atlantic Anomaly (SAA) is a region of decreased intensity in the Earth's magnetic field, located over the South Atlantic. It poses potential risks to technological devices due to the proximity of the Van Allen radiation belt. The anomaly, the most significant in the geomagnetic field, has been documented for nearly a century but is believed to have existed for up to 900 years. Its intensity has increased and it has migrated westward, influenced by geological core dynamics such as the Coriolis effect and magnetic declination. Understanding the causes of this gain in intensity is complicated, as it results from chaotic movements within the Earth's outer core.

## Methodology
In order to develop the software, I utilized the Python library "ppigrf" to adquire information about the geomagnetic activity. Alongisde this tool, I used, amongst many others, "matplotlib", "cartopy" and "numpy" to plot the results in a worldwide scale inside the program Visual Studio Code. There were two different approaches to analyse the data from ppigrf:
- The first approach relies on the vertical component of the earth's magnetosphere
- The second approach aims to elucidate the intensity of the magnetic field as a whole

The inferences were developed only by observing the results gathered throughout the process, documented in the redults and discussion.
To construct the scientific research, a standard approach was used. Seeking to understand the anomaly through scientific studies, some extensive papers were used and documented in the project.


## Results
...

## Visualization

Vertical Component of the Magnetic Field

![Vertical Component of the Magnetic Field](notebooks/vertical_component.gif)

Total Intensity of the Magnetic Field

![Total Intensity of the Magnetic Field](notebooks/total_intensity.gif)

## Technologies Used
- Python
 - ppifrg
 - matplotlib
 - numpy
 - cartopy
