from flask import render_template, redirect, url_for, flash
from . import auth
from .forms import SignupForm
from ..models import db, User

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=form.password.data,
        )
        db.session.add(new_user)
        db.session.commit()
        flash('User created successfully!')
        return redirect(url_for('auth.signup'))
    return render_template('signup.html', form=form)
