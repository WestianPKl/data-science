import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go


def fetch_financial_data(company="AMZN"):
    import pandas_datareader.data as web
    return web.DataReader(name=company, data_source='stooq')

df = fetch_financial_data()
df.reset_index(inplace=True)
df = df[df.Date > '2024-01-01']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H4('Notowania spółki Amazon'),

    dcc.Graph(
        figure=go.Figure(
            [go.Scatter(
                x=df['Date'],
                y=df['Close'],
                mode='lines',
                fill='tozeroy',
                name='Amazon'
            )],
            layout=go.Layout(
                yaxis={'type':'log'},
                height=500,
                title={'text': 'Wykres ceny'},
                showlegend=True
            )
        )
    ),

    dcc.Graph(
        figure=go.Figure(
            [go.Bar(
                x=df['Date'],
                y=df['Volume'],
                name='Wolumen'
            )],
            layout=go.Layout(
                yaxis={'type': 'log'},
                height=300,
                title={'text': 'Wykres wolumenu'},
                showlegend=True
            )
        )
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)