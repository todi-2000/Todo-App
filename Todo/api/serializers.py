from rest_framework import serializers
from .models import Notes

class NotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields='__all__'
