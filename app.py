from flask import Flask, render_template, url_for, session, request, redirect

app = Flask(__name__)
app.secret_key = "WebRulls"

# global variables:

users = [{'username': 'ofri', 'lastname': 'hazan', 'email': "ofrihaz@post.bgu.ac.il"},
         {'username': 'peleg', 'lastname': "chub", 'email': "pelegc@post.bgu.ac.il"},
         {'username': 'anat', 'lastname': "vitelson", 'email': "anatvi@post.bgu.ac.il"}]


@app.route('/')
def main():
    return render_template('CV.html')

#-------assignment9----
@app.route('/ex9')
@app.route('/assignment9', methods=['GET','POST'])
def assignment9():
    # session['isLogged'] = False
    current_method = request.method
    # if current_method in session:
    #     user_name, last_name, email = session['user_name'], session['lastname'], session['email']
    # else:
    if current_method == 'GET':
        if 'username' in request.args:
            username = request.args['username']
            lastname = request.args['lastname']
            email = request.args['email']

            if 'username' is '' and 'lastname' is '' and 'email' is '':
                return render_template('assignment9.html', users=users)
            filtered_users = []
            for user in users:
                if (username is '' or user['username'] == username) and (lastname is '' or user['lastname'] == lastname) and (email is '' or user['email'] == email):
                    filtered_users.append(user)
            if len(filtered_users) == 0:
                return render_template('assignment9.html', isUser=False, inSearch=True)
            else:
                return render_template('assignment9.html',isUser=True, inSearch=True, users=filtered_users)
        else:
            return render_template('assignment9.html')

    # if request.args['username'] in users:
    #     return render_template('assignment9.html', isUser=True, inSearch=True,
    #                            username=request.args['username'], user=users[request.args['username']])
    # else:
    #     return render_template('assignment9.html', isUser=False, inSearch=True)

    # elif current_method == 'POST':
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
                           songs=song)


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