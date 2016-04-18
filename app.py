
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.vars={}

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        # request was a POST
        app.vars['borough'] = request.form['selected_borough']

        # Display appropriate graph based on borough selection
        if app.vars['borough'] == 'Bronx':
            return render_template('Bronx.html')

        if app.vars['borough'] == 'Brooklyn':
            return render_template('Brooklyn.html')

        if app.vars['borough'] == 'Manhattan':
            return render_template('Manhattan.html')

        if app.vars['borough'] == 'Queens':
            return render_template('Queens.html')

        if app.vars['borough'] == 'Staten_Island':
            return render_template('Staten_Island.html')


if __name__ == '__main__':
  app.run(port=33507)
