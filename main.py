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

    #if 'username' not in session:
        #return redirect(url_for('login'))

    donors = Donor.select()

    if request.method == 'POST':
        donation = Donation(value=request.form['donation'])
        donation.donor = donor=request.form['donor']
        donation.save()

        return redirect(url_for('create'))

    else:
        return render_template('create.jinja2', donors=donors)
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

