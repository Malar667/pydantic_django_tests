from typing import List

from django.http import JsonResponse
from ninja import NinjaAPI
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from stats.models import Author
from stats.serializers import (
    AuthorNinjaSchema,
    AuthorOut,
    AuthorSchema,
    AuthorSerializer,
)
from stats.tests.factories import AuthorFactory


class AuthorViewSet(viewsets.GenericViewSet):
    serializer_class = AuthorSerializer

    @action(detail=False, methods=["POST"])
    def create_batch(self, request):
        AuthorFactory.create_batch(1000)

        return Response()

    @action(detail=False, methods=["GET"])
    def performance(self, request):
        db_data = Author.objects.all()

        serializer = AuthorSerializer(data=db_data, many=True)
        serializer.is_valid()

        return Response(serializer.data)


class AuthorDjanticViewSet(viewsets.ViewSet):
    @action(detail=False, methods=["GET"])
    def performance(self, request):
        db_data = Author.objects.all()

        response_data = AuthorSchema.from_django(db_data, many=True)
        #
        # response_data = []
        # for author in db_data:
        #     schema = AuthorSchema.from_django(author)
        #     response_data.append(schema.dict())

        return Response(response_data)


api = NinjaAPI()


@api.get("/performance", response=List[AuthorNinjaSchema])
def performance(request):
    db_data = Author.objects.all()
    return db_data
