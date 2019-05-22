import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import plotly.plotly as py
import base64

with open('background.png', 'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()
#add the prefix that plotly will want when using the string as source
encoded_image = "data:image/png;base64," + encoded_string

df = pd.read_csv('rests.csv')

df['color'] = df['price_level']

df.loc[df['price_level'] == 1, 'color'] = '#cdf4e1'
df.loc[df['price_level'] == 2, 'color'] = '#277c53'


data = [go.Scatter(
    x = df.loc[df['price_level'] == 1, 'dist_km'],
    y = df.loc[df['price_level'] == 1, 'rating'],
    dy = 0.5,
    text=df['name'],
    mode='markers',
    name='$',
    marker= dict(size= 10* np.log(df['user_ratings_total']), line = dict(
            width = 2, color = 'black'),
    color = df.loc[df['price_level'] == 1, 'color'])),

    go.Scatter(
        x = df.loc[df['price_level'] == 2, 'dist_km'],
        y = df.loc[df['price_level'] == 2, 'rating'],
        dy = 0.5,
        text=df['name'],
        name='$$',
        mode='markers',
        marker= dict(size= 10* np.log(df['user_ratings_total']), line = dict(
                width = 2, color = 'black'),
        color = df.loc[df['price_level'] == 2, 'color'])
        )]

layout = go.Layout(
    title='Restaurant distance from NBAC',
    font=dict(family='Calibri, monospace', size=20, color='black'),
    xaxis = dict(title = 'Distance (km)'), # x-axis label
    yaxis = dict(title = 'Rating'),
    width = 800,
    height = 580,
    margin=go.layout.Margin(
        l=100,
        r=50,
        b=100,
        t=60,
        pad=8
    ),
    showlegend = True,
        images = [dict(
                        source= encoded_image,
                        xref= "paper",
                        yref= "paper",
                        x= 0,
                        y= 1,
                        sizex= 1.1,
                        sizey= 1.0,
                        sizing= "contain",
                        opacity= 0.7,
                        visible = True,
                        layer= "below")]
                        )


fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='food-graph.html')
