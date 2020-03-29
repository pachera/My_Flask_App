from flask import Flask,request,render_template
"""
My Comment
"""

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def hello_flask():
    return("Hello Flask!")

@app.route('/old')
def query_strings():
    query_val = request.args.get('greeting')
    return('<h2> the greeting is : {} </h2>'.format(query_val))

# Using templates
@app.route('/temp')
def using_templates():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run(debug=True)
