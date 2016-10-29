from django.shortcuts import render
import json
from django.http import HttpResponse
from .models import UserVote

# Create your views here.


def save(request):
    data_label = ''
    data_lat = 0
    data_long = 0
    data_ip = ''

    json_data = json.loads(request.body)

    if 'loc_label' in json_data:
        data_label = json_data['loc_label']
    if 'latitude' in json_data:
        data_lat = json_data['latitude']
    if 'Longitude' in json_data:
        data_long = json_data['Longitude']
    if 'ip' in json_data:
        data_ip = json_data['ip']

    UserVote.objects.create(
        loc_label=data_label,
        latitude=data_lat,
        Longitude=data_long,
        ip=data_ip)

    return HttpResponse('saved', content_type='application/json')


def get(request):
    from django.core import serializers
    from django.db.models import Count

    db_data = UserVote.objects.all()

    json_data = serializers.serialize('json', db_data)
    print json_data
    return HttpResponse(json.dumps(json_data), content_type='application/json')



