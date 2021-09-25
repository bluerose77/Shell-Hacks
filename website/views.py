from flask import Blueprint,render_template
from website.dconnect import connect
views = Blueprint('views',__name__)

@views.route('/')
def home():
    cursor = connect.get_db()
    cursor.execute("SELECT * FROM covid_us.dailydata")
    data = cursor.fetchall()
    # print(data)
    return render_template('index.html', output_data = data)

@views.route('/daycase')
def daycase():
    