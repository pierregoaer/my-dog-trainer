from flask import Flask, render_template, request, redirect, url_for
from get_database import educateurs_database, blogs_database

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/educateurs', methods=["POST", "GET"])
def educateurs_list():
    if request.method == "GET":
        is_filtered = False
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
                           region=region)


@app.route('/educateur/<int:educateur_id>')
def educateur_page(educateur_id):
    educateur_request = educateurs_database[educateur_id]
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


@app.route('/blog')
def blog_page():
    return render_template('blog_page.html', blogs=blogs_database)


@app.route('/blog/<article_url>')
def blog_article(article_url):
    selected_article = {}
    for id, blog in blogs_database.items():
        if blog["url"] == article_url:
            selected_article = blog
    return render_template('blog_article.html', article=selected_article)


if __name__ == "__main__":
    # app.run('0.0.0.0')
    app.run()


# TODO: Before committing -> change google credentials, change app.run server
