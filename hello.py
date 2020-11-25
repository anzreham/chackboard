from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/say/<name>/<times>')          # The "@" decorator associates this route with the function immediately following
def hello_world(name,times):
    return render_template('index.html', some_name = name,times= int(times))


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def checkboard():
    return render_template('index.html')
@app.route('/<num>')          # The "@" decorator associates this route with the function immediately following
def addrows(num):
    return render_template('index.html', num =int(num ))

@app.route('/<num>/<num1>')          # The "@" decorator associates this route with the function immediately following
def addcol(num, num1):
    return render_template('index.html', num =int(num),num1 =int(num1))

@app.route('/<num>/<num1>/<colr1>/<colr2>')          # The "@" decorator associates this route with the function immediately following
def addcolandrow(num, num1,colr1, colr2):
    return render_template('index.html', num =int(num),num1 =int(num1), colr1=colr1, colr2 =colr2 )

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode

