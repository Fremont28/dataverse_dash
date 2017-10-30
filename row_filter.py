import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import json
import pandas as pd
import numpy as np
import plotly

app=dash.Dash() 
app.scripts.config.serve_locally=True

df=pd.read_csv('bjpols_R2.csv')

app.layout=html.Div([
    html.H4('bjpols data table'),
    dt.DataTable(
        rows=df.to_dict('records'),

#optional-sets the order of columns
columns=sorted(df.columns),

row_selectable=True,
filterable=True,
sortable=True,
selected_row_indices=[],
id='datatable-bjpols'
    ),
html.Div(id='selected-indexes'),
dcc.Graph(
    id='graph-bjpols'
    ),
], className="container")

@app.callback(
    Output('datatable-bjpols', 'selected_row_indices'),
    [Input('graph-bjpols', 'clickData')],
    [State('datatable-bjpols', 'selected_row_indices')])

def update_selected_row_indices(clickData,selected_row_indices):
    if clickData:
        for point in clickData['points']:
            if point['pointNumber'] in selected_row_indices:
                selected_row_indices.remove(point['pointNumber'])
            else:
                selected_row_indices.append(point['pointNumber'])
    return selected_row_indices 

@app.callback(
    Output('graph-bjpols', 'figure'),
    [Input('datatable-bjpols', 'rows'),
     Input('datatable-bjpols', 'selected_row_indices')])
def update_figure(rows, selected_row_indices):
    dff = pd.DataFrame(rows)
    fig = plotly.tools.make_subplots(
        rows=3, cols=1,
        subplot_titles=('sppop_L1', 'growth_L1', 'Country','partytype','shuffled'),
        shared_xaxes=True)
    marker = {'color': ['#0074D9']*len(dff)}
    for i in (selected_row_indices or []):
        marker['color'][i] = '#FF851B'
    fig.append_trace({
        'x': dff['sppop_L1'],
        'y': dff['growth_L1'],
        'type': 'scatter',
        'marker': marker
    }, 1, 1)
    fig['layout']['showlegend'] = False
    fig['layout']['height'] = 800
    fig['layout']['margin'] = {
        'l': 40,
        'r': 10,
        't': 60,
        'b': 200
    }
    fig['layout']['yaxis3']['type'] = 'log'
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)



        





