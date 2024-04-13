from flask import Flask , render_template
from database import *

app = Flask(__name__)

create_database('customer_database.db')
create_table('customer','RowNumber INTEGER PRIMARY KEY, customer_id INTEGER , Surname TEXT, CreditScore INTEGER, Geography TEXT, Gender TEXT, Age INTEGER, Tenure INTEGER, Balance REAL, Number_of_product INTEGER, HasCrCard INTEGER, IsActiveMember INTEGER, EstimatedSalary REAL, Exited INTEGER')
insert_data_csv('customer', 'group5_flask_project/Churn_Modelling.csv')
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data')
def display_data():
    
    conn = sqlite3.connect('customer_database.db')
    cursor = conn.cursor()

    
    cursor.execute("SELECT * FROM customer ORDER BY RowNumber LIMIT 15")
    data = cursor.fetchall()

    
    conn.close()

    return render_template('data.html', data=data)
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)