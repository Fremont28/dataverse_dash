##6. new dataset (bar)
#import flight dataset (international flights departing from the U.S.)
flights=pd.read_csv("int_us.csv")

pv = pd.pivot_table(flights,index=['DEST_COUNTRY'], columns=["CLASS"], values=['SEATS'])
#replace na with zeroes

#Airplane seats by class on international flights 
trace1 = go.Bar(x=pv.index, y=pv[('SEATS', 'P')], name='p')
trace2= go.Bar(x=pv.index, y=pv[('SEATS', 'L')], name='l')
trace3=go.Bar(x=pv.index, y=pv[('SEATS', 'F')], name='f')
trace4=go.Bar(x=pv.index,y=pv[('SEATS','G')],name='G')


app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='test bar plot'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace1,trace2,trace3,trace4],
            'layout':
            go.Layout(title='International Carrier Flights Classes', barmode='stack')
        })
])

if __name__ == '__main__':
    app.run_server()