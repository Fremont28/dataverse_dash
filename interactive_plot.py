import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

data1=pd.read_csv('bjpols_R2.csv') #read in the data set 

country_unique=data1["country"].unique() 

app=dash.Dash() 

app.layout = html.Div([
    html.H2("Party Types"),
    html.Div(
        [
            dcc.Dropdown(
                id="country",
                options=[{
                    'label': i,
                    'value': i
                } for i in country_unique],
                value='All Countries'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    dcc.Graph(id='funnel-graph'),
])

@app.callback(
    dash.dependencies.Output('funnel-graph', 'figure'),
    [dash.dependencies.Input('country', 'value')])

# NMB: Line 35 produces an error because you have this definition clause listed
# twice, on line 36 and on line 39
def update_graph(country):


def update_graph(country):
    if Manager == "All Countries":
        data1_plot = data1.copy()
    else:
        data1_plot = data1[data1['country'] == country]

    pv = pd.pivot_table(data1_plot,index=['country'],columns=["year"],values=['shuffled'],aggfunc=sum,fill_value=0)

    trace1 = go.Bar(x=pv.index, y=pv[('shuffled', 'year')], name='Year')
   
    return {
        'data': [trace1],
        'layout':
        go.Layout(
            title='Leadership Changes in African Countries'.format(Manager),
            barmode='overlay')
    }

if __name__ == '__main__':
    # NMB: This produces an error because Manager is called within your
    # update_graph() function but not defined in the function definition
    app.run_server(debug=True)
