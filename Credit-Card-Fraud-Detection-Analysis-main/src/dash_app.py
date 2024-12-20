from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("data/creditcard.csv")
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Credit Card Fraud Analysis"),
    dcc.Dropdown(
        id="feature-dropdown",
        options=[{"label": col, "value": col} for col in df.columns if col != "Class"],
        value="Amount"
    ),
    dcc.Graph(id="histogram")
])

@app.callback(
    Output("histogram", "figure"),
    Input("feature-dropdown", "value")
)
def update_histogram(feature):
    return px.histogram(df, x=feature, color="Class", barmode="overlay")

if __name__ == "__main__":
    app.run_server(debug=True)
