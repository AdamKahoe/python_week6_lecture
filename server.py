from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') #is equal to localhost: 5000
def hello_world():
    return 'Hello World!'

@app.route('/<name>/<int:num>') #is equal to localhost: 5000
def say_hello(name, num):
    print(type(name))
    print(type(num))
    return f'Hello {name} , your lucky number is {num}'

@app.route('/<name>') #is equal to localhost: 5000
def nums(name):
    print(type(name))
    food = "Pizza"
    return render_template('pizza.html', name = name, food = food)

if __name__=="__main__":
    app.run(debug=True) #sometimes (debug=True, _port=5001) if Monterey