from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pyodbc://root:124055@localhost/laraveltwo?driver=MySQL ODBC 8.0 Unicode Driver'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    email = db.Column('email', db.String(100))
    phone = db.Column('phone', db.String(100))
    # Add other columns as needed

    def __repr__(self):
        return f'<User {self.id}>'

@app.route('/')
def hello_world():
    return 'Hello World!'

# Fetch all records from the 'users' table
@app.route('/users')
def get_users():
    users = User.query.all()
    for user in users:
        print(user.name)
    return 'users'

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
