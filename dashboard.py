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
                # html.Img(src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Unico_Anello.png/1920px-Unico_Anello.png', 
                #       width='100px'),
                 html.H1("Aircraft Bird Strike in USA", className="display-3"),
                # html.P(
                #     "Add a description of the dashboard",
                #     className="lead",
                # ),
 
            ],
            fluid=True,
        )
    ],
    fluid=True,
)

dropdown_selector = dcc.Dropdown(
    id = 'damage_types_dropdown',
    options = [
        {'label': 'No Damage', 'value': 'None'},
        {'label': 'Minor Damage', 'value': 'Minor'},
        {'label': 'Medium Damage', 'value': 'Medium'},
        {'label': 'Substantial Damage', 'value': 'Substantial'}
    ],
    multi = True,
    value = []
    #value = ['Minor', 'Medium', 'Substantial']
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

radio_barchart = dcc.RadioItems(
    id = 'bar_radio',
    options = [
        {'label': 'Flight Phase', 'value': 'flight_phase'},
        {'label': 'Time of Day', 'value': 'time_of_day'},
        {'label': 'Bird Size', 'value': 'bird_size'}
    ],
    value = 'flight_phase'
)

radio_heatmap = dcc.RadioItems(
    id = 'heatmap_radio',
    options = [
        {'label': 'State', 'value': 'state'},
        {'label': 'Airport', 'value': 'airport'},
    ],
    value = 'state'
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
 

selectors =  dbc.Container(fluid = True, children = [dbc.Row([
        dbc.Col(children = [
            html.H4("Select Damage Type(s) to Generate Plot"),
            html.H6("(required: update selection when switching tabs)"),
            dropdown_selector,
            html.Br(),
            rangeslider_selector,
            html.Br(), html.Br(),
            radio_barchart,
            html.Br(),
            radio_heatmap],
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
        dcc.Tab(label='Factors', value='tab-1'),
        dcc.Tab(label='Airports / States', value='tab-2'),
    ]),
    html.Div(id='tabs-content')
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
        return tab_1_container
        
    elif tab == 'tab-2':
        tab_2_container = dbc.Container(fluid = True, children = [
            dbc.Row(children =[
                dbc.Col(children = [
                    heatmap]
                )
            ])  
        ])  
        return tab_2_container
#--------------------------------------------------------------------------------


app.layout = html.Div([title_header,
                       selectors,
                       tabs])

#--------------------------------------------------------------------------------
# CALLBACKS
#==========================

@app.callback(
    dash.dependencies.Output(component_id = 'line_plot', component_property = 'srcDoc'),
    [dash.dependencies.Input(component_id = 'date_slider', component_property = 'value'),
    dash.dependencies.Input(component_id = 'damage_types_dropdown', component_property = 'value')
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
            encodings = ['x'], # limit selection to x-axis value
            on = 'mouseover',  # select on mouseover events
            nearest = True,    # select data point nearest the cursor
            empty = 'none'     # empty selection includes no data points
        )

        line_plot_base = alt.Chart(df_line.query(query_string),
                      title = 'Bird Strike Damage over Time'
                      ).mark_area(opacity = 0.3
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
                                    stroke = 'grey', 
                                    strokeWidth = 1
                ).encode( text = 'count(damage_level):N'
                ).transform_filter(label),
                
                line_plot_base.mark_text(align = 'left', 
                                    dx = 5, dy = -10
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
    dash.dependencies.Input(component_id = 'damage_types_dropdown', component_property = 'value')
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
    dash.dependencies.Input(component_id = 'damage_types_dropdown', component_property = 'value')
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