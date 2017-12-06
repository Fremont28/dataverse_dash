# import dash components
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


#import dataset
filename = input("Enter filename: ")
tabular=pd.read_csv(filename)

app = dash.Dash()

app.layout = html.Div([
    dcc.Dropdown(
        id="xaxis",
        options=[
            {'label': var, 'value': var} for var in tabular.columns
        ],
        placeholder='Select X-Axis Variable'
    ),
    dcc.Dropdown(
        id="yaxis",
        options=[
            {'label': var, 'value': var} for var in tabular.columns
        ],
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
            x=tabular[xaxis],
            y=tabular[yaxis],
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
