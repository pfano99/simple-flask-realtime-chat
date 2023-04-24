from flask_socketio import emit, join_room, leave_room
from flask_login import current_user
from .. import socketio
from chat.models import Message
from chat import db


@socketio.on('joined', namespace='/chatx')
def joined(message):
    room = generate_room_id(int(current_user.id), int(message["msg"]))
    join_room(room)
    emit('status', {'msg': current_user.first_name + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chatx')
def text(message):
    recipient = int(message["recipient"])
    db.session.add(
        Message(
            body=message["msg"],
            sender_id=current_user.id,
            recipient_id=recipient
        )
    )
    db.session.commit()
    room = generate_room_id(int(current_user.id), recipient)
    emit('message', message, room=room)


def generate_room_id(user_id_1: int, user_id_2: int):
    return "{}_{}".format(min(user_id_1, user_id_2), max(user_id_1, user_id_2))
