from dash import Dash, html, dcc
import dash

app = Dash(__name__, use_pages=True)

if __name__ == '__main__':
    app.run_server(port = 4050)