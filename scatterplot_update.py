#import dataset
flights=pd.read_csv("int_us.csv")

app = dash.Dash()

#scatterplot seats available vs. passengers on international flights departing
# from the U.S.  
app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=flights[flights['DEST_COUNTRY_NAME'] == i]['SEATS'],
                    y=flights[flights['DEST_COUNTRY_NAME'] == i]['PASSENGERS'],
                    text=flights[flights['DEST_COUNTRY_NAME'] == i]['DEST_COUNTRY_NAME'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in flights.DEST_COUNTRY_NAME.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Seats'},
                yaxis={'title': 'Passengers'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])


if __name__ == '__main__':
    app.run_server()
