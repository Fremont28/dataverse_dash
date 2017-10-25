# Histogram (continuous data types)

#import modules
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd 
import matplotlib.pyplot as plt

# read-in the data set 
data3=pd.read_csv('2. Manla LDSF for upload to database.csv')

#sample histogram with pandas 
ax=data3[['SlopeDn']].plot(kind='hist',title="Down Slope Histogram",figsize=(10,5),legend=True,fontsize=12)
ax.set_xlabel('Slope Down',fontsize=12)
ax.set_ylabel('Frequency',fontsize=12)
plt.show()

# create a histogram with Dash (down slope distribution)
app=dash.Dash() 
trace2=go.Histogram(x='SlopeDn')

app.layout=html.H1(children=[
    html.H1(children='Slopedn'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data':[trace2],
            'layout':
            go.Layout(title='SlopeDn')
        })
])

if __name__ == '__main__':
    app.run_server(debug=True)














