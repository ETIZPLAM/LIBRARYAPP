from rest_framework import serializers
from django.utils import timezone
from .models import booksclass


class bookserializers(serializers.ModelSerializer):
    class Meta:
        model=booksclass
        fields='__all__'

    def create(self, validated_data):
        obj=super().create(validated_data)

        obj.created_at = timezone.now()
        obj.save()
        return obj