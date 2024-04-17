import flask_socketio
from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

# Dictionary to store active chat rooms and their messages
active_rooms = {}

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chat</title>
    </head>
    <body>
        <div id="chat"></div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.4.0/socket.io.js"></script>
        <script>
            var socket = io.connect('http://' + document.domain + ':' + location.port);

            socket.on('update', function(data) {
                var chatDiv = document.getElementById('chat');
                chatDiv.innerHTML = '';
                data.messages.forEach(function(message) {
                    chatDiv.innerHTML += '<p>' + message.username + ': ' + message.message + '</p>';
                });
            });

            var username = prompt('Enter your username:');
            var room = prompt('Enter the room name:');

            socket.emit('join', {'username': username, 'room': room});

            while (true) {
                var message = prompt('Enter your message (or type "exit" to leave):');
                if (message === 'exit') {
                    socket.emit('leave', {'username': username, 'room': room});
                    break;
                }
                socket.emit('message', {'username': username, 'room': room, 'message': message});
            }
        </script>
    </body>
    </html>
    """

@socketio.on('join')
def handle_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    if room not in active_rooms:
        active_rooms[room] = []
    active_rooms[room].append({'username': username, 'message': 'joined the chat'})
    socketio.emit('update', {'room': room, 'messages': active_rooms[room]}, room=room)

@socketio.on('leave')
def handle_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    active_rooms[room].append({'username': username, 'message': 'left the chat'})
    socketio.emit('update', {'room': room, 'messages': active_rooms[room]}, room=room)

@socketio.on('message')
def handle_message(data):
    username = data['username']
    room = data['room']
    message = data['message']
    active_rooms[room].append({'username': username, 'message': message})
    socketio.emit('update', {'room': room, 'messages': active_rooms[room]}, room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
