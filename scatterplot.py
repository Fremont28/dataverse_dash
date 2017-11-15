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

html.Div(dcc.Slider(
        id='crossfilter-year--slider',
        value=data1['year'],
        step=None,
        marks={str(year): str(year) for year in data1['year'].unique()}
    ), style={'width': '49%', 'padding': '0px 20px 20px 20px'})
   
# NMB: Line 55 produces an error because Output and Input are called without
# being defined.
@app.callback(Output('slider-container','children'),[Input('button','n_clicks')])

def add_sliders(n_clicks):
    return html.Div(
[dcc.Slider(id='slider-{}'.format(i)) for i in range(n_clicks)]+
[html.Div(id='output-{}'.format(i)) for i in range(n_clicks)]
    )

for i in range(10):
    @app.callback(Output('slider-{}'.format(i), 'children'), [Input('slider-{}'.format(i), 'value')])
    def update_output(slider_i_value_):
        return slider_i_value 

if __name__ == '__main__':
    app.run_server()


