# DSCI 532 App Creation - Group 105

created by: Evhen Dytyniak, Tani Barasch, and Robert Pimentel  

[Aircraft Birdstrikes App](https://group-105-milestone2.herokuapp.com/)
  
### Description:  
The purpose of the app is to investigate the effect of birdstrikes on aircraft between 1990 and 2002 in the United States.
Different factors (flight phase, time of day, and bird size) and regions (states / airports) are explored, visualizing four classes of damage to aircraft. Aiming to do so with 3 graphs arranged in two tabs.

##### Tab 1: 
In this tab, the left graph shows the number of birdstrikes over time, with the different damage levels - coloured. And on the right a bar chart showing the number of birdstrikes (Y axis) over one of three cetegories: 'Flight Phase', 'Time of Day', or "Bird Size".

- **Damage Type**: multi-choice dropdown menu, located in the top left of the screen to choose which damage types to be showen in the graphs: Substantial, Medium, Minor, or No damage (any combination of the 4 options), each assigned a different colour.
- **Date Range Between**: slider bar, located above the area chart, allows for customization of range of years for which to show data.
- **Factor**: dropdown, located above the bar chart, allows choosing X-axis variable for the bar chart.

Image of the tab below:
!["Bird Strikes by Factor"](https://github.com/TBarasch/Group_105/blob/master/imgs/2_charts.jpg?raw=true)



##### Tab 2:
A single heatmap that shows number of strikes over time (X axis) by location (Y axis), allowing for the following costumization:

- **Damage Type**: multi-choice dropdown menu, located in the top left of the screen to choose which damage types to be showen in the graphs: Substantial, Medium, Minor, or No damage (any combination of the 4 options), each assigned a different colour.
- **Location Type**: dropdown, located above the heatmap chart, allowes for specification of one of two types of location, the State or the Airport from which the flight took off.

Image of the tab below:
![](https://github.com/TBarasch/Group_105/blob/master/imgs/heatmap.jpg?raw=true)



Original [project proposal](project_proposal.md).
Original [Sketch](https://github.com/TBarasch/Group_105/blob/master/imgs/App_Sketch_1_D1.png?raw=true).
