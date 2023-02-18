from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, jsonify, current_app, session
from flask_login import current_user, login_required
from app import db
from app.main.forms import EditProfileForm, QuoteForm
from app.models import User
from app.helpers import own_shares, lookup, usd, apology, flash_errors
from app.main import bp

@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template('index.html', title='Portfolio')


@bp.route('/quote', methods=['GET', 'POST'])
@login_required
def quote():
    form = QuoteForm()
    if form.validate_on_submit():
        symbol = form.quote.data
        quote = lookup(symbol)
        if not quote:
            flash('Stock symbol not valid')
            return redirect(url_for('quote'))
        return render_template('quote.html', title='Quote', quote=quote)
    return redirect(url_for('quote'))


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)