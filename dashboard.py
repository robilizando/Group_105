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



#----------------------------------------------------------------------
# DBC and DASH Components
#===================================

title_header = dbc.Jumbotron(
    [
        dbc.Container(
            [
                dbc.Row([
                    dbc.Col([
                        html.Img(src='https://cdn.pixabay.com/photo/2012/04/16/13/55/swans-36088_960_720.png', 
                            width='100%')
                       ], width = 2),
                    dbc.Col([
                        html.H1("Aircraft Bird Strikes"),#, className="display-3"),                 
                        dcc.Markdown(
                            '''
                            The purpose of the app is to investigate the effect of birdstrikes on aircraft between 1990 and 2002 in the United States.   
                            Different factors (flight phase, time of day, and bird size) and regions (states / airports) are explored, visualizing four classes of damage to aircraft.   


                            The aim of __Tab 1__ is to visualize the trend of number of and damage caused by birdstrikes between 1990 and 2002.   
                            The visualizations in this tab explore what factors effect the number and of and damage caused by bird strikes.

                            The aim of __Tab 2__ is to explore which states and airports observed the largest number of bird strikes between 1990 and 2002.

                            '''
                        )
                        
                    ])
                 ]),

            ],
            fluid=True,
        )
    ],
    fluid=True,
)

dropdown_selector_tab1 = dcc.Dropdown(
    id = 'damage_types_dropdown_tab1',
    options = [
        {'label': 'No Damage', 'value': 'None'},
        {'label': 'Minor Damage', 'value': 'Minor'},
        {'label': 'Medium Damage', 'value': 'Medium'},
        {'label': 'Substantial Damage', 'value': 'Substantial'}
    ],
    multi = True,
    #value = []
    value = ['Minor', 'Medium', 'Substantial'],
    style = dict(width = '60%')
)

