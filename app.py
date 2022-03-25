import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    nl = "\n"
    return f"""
      <html>
       <head>
        <title>Hello World from a Container</title>
       </head>
       <body>
        <h1>Hello World!</h1>
        This is Python running in a container.
        <h2>Environment</h2>
        <pre>{nl.join([k+'='+v for k, v in dict(os.environ).items()])}</pre>
       </body>
      </html>
    """
