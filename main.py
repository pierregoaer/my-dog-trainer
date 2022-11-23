from flask import Flask, render_template, request, redirect, url_for
from get_database import database

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/educateurs', methods=["POST", "GET"])
def educateurs_list():
    if request.method == "GET":
        is_filtered = False
        return render_template('educateurs_list.html', database=database, is_filtered=is_filtered)
    if request.method == "POST":
        department = request.form["department"]
        return redirect(url_for('department_search', department=department))


@app.route('/educateurs/departement/<int:department>', methods=["POST", "GET"])
def department_search(department):
    is_filtered = True
    filtered_database = {}
    for id, educateur in database.items():
        if educateur["department"] == department:
            filtered_database[id] = educateur
    return render_template('educateurs_list.html', database=filtered_database, is_filtered=is_filtered)


@app.route('/educateurs/region/<region>', methods=["POST", "GET"])
def region_search(region):
    region = region.replace('-', ' ')
    counter = 0
    all_results = {}
    first_6_results = {}
    remaining_results = {}
    for id, educateur in database.items():
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
                           region=region)


@app.route('/educateur/<int:educateur_id>')
def educateur_page(educateur_id):
    educateur_request = database[educateur_id]
    return render_template('educateur_page.html', educateur=educateur_request)


if __name__ == "__main__":
    # app.run('0.0.0.0')
    app.run()


# TODO: Before committing -> chang google credentials, change app.run server
