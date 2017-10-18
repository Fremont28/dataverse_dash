#Create dash visualizations with integer, floats, and string data types

#import dash components 
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd 
import matplotlib.pyplot as plt

#1. Integers
data1=pd.read_csv('FL-1990-births (1).csv')

#create a bar graph
ax=data1[['January','February']].plot(kind='bar',title="Bar",figsize=(10,5),legend=True,fontsize=12)
ax.set_xlabel('Total',fontsize=12)
ax.set_ylabel('DOB Count',fontsize=12)
plt.show()

# create an index table (for births by day in January)
pv=pd.pivot_table(data1,index=['DOB_MM'],values=['January'],aggfunc=sum,fill_value=0)
trace1=go.Bar(x=pv.index,y=pv[('January')])
#create dash app (barplot)
app=dash.Dash() 
app.layout=html.H1(children=[
    html.H1(children='Births by Day in January'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data':[trace1],
            'layout':
            go.Layout(title='Births by Day in January',barmode='stack')
        })
])

if __name__ == '__main__':
    app.run_server(debug=True)

#2. Floats (Histogram)*************
data2=pd.read_csv('bjpols_R2.csv')

import matplotlib.pyplot as plt 

sub_data2=data2['sppop_L1']
pd.options.display.mpl_style='default'
sub_data2.hist() 

#test with dash (create histogram)*****
trace2=go.Histogram(x='sppop_L1')

app.layout=html.H1(children=[
    html.H1(children='SPPOP_L1'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data':[trace2],
            'layout':
            go.Layout(title='BSPPOP_L1')
        })
])

if __name__ == '__main__':
    app.run_server(debug=True)








