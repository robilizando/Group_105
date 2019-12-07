import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime as dt
import pandas as pd
import altair as alt
import dash_bootstrap_components as dbc
alt.data_transformers.disable_max_rows()

df = pd.read_csv('https://raw.githubusercontent.com/UBC-MDS/Group_105/master/data/birdstrikes_clean.csv')

app = dash.Dash(__name__, assets_folder='assets', external_stylesheets=[dbc.themes.CERULEAN])
app.config['suppress_callback_exceptions'] = True

server = app.server
app.title = 'Aircraft Birdstrikes in the USA'


# DBC & HTML COMPONENTS
#===================================

title_header = dbc.Jumbotron(fluid = True, children = [
    dbc.Container(fluid = True, children = [
            dbc.Row([
                dbc.Col([
                    html.Img(src='https://cdn.pixabay.com/photo/2012/04/16/13/55/swans-36088_960_720.png', 
                        width='100%')
                ], width = 2),
                dbc.Col([
                    html.H1("Aircraft Bird Strikes"),#, className="display-3"),                 
                    dcc.Markdown(
                        '''
                        The purpose of the app is to investigate the effect of birdstrikes on aircraft between 1990 and 2002 in the United States for 29 states.   
                        Different factors (flight phase, time of day, bird size) and regions (states, airports) are explored, visualizing four classes of damage to aircraft.   


                        The aim of __Tab 1__ is to visualize the trend of, number of, and damage caused by birdstrikes between 1990 and 2002.   
                        The visualizations in this tab explore what factors affect the number and of and damage caused by bird strikes.

                        The aim of __Tab 2__ is to explore which states and airports observed the largest number of bird strikes between 1990 and 2002.

                        '''
                    )  
                ])
            ]),
        ],
    )],
)

dropdown_selector_tab1 = dcc.Dropdown(
    id = 'damage_types_dropdown_tab1',
    options = [
        {'label': 'None Damage', 'value': 'None'},
        {'label': 'Minor Damage', 'value': 'Minor'},
        {'label': 'Medium Damage', 'value': 'Medium'},
        {'label': 'Substantial Damage', 'value': 'Substantial'}
    ],
    multi = True,
    value = ['Minor', 'Medium', 'Substantial'],
    style = dict(width = '60%')
)

dropdown_selector_tab2 = dcc.Dropdown(
    id = 'damage_types_dropdown_tab2',
    options = [
        {'label': 'None Damage', 'value': 'None'},
        {'label': 'Minor Damage', 'value': 'Minor'},
        {'label': 'Medium Damage', 'value': 'Medium'},
        {'label': 'Substantial Damage', 'value': 'Substantial'}
    ],
    multi = True,
    value = ['None', 'Minor', 'Medium', 'Substantial'],
    style = dict(width = '60%')
)

rangeslider_selector = dcc.RangeSlider(
    id = 'date_slider',
    marks = {i: '{}'.format(i) for i in range(1990, 2002)},
    count = 12,
    min = 1990,
    max = 2002,
    step = 1,
    value = [1990, 2002]
)

dropdown_barchart = dcc.Dropdown(
    id = 'bar_dropdown',
    options = [
        {'label': 'Flight Phase', 'value': 'flight_phase'},
        {'label': 'Time of Day', 'value': 'time_of_day'},
        {'label': 'Bird Size', 'value': 'bird_size'}
    ],
    value = 'flight_phase',
    style = dict(width = '48%')
)

dropdown_heatmap = dcc.Dropdown(
    id = 'heatmap_dropdown',
    options = [
        {'label': 'State', 'value': 'state'},
        {'label': 'Airport', 'value': 'airport'},
    ],
    value = 'state',
    style = dict(width = '30%')
)

line = html.Iframe( 
    sandbox = 'allow-scripts',
    id = 'line_plot',
    height = '550',
    width = '750',
    style = {'border-width': '0'}
)

bar = html.Iframe(
    sandbox = 'allow-scripts',
    id = 'bar_plot',
    height = '550',
    width = '650',
    style = {'border-width': '0'}
)

heatmap = html.Iframe(
    sandbox = 'allow-scripts',
    id = 'heatmap_plot',
    height = '1100',
    width = '1000',
    style = {'border-width': '0'}
) 
 

#TAB OBJECTS AND CALLBACK
#===================================

