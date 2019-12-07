Reflection and comments on the app and development process:

Our biggest challenge in developing the app, still focusses on the app layout and displaying the interactivity tools (e.g drop down menus) close to the plots to maximize user exploratory analysis experience. We realized this during the dry test activity perform on the lab with our peers.


### Summary of fixes performed for milestone 3.

1. Change code separating functions into separate files to make it more readable and robust (less supceptible to editing mistakes)
2. Added PEP8 Docstring to functions of plots.
3. Reduce length of instructions as per TA feedback to avoid overwhelming the user.

# ------------ TO BE DELETED AFTER SOLVING ISSUE----------------- 

# We need to decide which of these to keep or Move to Wish list if we cannot solve now.

4. Solve issue with Alabama state having not data in the Heat map, rather than plotting the state with not data, the plots automatically removes it. 

4. Alternative solution to heatmap issue mentioned by TA on States plotting with not data, is to add a warning Text indicating that App only plots available data. If something does not plot is because there is not data to plot.

#-------------TO BE DELETED AFTER SOLVING ISSUE------------------

5. Adjusted dropdown menu select words and plot in the app ("No damage" is same a "None") to be consistent.
6. Reduce number of question and plot size to fit shorten distance between plot and interactive dropdown tool menus.

### Bug fixes and Features Wish List

Here is a list of all items we wish to improve but did not have time for milestone 3:

1. Option to show data over months rather then years, allowing for "yearly cycle" analysis as well
2. **Update bird count when year slide range changes**?
3. Add a cross line guides feature together with the mouse interactive tool to explore the heat map. This will prevent user from getting lost when there are so many features to explore.
4. Import feature that could use the same plots layout and automatically generate them using different data.

### Summary of Suggestions (from TA and Lab Session peers) not implemented.

Below is a summary of the suggested improvements we decided not to implement. We try to give a brief explanation of why not. We are thankful anyway to all the first users for their time and their valua feedback. 

1. Did not implement the suggestion from TA of having a separate plot for No damage category only, the team believes it is more valuable to easily compare the different types of damage on the same plot, even if only proportionally. User can always deselect this category using the dropdown menu.
2. Did not include, city and state in the heat map as suggested during the lab feedback. It is not the purpose of the tool to teach geography.  
3. Organize x axis by flight phase in the bar chart (Lab Session feedback). This is more of a nice to have. Bar chart is ordered to from smallest to biggest. 
4. Change area chart to line plot. Area plot is more aesthetic that a simple line plot and the interaction tools help use remove the confusion if any.   


### Lab Activity Feedback Summary

A list of summarizing all the issues can be found under issue 41 of the python repository:

https://github.com/UBC-MDS/Group_105/issues/41

In general, the app is not all difficult to use. However, it was noticed by all of us when acting as "fly in the wall" that because the plots were on the bottom and controls on the top, the user started clicking without observing the changes on the plot and got confused. Thus, our focus from such activity is to try solving the following (if time permits):

1. Reducing the number of questions to allow the controls and plots be vissible at the same time.
2. Modify labels of plots to include units, so user understand they are looking at Total number of bird strikes and not average. 
3. Resize the plots if still they do not fit together with the test. We might consider moving the list of questions to another tab.
4. Keep consistency dropdown select words in the app ("No damage" is same a "None")








Did not implament peer feedback from thursdays lab, it was already thursday....

