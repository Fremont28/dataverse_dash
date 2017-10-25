# Bar plot (categorical data types)

# import dash components
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd 
import matplotlib.pyplot as plt

# read-in the data set 
data2=pd.read_csv('2. Manla LDSF for upload to database.csv')

# create a barplot with Dash (counting categorical variables)
# type of slope (i.e. Sloping, Steep, Composite) 
app=dash.Dash() 
data2['MajLform'].value_counts().plot(kind="bar")
plt.show() 
trace1=go.Bar(x='MajLform')

app.layout=html.H1(children=[
    html.H1(children='Majiform'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data':[trace1],
            'layout':
            go.Layout(title='Majiform')
        })
])

if __name__ == '__main__':
    app.run_server(debug=True)