dropdown_selector_tab2 = dcc.Dropdown(
    id = 'damage_types_dropdown_tab2',
    options = [
        {'label': 'No Damage', 'value': 'None'},
        {'label': 'Minor Damage', 'value': 'Minor'},
        {'label': 'Medium Damage', 'value': 'Medium'},
        {'label': 'Substantial Damage', 'value': 'Substantial'}
    ],
    multi = True,
    #value = []
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

radio_barchart = dcc.Dropdown(
    id = 'bar_radio',
    options = [
        {'label': 'Flight Phase', 'value': 'flight_phase'},
        {'label': 'Time of Day', 'value': 'time_of_day'},
        {'label': 'Bird Size', 'value': 'bird_size'}
    ],
    value = 'flight_phase',
    style = dict(width = '48%')
)

radio_heatmap = dcc.Dropdown(
    id = 'heatmap_radio',
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
    height = '650',
    width = '850',
    style = {'border-width': '0'}
)

bar = html.Iframe(
    sandbox = 'allow-scripts',
    id = 'bar_plot',
    height = '650',
    width = '750',
    style = {'border-width': '0'}
)

heatmap = html.Iframe(
    sandbox = 'allow-scripts',
    id = 'heatmap_plot',
    height = '1100',
    width = '1000',
    style = {'border-width': '0'}
) 
 

selectors_tab1 =  dbc.Container(fluid = True, 
    children = [dbc.Row([
        dbc.Col(children = [
            html.H5("Damage Type"),
            dropdown_selector_tab1,
            html.Br()
        ])
    ]),
    dbc.Row(children = [
        dbc.Col(children = [
            html.H5("Date Range Between 1990 - 2002"),
            rangeslider_selector,
            html.Br()]),
        dbc.Col([
            html.H5("Factor"),
            radio_barchart,
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
            The following visualization can help solving many problems. Using the interactive tools above, try answering the following:    

            - How has the number of bird strikes causing substantial damage changed between 1994 and 1999?    
            - What is the difference between birdstrikes causing minor damage and medium damage in 1996?   
            - What time of day results in the most birdstrikes causing substantial damage?  
            - What is the difference between the number of large bird and small bird birdstrikes that cause no damage?  
            '''
        )
    ]),
    dbc.Row([
        dbc.Col([
            html.Hr()
        ])
    ]),
 ])

selectors_tab2 =  dbc.Container(fluid = True, children = [dbc.Row([
        dbc.Col(children = [
            html.H5("Damage Type"),
            dropdown_selector_tab2,
            html.Br(),
            html.H5("Location Type"),
            radio_heatmap,
            html.Hr(),
            dcc.Markdown(
            '''
            __Example Questions__  
            The following visualization can help solving many problems. Using the interactive tools above, try answering the following:    

            - What state experienced the most birdstrikes and in what year?  
            - What airport experienced the most birdstrikes and in what year and state did this occur?  
            - What states experienced the most birdstrikes causing minor damage and in what year did this occur?
            '''
            ),
            html.Hr()
            ],
        ),
    ])
 ])


#--------------------------------------------------------------------------------
#USING dbc TABS below - 
#==================================
# tab1_content = dbc.Card(
#     dbc.CardBody(
#         [
#             dbc.Container(fluid = True, children = [
#                 dbc.Row(children = [ 
#                     dbc.Col(children = [
#                         line], #width = 6
#                     ),
#                     dbc.Col(children = [
#                         bar], #width = 6
#                     ),
#                 ]),           
#             ])
#         ]
#     ),
#     className="mt-3",
# )

# tab2_content = dbc.Card(
#     dbc.CardBody(
#         [
#             dbc.Container(fluid = True, children = [
#                 dbc.Row(children =[
#                     dbc.Col(children = [
#                         heatmap]
#                     )
#                 ])  
#             ])  
#         ]
#     ),
#     className="mt-3",
# )

# tabs = dbc.Tabs(
#     [
#         dbc.Tab(children = [tab1_content], label="Factors"),
#         dbc.Tab(children = [tab2_content], label="Airports / States")
#     ]
# )
#--------------------------------------------------------------------------------
#USING html TABS below
#===================================
tabs = \
html.Div(children = [
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Tab 1 - Bird Strikes Trends & Factors', value='tab-1'),
        dcc.Tab(label='Tab 2- Bird Strikes by Location', value='tab-2'),
    ]),
    html.Div(id='tabs-content')#, style = {'backgroundColor':'tan'})
])

@app.callback(Output(component_id ='tabs-content',component_property = 'children'),
              [Input(component_id = 'tabs', component_property = 'value')])
def display_tabs(tab):
    if tab == 'tab-1':
        tab_1_container = dbc.Container(fluid = True, children = [
            dbc.Row(children = [ 
                dbc.Col(children = [
                    line], #width = 6
                ),
                dbc.Col(children = [
                    bar], #width = 6
                ),
            ]),           
        ])
        return [selectors_tab1, tab_1_container]
        
    elif tab == 'tab-2':
        tab_2_container = dbc.Container(fluid = True, children = [
            dbc.Row(children =[
                dbc.Col(children = [
                    heatmap]
                )
            ])  
        ])  
        return [selectors_tab2, tab_2_container]
#--------------------------------------------------------------------------------


app.layout = html.Div([title_header,
                       tabs,
                       dcc.Markdown(
                           '''
                           [Photo Attribution](https://pixabay.com/vectors/swans-silhouette-black-flying-36088/)
                           '''
                       )])

#--------------------------------------------------------------------------------
# CALLBACKS
#==========================

@app.callback(
    dash.dependencies.Output(component_id = 'line_plot', component_property = 'srcDoc'),
    [dash.dependencies.Input(component_id = 'date_slider', component_property = 'value'),
    dash.dependencies.Input(component_id = 'damage_types_dropdown_tab1', component_property = 'value')
    ]
)
def make_line_plot(date_list, damage):
    
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
                                      #sort = ['Substantial', 'Medium', 'Minor', 'None'],
                                      scale = alt.Scale(domain = ['Substantial', 'Medium', 'Minor', 'None'],
                                                        range = ['red', 'dodgerblue', 'grey', 'darkgreen']),
                                      legend = alt.Legend(orient='bottom', 
                                                            titleOrient='left',
                                                            title = "Damage Level")),
                                                          #orient = 'none', 
                                                          #legendX = 675, legendY = 10, 
                                                          #fillColor = 'white')),
                            alt.Order('damage_level_sort', sort = 'ascending')
                      )
                 
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
            ).properties(width = 600, height = 500)
        
        line_plot = line_plot.to_html()
    else:
        line_plot = None
    
    return line_plot

@app.callback(
    dash.dependencies.Output(component_id = 'bar_plot', component_property = 'srcDoc'),
    [dash.dependencies.Input(component_id = 'bar_radio', component_property = 'value'),
    dash.dependencies.Input(component_id = 'damage_types_dropdown_tab1', component_property = 'value')
    ]
)
def make_bar_plot(category, damage):

    query_string = ""
    for user_select_damage in damage:
        query_string += 'damage_level == "' + user_select_damage + '" | ' 
    query_string = query_string[: -2]

    x_title = category.replace('_', ' ').title()
    main_title = 'Effect of ' + x_title + ' on Birdstrikes'

    if len(query_string) != 0:
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
                                                        title = "Damage Level")),
                            alt.Order('damage_level_sort', sort = 'ascending'),
                            alt.Tooltip(['count(damage_level)']) 
                    ).properties(width = 600, height = 500)
        
        bar_plot = bar_plot.to_html()
    
    else:
        bar_plot = None
        
    return bar_plot

@app.callback(
    dash.dependencies.Output(component_id = 'heatmap_plot', component_property = 'srcDoc'),
    [dash.dependencies.Input(component_id = 'heatmap_radio', component_property = 'value'),
    dash.dependencies.Input(component_id = 'damage_types_dropdown_tab2', component_property = 'value')
    ]
)
def make_heatmap_plot(y_category, damage):
    
    query_string = ""
    for user_select_damage in damage:
        query_string += 'damage_level == "' + user_select_damage + '" | ' 
    
    query_string = query_string[: -2]

    main_title = 'Bird Strikes by' + y_category.title()
    
    if y_category == 'state':
        plot_height = 600
    else:
        plot_height = 1000

    if len(query_string) != 0:
        heatmap_plot = alt.Chart(df.query(query_string),
                         title = main_title
                        ).mark_rect(
                        ).encode(
                                alt.X('year:N', axis = alt.Axis(title = "Year", 
                                                                labelAngle = 0)),
                                alt.Y(y_category + ':O', axis = alt.Axis(title = y_category.title())),
                                alt.Color('count(damage_level)',
                                          scale = alt.Scale(scheme = "lighttealblue"),
                                          legend = alt.Legend(title = "Bird Strikes")),
                                alt.Tooltip(['year', 'state', 'count(damage_level)'])
                        ).properties(width = 600, height = plot_height)
        
        heatmap_plot = heatmap_plot.to_html()
    else:
        heatmap_plot = None

    return heatmap_plot

if __name__ == '__main__':
    app.run_server(debug=True)