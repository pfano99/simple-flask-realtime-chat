import datetime

from flask_login import UserMixin
from chat import db

from chat import login_manager


@login_manager.user_loader
def load_user(_id):
    return User.query.get(_id)


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    password = db.Column(db.String(50), nullable=False)

    sent = db.relationship('Message', foreign_keys="Message.sender_id", backref='user_sender', lazy=True,
                           cascade="all, delete-orphan")
    received = db.relationship('Message', foreign_keys="Message.recipient_id", backref='user_recipient', lazy=True,
                               cascade="all, delete-orphan")

    def __repr__(self):
        return "User( id: {}, first-name: {}, last-name: {}, email: {})".format(
            self.id, self.first_name, self.last_name, self.email
        )


class Message(db.Model):
    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    date_sent = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "Message ( id: {}, sender_id: {}, recipient_id: {}, body: {}, sent date: {}".format(
            self.id, self.sender_id, self.recipient_id, self.body, self.date_sent
        )