tab1_selectors = \
    [dbc.Row([
            dbc.Col(children = [
                html.H5("Damage Type"),
                html.H6("Plot: Both"),
                dropdown_selector_tab1,
                html.Br()
            ])
        ]),
        dbc.Row(children = [
            dbc.Col(children = [
                html.H5("Date Range Between 1990 - 2002"),
                html.H6("Plot: Bird Strike Damage Over Time"),
                rangeslider_selector,
                html.Br(),
                html.Br()]),
            dbc.Col([
                html.H5("Factor"),
                html.H6("Plot: Effect of (factor) on Birdstrikes"),
                dropdown_barchart,
                html.Br()],
            ),
        ]),
        dbc.Row([
            dbc.Col([
                html.Hr()
            ])
        ]),
        dbc.Row([
            dcc.Markdown(
                '''
                __Example Questions__  
                Using the interactive tools above, try answering the following:    

                - How has the number of bird strikes causing substantial damage changed between 1994 and 1999?    
                - What is the difference between birdstrikes causing minor damage and medium damage in 1996?   
                - What time of day results in the most birdstrikes causing substantial damage?  
                - What is the difference between the number of large bird and small bird birdstrikes that caused no damage?  
                '''
            )
        ]),
        dbc.Row([
            dbc.Col([
                html.Hr()
            ])
        ])
    ]

tab2_selectors = \
[
dbc.Row([
        dbc.Col(children = [
            html.H5("Damage Type"),
            html.H6('Plot: Birdstrikes by Location'),
            dropdown_selector_tab2,
            html.Br(),
            html.H5("Location Type"),
            html.H6('Plot: Birdstrikes by Location'),
            dropdown_heatmap,
            html.Hr(),
            dcc.Markdown(
            '''
            __Example Questions__  
            Using the interactive tools above, try answering the following:    

            - What state experienced the most birdstrikes and in what year?  
            - What airport experienced the most birdstrikes and in what year and state did this occur?  
            - What states experienced the most birdstrikes causing minor damage and in what year did this occur?
            '''
            ),
            html.Hr()
            ],
        ),
    ])
]

tabs = \
html.Div(children = [
    dcc.Tabs(id="tabs", value='tab-1', 
            style = {'padding-left': '130px',
                    'padding-right': '130px'}, 
            colors={"border": "white",
                    "primary": "dodgerblue",
                    "background": "AliceBlue"},
            children=[
                dcc.Tab(label='Tab 1 - Bird Strikes Trends & Factors', value='tab-1'),
                dcc.Tab(label='Tab 2- Bird Strikes by Location', value='tab-2'),
            ]),
            html.Div(id='tabs-content')#, style = {'backgroundColor':'tan'})
])

@app.callback(Output(component_id ='tabs-content',component_property = 'children'),
              [Input(component_id = 'tabs', component_property = 'value')])
def display_tabs(tab):
    """
    Creates a dbc container with all elements to be displayed in a selected tab

    Parameters
    ----------
    tab - a string; user selected from a choice of tabs and passed by callback

    Return
    ------
    A dbc container object for a selected tab
    """
    if tab == 'tab-1':
        tab_1_container = \
            dbc.Container(#style = {'padding-left': '100px', 'padding-right':'100px'}, #for future reference
                fluid = True, 
                children = [
                    dbc.Row(children = [
                                dbc.Col(width = 1), 
                                dbc.Col([
                                    *tab1_selectors,
                                    dbc.Row([dbc.Col([line]), #width = 6),
                                            dbc.Col([bar]), #width = 6),
                                            ])
                                        ]),
                                dbc.Col(width = 1)
                            ]
                    )           
                ]
            )
        return tab_1_container
        
    elif tab == 'tab-2':
        tab_2_container = \
            dbc.Container(
                fluid = True, 
                children = [
                    dbc.Row(children = [
                                dbc.Col(width = 1),
                                dbc.Col([
                                    *tab2_selectors,
                                    dbc.Row([dbc.Col([heatmap])])
                                ]),
                                dbc.Col(width = 1)
                            ])  
                ]
            )  
        return tab_2_container


# APP LAYOUT
#==========================

app.layout = html.Div([title_header,
                       tabs,
                       dcc.Markdown(
                           '''
                           [Photo Attribution](https://pixabay.com/vectors/swans-silhouette-black-flying-36088/)
                           '''
                       )])

