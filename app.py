from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Goal Tracker Dashboard"),
    html.P("Welcome to your first Dash app"),
])

def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
