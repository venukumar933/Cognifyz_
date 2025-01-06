import dash # type: ignore
from dash import dcc # type: ignore
from dash import html # type: ignore
from dash.dependencies import Input, Output # type: ignore
import plotly.express as px # type: ignore
import pandas as pd # type: ignore
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore
import io
import base64

# Create a Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Interactive Data Visualization Tool"),
    
    # File upload component
    dcc.Upload(
        id='upload-data',
        children=html.Button('Upload Data'),
        multiple=False
    ),
    
    html.Br(),
    html.Div(id='file-name'),
    
    # Dropdown for selecting type of plot
    dcc.Dropdown(
        id='plot-type',
        options=[
            {'label': 'Bar Chart', 'value': 'bar'},
            {'label': 'Line Chart', 'value': 'line'},
            {'label': 'Scatter Plot', 'value': 'scatter'},
            {'label': 'Box Plot', 'value': 'box'},
            {'label': 'Histogram', 'value': 'hist'},
            {'label': 'Correlation Heatmap', 'value': 'heatmap'}
        ],
        value='bar',
        style={'width': '50%'}
    ),
    
    # Dropdown for selecting columns
    dcc.Dropdown(id='x-column', style={'width': '50%'}),
    dcc.Dropdown(id='y-column', style={'width': '50%'}),
    
    # Placeholder for visualizations
    html.Div(id='plot-output')
])

# Callback to handle file upload and display dataset preview
@app.callback(
    Output('file-name', 'children'),
    Output('x-column', 'options'),
    Output('y-column', 'options'),
    Input('upload-data', 'contents')
)
def upload_file(contents):
    if contents is None:
        return "No file uploaded", [], []
    
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    
    columns = [{'label': col, 'value': col} for col in df.columns]
    
    return f"File Uploaded: {df.shape[0]} rows, {df.shape[1]} columns", columns, columns

# Callback to generate plot based on the user's selection
@app.callback(
    Output('plot-output', 'children'),
    Input('plot-type', 'value'),
    Input('x-column', 'value'),
    Input('y-column', 'value'),
    Input('upload-data', 'contents')
)
def generate_plot(plot_type, x_col, y_col, contents):
    if contents is None:
        return "Please upload a dataset."
    
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    
    if plot_type == 'bar':
        fig = px.bar(df, x=x_col, y=y_col, title=f'Bar Chart: {x_col} vs {y_col}')
    elif plot_type == 'line':
        fig = px.line(df, x=x_col, y=y_col, title=f'Line Chart: {x_col} vs {y_col}')
    elif plot_type == 'scatter':
        fig = px.scatter(df, x=x_col, y=y_col, title=f'Scatter Plot: {x_col} vs {y_col}')
    elif plot_type == 'box':
        fig = px.box(df, x=x_col, y=y_col, title=f'Box Plot: {x_col} vs {y_col}')
    elif plot_type == 'hist':
        fig = px.histogram(df, x=x_col, title=f'Histogram: {x_col}')
    elif plot_type == 'heatmap':
        correlation_matrix = df.corr()
        fig = px.imshow(correlation_matrix, text_auto=True, title='Correlation Heatmap')
    
    return dcc.Graph(figure=fig)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
