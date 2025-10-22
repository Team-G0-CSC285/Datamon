from flask import Flask, render_template, request, redirect, url_for, session
import math_checkers  # assuming this module has logic for Answer Checker

app = Flask(__name__)
app.secret_key = 'your‑secret‑key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile')
def profile():
    player = session.get('player', {'name': None, 'history': [], 'score': 0})
    return render_template('profile.html', player=player)

@app.route('/game/answer_checker', methods=['GET','POST'])
def answer_checker():
    if request.method == 'POST':
        # get user answer
        user_answer = request.form.get('answer')
        # get correct answer stored in session
        correct = session.get('current_correct')
        # check
        is_correct = (str(user_answer) == str(correct))
        # update session history & score
        history = session.setdefault('history', [])
        history.append({'problem': session.get('current_problem'), 'your_answer': user_answer, 'correct_answer': correct, 'is_correct': is_correct})
        session['history'] = history
        if is_correct:
            session['score'] = session.get('score',0) + 1
        return redirect(url_for('answer_checker_result'))

    # GET: generate new problem
    num1, operator, num2, correct = math_checkers.generate_problem()  # you’d write this
    session['current_problem'] = f"{num1} {operator} {num2}"
    session['current_correct'] = correct
    return render_template('answer_checker.html', problem=session['current_problem'])

@app.route('/game/answer_checker/result')
def answer_checker_result():
    # show result of last answer, link to next or summary
    last = session['history'][-1] if session.get('history') else None
    return render_template('answer_checker_result.html', last=last)

@app.route('/game/summary')
def summary():
    return render_template('summary.html', history=session.get('history', []), score=session.get('score',0))

if __name__ == '__main__':
    app.run(debug=True)
