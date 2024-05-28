from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    name = '권지밍'
    lotto = [16, 18, 20, 21, 9, 11]
    context= {
        "name" : name,
        "lotto" : lotto,
    }
    return render_template('index.html', data=context)

@app.route('/mypage')
def mypage():
    return 'This is mypage!'

if __name__ == '__main__':  
    app.run(debug=True)