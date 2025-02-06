import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Load data
df = pd.read_csv("formatted_data.csv")

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1("Pink Morsels Sales Data", className="title"),

    html.Label("Select a Region:", className="label"),
    dcc.RadioItems(
        id="region-selector",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"}
        ],
        value="all",  # Default to showing all regions
        className="radio-buttons"
    ),

    dcc.Graph(id="sales-chart", className="chart")
], className="container")


# Callback to update chart based on selected region
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(selected_region):
    filtered_df = df if selected_region == "all" else df[df["region"] == selected_region]
    fig = px.line(filtered_df, x="date", y="sales", color="region", title="Sales Trends")
    return fig


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)



