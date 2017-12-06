# import dash components
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


#import dataset
flights=pd.read_csv("int_flights_us.csv")

app = dash.Dash()

app.layout = html.Div([
    dcc.Dropdown(
        id="xaxis",
        options=[
            {'label': var, 'value': var} for var in flights.columns
        ],
        # value=flights.columns[0],
        placeholder='Select X-Axis Variable'
    ),
    dcc.Dropdown(
        id="yaxis",
        options=[
            {'label': var, 'value': var} for var in flights.columns
        ],
        # value=flights.columns[0],
        placeholder='Select Y-Axis Variable'
    ),
    dcc.Graph(id='scatterplot')
])

@app.callback(
    dash.dependencies.Output('scatterplot', 'figure'),
    [
        dash.dependencies.Input("xaxis", 'value'),
        dash.dependencies.Input("yaxis", 'value')
    ])
def update_figure(xaxis, yaxis):
    return {
        'data': [go.Scatter(
            x=flights[xaxis],
            y=flights[yaxis],
            text='Scatterplot',
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
                        }
                    )
                ],
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': xaxis},
            yaxis={'title': yaxis},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server()
