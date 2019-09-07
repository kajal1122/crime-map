from flask import Flask ,render_template,request
from db_code import DB

app = Flask(__name__)
db = DB()
@app.route('/')
def home():
    try:
        data = db.read_data()
    except:
        data = None
    return render_template('home.html',data = data)

@app.route('/add', METHODS = ['POST'])
def add():
    try:
        data = request.form.get('user_input')
        db.insert_data(data)
    except:
        print("Error: Inserting Data")
    return home()


@app.route('/clear')
def clear():
    try:
        db.delete_data()
    except:
        print("Error : Deleting Data")
    return home()
if __name__ == '__main__':
    app.run()


# root - home,
# to insert crime add fun pass keyword
# clear url-  clear fun ,database clear pass
