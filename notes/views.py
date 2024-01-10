from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Note
from .serializers import NoteSerializer

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_routes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]

    return Response(routes)


from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_note(request, pk):
    try:
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(note, many=False)
        return Response({'message': 'Note fetched successfully.', 'note': serializer.data}, status=200)
    except Note.DoesNotExist:
        return Response({'message': 'Note not found.'}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createNote(request):
    data = request.data
    note = Note.objects.create(body=data.get('body', ''))
    serializer = NoteSerializer(note)
    return Response({'message': 'Note created successfully.', 'note': serializer.data}, status=201)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateNote(request, pk):
    try:
        note = Note.objects.get(id=pk)
    except Note.DoesNotExist:
        return Response({'message': 'Note not found.'}, status=404)

    data = request.data
    serializer = NoteSerializer(instance=note, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Note updated successfully.', 'note': serializer.data}, status=200)
    return Response({'message': 'Invalid data.', 'errors': serializer.errors}, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteNote(request, pk):
    try:
        note = Note.objects.get(id=pk)
        note.delete()
        return Response({'message': 'Note deleted successfully.'}, status=204)
    except Note.DoesNotExist:
        return Response({'message': 'Note not found.'}, status=404)


