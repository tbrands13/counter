from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "countItUp"





@app.route('/')
def count():
    if 'visits' in session:
        session ['visits']+=1
    elif 'visits' not in session:
        session ['visits']=1
    print("Visit Count")
    print(request.form)
    return render_template('index.html',
    visit_count = session['visits'])








@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')













if __name__=="__main__":
        app.run(debug=True)