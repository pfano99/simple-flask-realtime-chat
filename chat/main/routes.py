from flask import redirect, url_for, render_template
from flask_login import login_required, current_user

from chat.models import User, Message
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))
    else:
        return redirect(url_for("Auth.login"))


@main.route('/chat/<int:user_id>')
def message(user_id: int):
    messages = Message.query.filter((Message.sender_id == current_user.id) & (Message.recipient_id == user_id) |
                                    (Message.recipient_id == current_user.id) & (Message.sender_id == user_id))

    context = {
        "recipient": user_id,
        "messages": messages
    }
    return render_template('chat.html', context=context)


@login_required
@main.route("/dashboard")
def dashboard():
    print("sssssss")
    if not current_user.is_authenticated:
        return redirect(url_for("Auth.login"))
    print(current_user)
    users = User.query.all()
    users = filter(lambda x: x.id != current_user.id, users)
    return render_template("dashboard.html", users=users)
