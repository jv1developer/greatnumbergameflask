from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'greatNumbers'

@app.route('/')
def index():
    import random
    if 'randomNumber' not in session:
        session['randomNumber'] = random.randrange(0, 101)
    if 'count' not in session:
        session['count'] = 0
    print("Random Number: ",session['randomNumber'])
    print("Session Count: ",session['count'])
    if 'lowFill' not in session:
        session['lowFill'] = 'none'
    if 'highFill' not in session:
        session['highFill'] = 'none'
    if 'correctFill' not in session:
        session['correctFill'] = 'none'
    if 'playFill' not in session:
        session['playFill'] = 'none'
    if 'guessFill' not in session:
        session['guessFill'] = 'block'
    return render_template('index.html', lowFill=session['lowFill'], highFill=session['highFill'], correctFill=session['correctFill'], playFill=session['playFill'], guessFill=session['guessFill'])

@app.route('/tooLow')
def low():
    session['lowFill'] = 'block'
    session['highFill'] = 'none'
    session['correctFill'] = 'none'
    session['playFill'] = 'none'
    session['guessFill'] = 'block'
    session['count'] = session['count'] + 1
    return redirect('/')

@app.route('/tooHigh')
def high():
    session['lowFill'] = 'none'
    session['highFill'] = 'block'
    session['correctFill'] = 'none'
    session['playFill'] = 'none'
    session['guessFill'] = 'block'
    session['count'] = session['count'] + 1
    return redirect('/')

@app.route('/correct')
def equal():
    session['lowFill'] = 'none'
    session['highFill'] = 'none'
    session['correctFill'] = 'block'
    session['playFill'] = 'block'
    session['guessFill'] = 'none'
    return redirect('/')

@app.route('/check', methods=['POST'])
def check():
    print("Got Post Info")
    session['attempt'] = request.form['attempt']
    attInt = int(session['attempt'])
    if attInt < session['randomNumber']:
        attInt = 0
        session['attempt'] = 0
        return redirect('/tooLow')
    if attInt > session['randomNumber']:
        attInt = 0
        session['attempt'] = 0
        return redirect('/tooHigh')
    if attInt == session['randomNumber']:
        attInt = 0
        session['attempt'] = 0
        return redirect('correct')

@app.route('/restart', methods=['GET'])
def startAgain():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True) 