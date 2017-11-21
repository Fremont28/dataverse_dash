
#Scatterplot with selection option for flight carriers 

#import dataset
flights=pd.read_csv("int_us.csv")

flight_carriers = flights["CARRIER"].unique()

app = dash.Dash()

app.layout = html.Div([
    html.H2("Carriers"),
    html.Div(
        [
            dcc.Dropdown(
                id="CARRIER",
                options=[{
                    'label': i,
                    'value': i
                } for i in flight_carriers],
                value='ALL CARRIERS'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    dcc.Graph(id='funnel-graph'),
])

@app.callback(
    dash.dependencies.Output('funnel-graph', 'figure'),
    [dash.dependencies.Input('CARRIER', 'value')])
def update_graph(CARRIER):
    if Manager == "All CARRIERS":
       flights_plot = flights.copy()
    else:
     flights_plot = flights[flights['CARRIER'] == CARRIER]


pv = pd.pivot_table(flights_plot,index=['DEST_COUNTRY'],columns=["CLASS"],values=['SEATS'])


trace1 = go.Bar(x=pv.index, y=pv[('SEATS', 'P')], name='p')
trace2= go.Bar(x=pv.index, y=pv[('SEATS', 'L')], name='l')
trace3=go.Bar(x=pv.index, y=pv[('SEATS', 'F')], name='f')
trace4=go.Bar(x=pv.index,y=pv[('SEATS','G')],name='G')


return {
        'data': [trace1, trace2, trace3, trace4],
        'layout':
        go.Layout(
            title='Carrier {}'.format(CARRIER),
            barmode='stack')
    }

#stil getting error (did I correctly call CARRIER in the update_graph() function?)
if __name__ == '__main__':
    app.run_server(debug=True)
