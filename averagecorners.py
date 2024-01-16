from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        t1 = request.form['team1'].upper()
        t2 = request.form['team2'].upper()

        a = [int(i) for i in request.form['corners_home'].split()]
        b = [int(i) for i in request.form['corners_away'].split()]
        m = [int(i) for i in request.form['home_score'].split()]
        n = [int(i) for i in request.form['home_concede'].split()]
        o = [int(i) for i in request.form['away_score'].split()]
        p = [int(i) for i in request.form['away_concede'].split()]

        mediagerala = sum(a) / 10
        mediageralb = sum(b) / 10
        mediageral = (mediagerala + mediageralb) / 2
        cm = sum(m) / 10
        cl = sum(n) / 10
        fm = sum(o) / 10
        fl = sum(p) / 10

        return render_template('result.html', t1=t1, t2=t2, mediageral=mediageral, cm=cm, cl=cl, fm=fm, fl=fl)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)