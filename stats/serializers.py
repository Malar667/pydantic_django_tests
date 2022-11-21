import djantic
import ninja
from rest_framework import serializers

from stats.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "last_name", "first_name")


class AuthorSchema(djantic.ModelSchema):
    class Config:
        model = Author
        model_fields = ("id", "last_name", "first_name")


class AuthorNinjaSchema(ninja.ModelSchema):
    class Config:
        model = Author
        model_fields = ("id", "last_name", "first_name")
