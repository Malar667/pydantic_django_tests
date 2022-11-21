from typing import List

from codetiming import Timer
from ninja import NinjaAPI
from pydantic import parse_obj_as
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.utils import json

from stats.models import Author
from stats.serializers import AuthorDjanticSchema, AuthorNinjaSchema, AuthorSerializer
from stats.tests.factories import AuthorFactory


class AuthorViewSet(viewsets.GenericViewSet):
    serializer_class = AuthorSerializer

    @action(detail=False, methods=["POST"])
    @Timer()
    def create_batch(self, request):
        AuthorFactory.create_batch(1000)

        return Response()

    @action(detail=False, methods=["POST"])
    @Timer()
    def performance_create(self, request):

        serializer = AuthorSerializer(data=request.data, many=True)
        serializer.is_valid()
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["GET"])
    @Timer()
    def performance_single(self, request):
        db_data = Author.objects.first()

        print(db_data)

        serializer = AuthorSerializer(db_data)

        return Response(serializer.data)

    @action(detail=False, methods=["GET"])
    @Timer()
    def performance_list(self, request):
        db_data = Author.objects.all()

        serializer = AuthorSerializer(data=db_data, many=True)
        serializer.is_valid()

        return Response(serializer.data)


class AuthorDjanticViewSet(viewsets.ViewSet):
    @action(detail=False, methods=["POST"])
    @Timer()
    def performance_create(self, request):
        json_data = json.loads(request.body)

        schemas = parse_obj_as(List[AuthorDjanticSchema], json_data)

        build_data = [
            Author(first_name=schema.first_name, last_name=schema.last_name)
            for schema in schemas
        ]

        Author.objects.bulk_create(build_data)

        return Response(status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["GET"])
    @Timer()
    def performance_single(self, request):
        db_data = Author.objects.first()

        response_data = AuthorDjanticSchema.from_django(db_data)

        return Response(response_data.dict())

    @action(detail=False, methods=["GET"])
    @Timer()
    def performance_list(self, request):
        db_data = Author.objects.all()

        response_data = [
            AuthorDjanticSchema.from_django(author).dict() for author in db_data
        ]

        # This doesn't return good structure
        # many=True vs many=False returns list vs single object, utter bullshit
        # response_data = AuthorSchema.from_django(db_data, many=True)

        return Response(response_data)


api = NinjaAPI()

# TODO using timer here is tricky because bunch of logic is actually in api.get
@api.get("/performance_single", response=AuthorNinjaSchema)
@Timer()
def performance_single(request):
    db_data = Author.objects.first()
    return db_data


@api.get("/performance_list", response=List[AuthorNinjaSchema])
@Timer()
def performance_list(request):
    db_data = Author.objects.all()
    return db_data
