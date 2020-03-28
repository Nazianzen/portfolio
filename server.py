from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        message = data['message']
        subject = data['subject']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data['email']
        message = data['message']
        subject = data['subject']

        fieldnames = ['email', 'subject', 'message']

        csv_writer = csv.DictWriter(database2, fieldnames=fieldnames, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow({
            'email': email,
            'subject': subject,
            'message': message
        })


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        # write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "Something went wrong. Try again!"