# CUSTOM ALTAIR THEME
#==========================
def mds_special():
    """
    creates an altair theme

    Parameters
    ----------

    Return
    ------
    A dictionary object that can be used to set an altair theme
    """
    font = "Arial"
    axisColor = "#000000"
    gridColor = "#DEDDDD"
    return {
        "config": {
            "title": {
                "fontSize": 20,
                "font": font,
                "anchor": "start", # equivalent of left-aligned.
                "fontColor": "#000000"
            },
            'view': {
                "height": 300, 
                "width": 400
            },
            "axisX": {
                "domain": True,
                #"domainColor": axisColor,
                "gridColor": gridColor,
                "domainWidth": 1,
                "grid": False,
                "labelFont": font,
                "labelFontSize": 12,
                "labelAngle": 0, 
                "tickColor": axisColor,
                "tickSize": 5, # default, including it just to show you can change it
                "titleFont": font,
                "titleFontSize": 16,
                "titlePadding": 10, # guessing, not specified in styleguide
                "title": "X Axis Title (units)", 
            },
            "axisY": {
                "domain": False,
                "grid": True,
                "gridColor": gridColor,
                "gridWidth": 1,
                "labelFont": font,
                "labelFontSize": 14,
                "labelAngle": 0, 
                #"ticks": False, # even if you don't have a "domain" you need to turn these off.
                "titleFont": font,
                "titleFontSize": 16,
                "titlePadding": 10, # guessing, not specified in styleguide
                "title": "Y Axis Title (units)", 
                # titles are by default vertical left of axis so we need to hack this 
                #"titleAngle": 0, # horizontal
                #"titleY": -10, # move it up
                #"titleX": 18, # move it to the right so it aligns with the labels 
            },
        }
    }


# CALLBACKS & PLOT CREATION
#==========================

@app.callback(
    dash.dependencies.Output(component_id = 'line_plot', component_property = 'srcDoc'),
    [dash.dependencies.Input(component_id = 'date_slider', component_property = 'value'),
    dash.dependencies.Input(component_id = 'damage_types_dropdown_tab1', component_property = 'value')
    ]
)
def make_line_plot(date_list, damage):
    """
    Generates a filled line plot based on user selection of date and damage level

    Parameters
    ----------
    date_list - a list of 2 ints; user selected from a date slide and passed by callback
    damage - a string; user selected from dropdown and passed by callback

    Return
    ------
    an altair plot converted to html
    """

    alt.themes.register('mds_special', mds_special)
    alt.themes.enable('mds_special')
    #alt.themes.enable('none') # to return to default
    
    query_string = ""
    for user_select_damage in damage:
        query_string += 'damage_level == "' + user_select_damage + '" | ' 
    
    query_string = query_string[: -2]

    df_line = df.query('year >= @date_list[0] & year <= @date_list[1]')

    if len(query_string) != 0:
        label = alt.selection_single(
            encodings = ['x'], 
            on = 'mouseover',  
            nearest = True,    
            empty = 'none'     
        )
        
        #generate a line plot
        line_plot_base = alt.Chart(df_line.query(query_string),
                      title = 'Bird Strike Damage over Time'
                      ).mark_area(opacity = 0.3, interpolate = 'monotone'
                      ).encode(
                            alt.X('year:O', axis=alt.Axis(title = "Year",
                                                          labelAngle = 0)),
                            alt.Y('count(damage_level):N', 
                                  axis = alt.Axis(title = "Bird Strikes"), 
                                  stack = None),
                            alt.Color('damage_level', 
                                      scale = alt.Scale(domain = ['Substantial', 'Medium', 'Minor', 'None'],
                                                        range = ['red', 'dodgerblue', 'grey', 'darkgreen']),
                                      legend = alt.Legend(orient='bottom', 
                                                            titleOrient='left',
                                                            title = "Damage Level",
                                                            labelFontSize=15,
                                                            titleFontSize=15)),
                            alt.Order('damage_level_sort', sort = 'ascending'),
                            alt.Tooltip(['damage_level', 'year', 'count(damage_level)'])
                      )
        #create an interactive vertical bar that displays point values of line plots         
        line_plot = alt.layer(
                line_plot_base,
                
                alt.Chart().mark_rule(color = 'grey').encode(
                    x = 'year:O'
                ).transform_filter(label),

                line_plot_base.mark_circle().encode(
                    opacity = alt.condition(label, alt.value(1), alt.value(0))
                ).add_selection(label),

                line_plot_base.mark_text(align = 'left', 
                                    dx = 5, dy = -10,
                                    fontSize = 15,
                                    fontWeight = 600,
                                    stroke = 'grey', 
                                    strokeWidth = 1
                ).encode( text = 'count(damage_level):N'
                ).transform_filter(label),
                
                line_plot_base.mark_text(align = 'left', 
                                    dx = 5, dy = -10,
                                    fontSize = 15,
                                    fontWeight= 600
                ).encode(text='count(damage_level):N'
                ).transform_filter(label),
                
                data = df
            ).properties(width = 500, height = 400)
        
        line_plot = line_plot.to_html()
    else:
        line_plot = None
    
    return line_plot

