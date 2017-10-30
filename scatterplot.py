#Scatterplot (continuous data types)

#import dash components 
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd 
import matplotlib.pyplot as plt

#read-in the data set 
data1=pd.read_csv('bjpols_R2.csv') #read in the data set 

# create scatterplot with dash 
app = dash.Dash()

#app layout for visualization 
app.layout = html.Div([
    dcc.Graph(
        id='ln_cgdppc_L1 vs. growth_L1',
        figure={
            'data': [
                go.Scatter(
                    x=data1[data1['country'] == i]['ln_cgdppc_L1'],
                    y=data1[data1['country'] == i]['growth_L1'],
                    text=data1[data1['country'] == data1]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in data1.country.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'ln_cgdppc_L1'},
                yaxis={'title': 'growth_L1'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()


