from flask import Flask, render_template, url_for, session, request, redirect, Blueprint

app = Flask(__name__)
app.secret_key = "WebRulls"

# global variables:
users = [{'username': 'ofri', 'lastname': 'hazan', 'email': "ofrihaz@post.bgu.ac.il"},
         {'username': 'peleg', 'lastname': "chub", 'email': "pelegc@post.bgu.ac.il"},
         {'username': 'anat', 'lastname': "vitelson", 'email': "anatvi@post.bgu.ac.il"},
         {'username': 'gal', 'lastname': "cohen", 'email': "galc@post.bgu.ac.il"}]


@app.route('/')
def main():
    return render_template('CV.html')


# ---------assignment10------------#
from assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)


#-------assignment9----
@app.route('/ex9')
@app.route('/assignment9', methods=['GET','POST'])
def assignment9():
    current_method = request.method
    if current_method == 'GET':
        if 'username' in request.args:
            username = request.args['username']
            lastname = request.args['lastname']
            email = request.args['email']

            if username is '' and lastname is '' and email is '':
                return render_template('assignment9.html', inSearch=True, users=users)
            searchedUsers = []
            for user in users:
                if (username is '' or user['username'] == username) and (lastname is '' or user['lastname'] == lastname) and (email is '' or user['email'] == email):
                    searchedUsers.append(user)
            if len(searchedUsers) == 0:
                return render_template('assignment9.html', isUser=False, inSearch=True)
            else:
                return render_template('assignment9.html', isUser=True, inSearch=True, user=searchedUsers)
        else:
            return render_template('assignment9.html')

    else:
        if request.form['username'] in users:
            session['username'] = request.form['username']
            session['lastname'] = request.form['lastname']
            session['email'] = request.form['email']
            session['isLogged'] = True
            return render_template('assignment9.html')
        else:
            users.append({'username': request.form['username'],
                          'lastname': request.form['lastname'],
                          'email': request.form['email']})
            session['username'] = request.form['username']
            session['lastname'] = request.form['lastname']
            session['email'] = request.form['email']
            session['isLogged'] = True
            return render_template('assignment9.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['username'] = ''
    session['lastname'] = ''
    session['email'] = ''
    session['isLogged'] = False
    return redirect(url_for('assignment9'))


#---------assignment8------------
@app.route('/ex8')
@app.route('/assignment8')
def assignment8():
    name = 'ARSENI'
    writer = 'Ofri'
    hobby = 'listening to music', 'travelling', 'going to the beach'
    song = 'perfect', 'im yours', 'montreo'
    return render_template('assignment8.html',
                           name=name,
                           writer=writer,
                           hobbies=hobby,
                           songs=song,
                           )


@app.route('/preferences')
def preferences():
    writer = 'Ofri'
    dog='nalla'
    name = ''
    hobby = 'listening to music', 'travelling', 'going to the beach'
    song = 'perfect', 'im yours', 'montreo'
    return render_template('preferences.html',
                           dog=dog,
                           name=name,
                           writer=writer,
                           hobbies=hobby,
                           songs=song
                           )


# ----ex7--------
@app.route('/contactList')
def contactlist():
    return render_template('contactList.html')


if __name__ == '_main_':
    app.run(debug=True)
