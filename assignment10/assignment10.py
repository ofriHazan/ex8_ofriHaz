from flask import Flask, render_template, request, redirect, Blueprint, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "WebRulls"


# ----assignment10 blueprint definition----#
assignment10 = Blueprint(
    'assignment10',
    __name__,
    static_folder='static',
    static_url_path='/assignment10',
    template_folder='templates'
)

# ----------database connection-------- #
# ------------------------------------- #


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='root',
                                         database='web_course')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True
    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


# -------------routes-------------#

# -----------select------------------ #
# ----------------------------------- #
@assignment10.route('/ex10')
@assignment10.route('/assignment10')
@assignment10.route('/users')
def users():
    # con=mysql.connector.connect('web_course')
    query = "select * from web_course.users_table"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)
# ----------------------------------- #
# ----------------------------------- #


# -------------insert---------------- #
# ----------------------------------- #


@assignment10.route('/insert_user', methods=['GET','POST'])
def insert_users():
    if request.method == 'POST':
        username = request.form['username']
        lastname = request.form['lastname']
        email = request.form['email']
        if username == '' or lastname == '' or email == '':
            flash('You need to fill all the boxes!')
            return redirect('/users')
        else:
            sheilta = "SELECT email FROM web_course.users_table WHERE email='%s';" % email
            sheilta_validation = interact_db(query=sheilta, query_type='fetch')
            if len(sheilta_validation) == 0:
                query = "INSERT INTO web_course.users_table(username, lastname, email) value ('%s', '%s', '%s');" \
                        % (username, lastname, email)
                interact_db(query=query, query_type='commit')
                flash('The user was added successfully!')
                return redirect('/users')
            else:
                flash(f'user {username} is already registered')
                return redirect('/users')
    return render_template('assignment10.html', req_method=request.method)


# ----------------------------------- #
# ----------------------------------- #

# -------------delete---------------- #
# ----------------------------------- #


@assignment10.route('/delete_user', methods=['POST'])
def delete_users():
    user_id = request.form['id']
    sheilta = "SELECT username FROM web_course.users_table WHERE id='%s';" % user_id
    sheilta_validation = interact_db(query=sheilta, query_type='fetch')
    if len(sheilta_validation) > 0:
        query = "delete from web_course.users_table where id='%s';" % user_id
        interact_db(query=query, query_type='commit')
        flash('The user was deleted successfully!')
        return redirect('/users')
    else:
        flash('The user was NOT deleted because he does not exist')
        return redirect('/users')

# -------------update---------------- #
# ----------------------------------- #


@assignment10.route('/update_user', methods=['GET','POST'])
def update_users():

        id = request.form['id']
        username = request.form['username']
        lastname = request.form['lastname']
        email = request.form['email']
        if username == '' or lastname == '' or email == '':
            flash('You need to fill all the boxes!')
            return redirect('/users')
        else:
            sheilta = "SELECT username FROM web_course.users_table WHERE id='%s';" % id
            sheilta_validation = interact_db(query=sheilta, query_type='fetch')
            if len(sheilta_validation) > 0:
                query = "UPDATE web_course.users_table SET username='%s', lastname='%s', email='%s' WHERE id='%s';" % \
                    (username, lastname, email, id)
                interact_db(query=query, query_type='commit')
                flash('The user was updated successfully!')
                return redirect('/users')
            else:
                flash(f'user {username} does not exist')
                return redirect('/users')
