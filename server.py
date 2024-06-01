from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
