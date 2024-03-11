from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def print_current_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Current Date and Time: {current_date}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

