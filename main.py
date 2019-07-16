import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donor, Donation 

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/create', methods=['GET', 'POST'])
def create():

    if request.method == 'POST':
        try:
            donor1 = Donor.select().where(Donor.name==request.form['donor']).get()
            Donation.insert(donor=donor1.id, value=int(request.form['donation'])).execute()
        except:
            return render_template('create.jinja2', error=format(request.form['donor'] + ' is not in the database. Please try again.'))

        else:
            return redirect(url_for('create'))

    else:
        return render_template('create.jinja2')
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)