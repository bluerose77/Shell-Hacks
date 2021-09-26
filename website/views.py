from flask import Blueprint,render_template,request
from website.dconnect import connect
views = Blueprint('views',__name__)

@views.route('/')
def home():
    cursor = connect.get_db()
    cursor.execute("SELECT * FROM covid_us.us_cases order by date desc")
    data = cursor.fetchall()
    # print(data)
    cursor.execute("SELECT MAX(total_cases) FROM covid_us.us_cases")
    total_cases = cursor.fetchall()
    total_cases = total_cases[0]
    total_cases = total_cases[0]
    return render_template('home.html', output_data = data , total_case = total_cases)

@views.route('/vaccine')
def vaccine():
    cursor = connect.get_db()
    cursor.execute("SELECT * FROM covid_us.us_vaccination order by date desc")
    data = cursor.fetchall()
    return render_template('vaccine.html', output_data = data )

@views.route('/daycase', methods= ['GET','POST'])
def daycase():
    if request.method == 'POST':
        dat = request.form.get('date')
        dat = str(dat)
        print(dat)
        cursor = connect.get_db()
        query = f"SELECT * FROM covid_us.us_cases WHERE date = %s"
        cursor.execute(query,dat)
        data = cursor.fetchall()
        print(data)
        return render_template('daycase.html',output_data= data,)
    return render_template('daycase.html',output_data= None)