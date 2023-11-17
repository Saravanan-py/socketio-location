from django.http import HttpResponse
import os
import socketio
from .models import socketioTable
from rest_framework.views import APIView

thread = None
basedir = os.path.dirname(os.path.realpath(__file__))
sio = socketio.Server(async_mode=None)


class SYNCapi(APIView):
    def get(self, request):
        return HttpResponse(open(os.path.join(basedir, 'static/index.html')))


@sio.event
def connect(sid, environ):
    sio.emit('connected', {'data': 'Connected to server'}, room=sid)


@sio.event
def disconnect(sid):
    print(f'[{sid}] Client disconnected')


@sio.event
def generate_random_data(sid, data):
    if data is not None:
        data_response = {
            'response_code': 200,
            'message': 'Data sended successfully.',
            'statusFlag': True,
            'status': 'SUCCESS',
            'errorDetails': None,
            'data': data
        }
        print(data)
        sio.emit('my_response1', {'data': data_response})
        db = socketioTable(uniqueID=data['uniqueId'], latitude=data['latitude'], longitude=data['longitude'], timestamp = data['timestamp'])
        db.save()







# from django.shortcuts import render
# from rest_framework.response import Response
# from django.http import HttpResponse
#
# # Create your views here.
#
# async_mode = None
#
# import os
#
# from django.http import HttpResponse
# import socketio
#
# basedir = os.path.dirname(os.path.realpath(__file__))
# sio = socketio.Server(async_mode=async_mode)
# thread = None
#
#
# def index(request):
#     global thread
#     if thread is None:
#         thread = sio.start_background_task(background_thread)
#     return HttpResponse(open(os.path.join(basedir, 'static/index.html')))
#
#
# def background_thread():
#     """Example of how to send server generated events to clients."""
#     count = 0
#     while True:
#         sio.sleep(10)
#         count += 1
#         sio.emit('my_response', {'data': 'Server generated event'},
#                  namespace='/test')
#
#
#
# @sio.event
# def my_event(sid, message):
#     sio.emit('my_response', {'data': message['data']}, room=sid)
#
#
# @sio.event
# def my_broadcast_event(sid, message):
#     print(f"[{sid}] Message: {message['data']}")
#     sio.emit('my_response', {'data': message['data']})
#
#
# @sio.event
# def join(sid, message):
#     sio.enter_room(sid, message['room'])
#     print(f" Entered room: {message['room']}")
#     sio.emit('my_response', {'data': 'Entered room: ' + message['room']},
#              room=sid)
#
#
# @sio.event
# def leave(sid, message):
#     sio.leave_room(sid, message['room'])
#     print(f"Left room: {message['room']}")
#     sio.emit('my_response', {'data': 'Left room: ' + message['room']},
#              room=sid)
#
#
# @sio.event
# def close_room(sid, message):
#     sio.emit('my_response',
#              {'data': 'Room ' + message['room'] + ' is closing.'},
#              room=message['room'])
#     print(f"Closed room: {message['room']}")
#     sio.close_room(message['room'])
#
#
# @sio.event
# def my_room_event(sid, message):
#     print(f"Message from room: {message['data']}")
#     sio.emit('my_response', {'data': message['data']}, room=message['room'])
#
#
# @sio.event
# def disconnect_request(sid):
#     sio.disconnect(sid)
#
#
# @sio.event
# def connect(sid, environ):
#     sio.emit('my_response', {'data': 'Connected', 'count': 0}, room=sid)
#
#
# @sio.event
# def disconnect(sid):
#     print('Client disconnected')

# import os
# from django.http import HttpResponse
# import socketio
# import random
# import uuid
#
# # Create a new Socket.IO server
# sio = socketio.Server(async_mode=None)
# thread = None
#
#
# def index(request):
#     global thread
#     if thread is None:
#         thread = sio.start_background_task(background_thread)
#     return HttpResponse(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/index.html')))
#
#
# def generate_random_location():
#     """Generate random latitude and longitude."""
#     latitude = round(random.uniform(-90, 90), 6)
#     longitude = round(random.uniform(-180, 180), 6)
#     return latitude, longitude
#
#
# def background_thread():
#     """Generate and emit a random string every seconds."""
#     import time
#     import random
#     while True:
#         sio.sleep(1)
#         unique_id = "VRD"+"".join(random.choice("123456789") for _ in range(4))
#
#         # Generate random latitude and longitude
#         latitude, longitude = generate_random_location()
#
#         # Print the data in the server console
#         data = {'Unique ID:': unique_id,
#                 'Latitude:': latitude,
#                 'Longitude:': longitude
#                 }
#         print(data)
#
#         # Send the data to all connected clients
#         sio.emit('location_data', {'id': unique_id, 'latitude': latitude, 'longitude': longitude}, namespace='/test')
#
#
# @sio.event
# def connect(sid, environ):
#     print('Client connected:', sid)
#
#
# @sio.event
# def disconnect(sid):
#     print('Client disconnected:', sid)

