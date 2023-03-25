import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_mail import Message, Mail
from get_database import educateurs_database, blogs_database, gsheet_file
from forms import ContactForm
from datetime import datetime

EMAIL_RECIPIENT_1 = f'{os.environ["EMAIL_RECIPIENT_1_1"]}.{os.environ["EMAIL_RECIPIENT_1_2"]}.ad@gmail.com'
EMAIL_RECIPIENT_2 = f'{os.environ["EMAIL_RECIPIENT_2_1"]}.{os.environ["EMAIL_RECIPIENT_2_2"]}@gmail.com'

app = Flask(__name__, static_folder='static', static_url_path='')
app.config['SECRET_KEY'] = os.environ.get('APPCONFIGSECRETKEY')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = f'{os.environ["EMAIL_SENDER_1_1"]}@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ["GOOGLE_PASSWORD"]
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/educateurs', methods=["POST", "GET"])
def educateurs_list():
    if request.method == "GET":
        number_of_results = 18
        counter = 0
        first_results = {}
        remaining_results = {}
        for id, educateur in educateurs_database.items():
            if counter < number_of_results:
                first_results[id] = educateur
                counter += 1
            else:
                remaining_results[id] = educateur
        return render_template('educateurs_list.html',
                               database=educateurs_database,
                               first_results=first_results,
                               remaining_results=remaining_results,
                               is_filtered=False)
    if request.method == "POST":
        department = request.form["department"]
        return redirect(url_for('department_search', department=department))


@app.route('/educateurs/departement/<int:department>', methods=["POST", "GET"])
def department_search(department):
    is_filtered = True
    filtered_database = {}
    for id, educateur in educateurs_database.items():
        if educateur["department"] == department:
            filtered_database[id] = educateur
    return render_template('educateurs_list.html',
                           database=filtered_database,
                           first_results=filtered_database,
                           remaining_results={},
                           department=department,
                           is_filtered=True)


@app.route('/educateurs/region/<region>', methods=["POST", "GET"])
def region_search(region):
    region = region.replace('-', ' ')
    counter = 0
    all_results = {}
    first_6_results = {}
    remaining_results = {}
    for id, educateur in educateurs_database.items():
        if educateur["region"] == region:
            all_results[id] = educateur
            if counter < 6:
                first_6_results[id] = educateur
                counter += 1
            else:
                remaining_results[id] = educateur
    return render_template('educateurs_list_region.html',
                           all_results=all_results,
                           first_6_results=first_6_results,
                           remaining_results=remaining_results,
                           region=region,
                           is_filtered=True)


@app.route('/educateur/<educateur_id>')
def educateur_page(educateur_id):
    educateur_request = educateurs_database[educateur_id]
    # print(educateur_request)
    selected_articles = {}
    number_of_articles = 2
    counter = 0
    for id, blog in blogs_database.items():
        if counter < number_of_articles:
            selected_articles[id] = blog
            counter += 1
    return render_template('educateur_page.html',
                           educateur=educateur_request,
                           blogs=selected_articles)


@app.route('/educateur-canin')
def educateur_job_description():
    return render_template('educateur_job_description.html')


@app.route('/conseils')
def blog_page():
    return render_template('blog_page.html', blogs=blogs_database)


@app.route('/conseils/<article_url>')
def blog_article(article_url):
    selected_article = {}
    for _, blog in blogs_database.items():
        if blog["url"] == article_url:
            selected_article = blog
    return render_template('blog_article.html', article=selected_article)


@app.route('/contact', methods=["POST", "GET"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        today = datetime.today().strftime("%d/%m/%Y %H:%M:%S")
        name = form.name.data
        profession = form.profession.data
        email = form.email.data
        phone = form.phone.data
        message = form.message.data
        contact_worksheet = gsheet_file.worksheet("contact")
        worksheet_rows = len(contact_worksheet.get_all_values())
        new_data = [today, name, profession, email, phone, message]
        # Update Google Sheet with contacts
        for col in range(1, 7):
            contact_worksheet.update_cell(worksheet_rows + 1, col, str(new_data[col - 1]))

        # Send email notification
        html = f"Nouveau message recu!<br>" \
               f"<br>" \
               f"Date : {today}<br>" \
               f"Nom : {name}<br>" \
               f"Profession : {profession}<br>" \
               f"Email : {email}<br>" \
               f"Telephone : {phone}<br>" \
               f"Message : {message}<br><br>" \
               f"Voir https://docs.google.com/spreadsheets/d/1pj8GY-kOBB35c6W6dDo-dcyI_ecOOAvQ250930bjorc/edit#gid=580153284"
        msg = Message(
            subject='Nouveau contact sur Mon Educateur Canin',
            html=html,
            sender=('Contact - Mon Éducateur Canin', app.config['MAIL_USERNAME']),
            recipients=[EMAIL_RECIPIENT_1, EMAIL_RECIPIENT_2]
        )
        mail.send(msg)
        return redirect(url_for('contact_thank_you'))
    return render_template('contact.html', form=form)


@app.route('/contact/merci')
def contact_thank_you():
    return render_template('contact_thank_you.html')


@app.route('/mentions-légales')
def legal_mentions():
    return render_template('legal_mentions.html')


@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=80)
    app.run()

# TODO: Before committing -> change google credentials, change app.run server