@app.callback(
    dash.dependencies.Output(component_id = 'bar_plot', component_property = 'srcDoc'),
    [dash.dependencies.Input(component_id = 'bar_dropdown', component_property = 'value'),
    dash.dependencies.Input(component_id = 'damage_types_dropdown_tab1', component_property = 'value')
    ]
)
def make_bar_plot(category, damage):
    """
    Generates a bar plot based on user selection of category and damage level

    Parameters
    ----------
    category - a string; user selected from dropdown and passed by callback
    damage - a string; user selected from dropdown and passed by callback

    Return
    ------
    an altair plot converted to html
    """

    alt.themes.register('mds_special', mds_special)
    alt.themes.enable('mds_special')
    #alt.themes.enable('none') # to return to default

    query_string = ""
    for user_select_damage in damage:
        query_string += 'damage_level == "' + user_select_damage + '" | ' 
    query_string = query_string[: -2]

    x_title = category.replace('_', ' ').title()
    main_title = 'Effect of ' + x_title + ' on Birdstrikes'

    if len(query_string) != 0:
        #generate a bar plot
        bar_plot = alt.Chart(df.query(query_string),
                        title = main_title
                    ).mark_bar(opacity = 0.3
                    ).encode(
                            alt.X(category + ':O', 
                                axis=alt.Axis(title = x_title, 
                                                labelAngle = 0),
                                sort = alt.EncodingSortField(
                                    field = 'damage_level_sort',
                                    op = 'count',
                                    order = 'ascending')),                                
                            alt.Y('count(damage_level):Q', 
                                axis=alt.Axis(title = "Bird Strikes"), 
                                stack = True),
                            alt.Color('damage_level',
                                    scale = alt.Scale(domain = ['Substantial', 'Medium', 'Minor', 'None'],
                                                    range = ['red', 'dodgerblue', 'grey', 'darkgreen']),
                                    legend = alt.Legend(orient='bottom', 
                                                        titleOrient='left', 
                                                        title = "Damage Level",
                                                        labelFontSize=15,
                                                        titleFontSize=15)),
                            alt.Order('damage_level_sort', sort = 'ascending'),
                            alt.Tooltip(['count(damage_level)']) 
                    ).properties(width = 500, height = 400)
        
        bar_plot = bar_plot.to_html()
    
    else:
        bar_plot = None
        
    return bar_plot

@app.callback(
    dash.dependencies.Output(component_id = 'heatmap_plot', component_property = 'srcDoc'),
    [dash.dependencies.Input(component_id = 'heatmap_dropdown', component_property = 'value'),
    dash.dependencies.Input(component_id = 'damage_types_dropdown_tab2', component_property = 'value')
    ]
)
def make_heatmap_plot(y_category, damage):
    """
    Generates a heatmap plot based on user selection of category and damage level

    Parameters
    ----------
    y_category - a string; user selected from dropdown and passed by callback
    damage - a string; user selected from dropdown and passed by callback

    Return
    ------
    an altair plot converted to html
    """

    alt.themes.register('mds_special', mds_special)
    alt.themes.enable('mds_special')
    #alt.themes.enable('none') # to return to default
    
    query_string = ""
    for user_select_damage in damage:
        query_string += 'damage_level == "' + user_select_damage + '" | ' 
    
    query_string = query_string[: -2]

    main_title = 'Bird Strikes by ' + y_category.title()
    
    if y_category == 'state':
        plot_height = 600
    else:
        plot_height = 1000

    if len(query_string) != 0:
        #generate a heatmap
        heatmap_plot = alt.Chart(df.query(query_string),
                         title = main_title
                        ).mark_rect(
                        ).encode(
                                alt.X('year:N', axis = alt.Axis(title = "Year", 
                                                                labelAngle = 0)),
                                alt.Y(y_category + ':O', axis = alt.Axis(title = y_category.title())),
                                alt.Color('count(damage_level)',
                                          scale = alt.Scale(scheme = "lighttealblue"),
                                          legend = alt.Legend(  title = "Bird Strikes",
                                                                labelFontSize=15,
                                                                titleFontSize=15)),
                                alt.Tooltip(['year', 'state', 'count(damage_level)'])
                        ).properties(width = 600, height = plot_height)
        
        heatmap_plot = heatmap_plot.to_html()
    else:
        heatmap_plot = None

    return heatmap_plot

if __name__ == '__main__':
    app.run_server(debug=True)