from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import db
import QR_CODE



app = Dash()

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}   


fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(
    style={
        'backgroundColor': colors['background'],
        'color': colors['text'] 
    },
    
    children=[
    html.H1(children='Testing Dash Application - Day 1', style=
            {
                'textAlign': 'center',
                'color': colors['text']
            }),

    html.Div(children='''
        Dash: A web application framework for your data.
    ''', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

db.create_table()

tableFruit = db.addTable(df.iloc[0]['Fruit'], df.iloc[0]['Amount'], df.iloc[0]['City'])

print('Or u can use this QR code int the next folder to connect to the webpage dash app')
QR_CODE.generateByDefault('http://127.0.0.1:8050/')
if __name__ == '__main__':
    app.run(dev_tools_hot_reload=False, debug=True, port=8050)
    
    
