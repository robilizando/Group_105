## Maintenance of Python Dashboard

Certain elements were prioritized over others when determining a workflow for maintenance. Since our app was working without any bugs, the primary goal was to clean up the code to make it easier to read and reproducable; the idea was that this would allow for easier maintenance and feature updates in the future. Next, it was important to incorporate the feedback from our peers and TA; there were certain elements of the dashboard that could immediately be addressed to make the overall experience more engaging. Ideally more feedback would be required. Next, the principles of creating effective dashboards would be reviewed and the dashboard adjusted as required _(no time for this element)_. Finally, additional features would be added _(no time for this element)_. Items completed and outstanding are listed below:

### Outstanding

---

1. Implement feedback you receive from peers during Lab 3's feedback session  
  - __TA feedback__:  
    - ensuring all states and airports appear on the map consistently, regardless of damage type, needs to be addressed  
  - organization of selectors and examples needs to be further examined and optimized for user experience  
2. If needed, reorganize and restructure your files/directory structure to separate different structures (see the [Dash docs](Structuring a Multi-Page App) for suggested organizations) 
  - not necessarily required for this project  
3. Apply principles of creating effective dashboards (Lecture 4)  
4. Implement any new features (if time permits)  
  - need to figure out how to have plots size and scale automatically instead of setting property sizes of the Iframes and altair sizes.   


### Completed

---

1. Implement known bug-fixes and work-arounds  
  - non known issues to fix  

2. Implement feedback you receive from peers during Lab 3's feedback session:  
  - __TA feedback__:    
    - examples not removed, provide guidance to users. Peer reviewers thought enclusion was useful.  
    - another plot for no damage was not created - this would clutter the page too much. The idea was to demonstrate that no-damage birdstrikes dwarf damage causing birdstrikes and an overlay best demonstrates this. A user would only look at either damage causing birdstrikes together or non-damage causing birdstrikes.   
  - __Peer feedback__:  
    - direction was added to each selector identifying what plot it controls/adjusts  
    - changed damage type in dropdown to match legend of plots  
    - no change to the y-axis needed  
    - no change to area plot vs line plot  
    - bar chart is ordered in ascending order, x-axis is not meant to be "ordered"  
    - city's not provided in data set  

3. Clean-up and refactor code to make it more readable   
    - Added margins to dashboard  
    - Consolidated tab content to be a list under the tab callback for both tabs (instead of returning two dbc elements at the callback return)
    - Changed tab colour and background colour
    - changed size of plots to better fit on a 1080p laptop screen  
    - `mds_special` theme added  
    - changed legend size for better readability  
    - added tooltips to line plot over time  
    - changed dcc object names to properly reflect their type  
    - removed unneeded code 
    - corrected grammar and added additional content on number of states represented   

4. Reformat your code and add docstrings (PEP8 style)  



