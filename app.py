from flask import Flask , render_template, request
import requests


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/reveal")
def hello_world2():
    return render_template('reveal.html')
    
@app.route("/test2", methods=["POST"])
def hello_world3():
    user_name = request.form['user'] 
    print(user_name)
    data = requests.get(f"https://api.agify.io/?name={user_name}")
    api = data.json()
    print(api)
    return render_template('name.html', user_name=api["name"], user_age=api["age"])

# @app.route("/2")
# def hello_world2():
#     requests.get("http://100.114.3.62:5000/test2")
        

# @app.route("/album", methods=["GET"])
# def Album():
#     query_string = request.args
#     return data[query_string["resource"]]

if __name__ == '__main__':
     app.run(debug=True, port=5050, host='0.0.0.0')