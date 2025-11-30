import os
from dash import Dash, html

# Create the app
app = Dash(__name__)
server = app.server  # Expose the Flask server for Render

# Layout
app.layout = html.Div([
    html.H1("Goal Tracker Dashboard"),
    html.P("Welcome to your first Dash app on Render!")
])

# Entry point
if __name__ == "__main__":
    # Render sets the PORT environment variable automatically
    port = int(os.environ.get("PORT", 8050))
    app.run(host="0.0.0.0", port=port, debug=False)
