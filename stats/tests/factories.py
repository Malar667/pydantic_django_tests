import factory

from stats.models import Author


class AuthorFactory(factory.django.DjangoModelFactory):
    first_name = factory.Sequence(lambda n: "Name %s" % n)
    last_name = factory.Sequence(lambda n: "Surname %s" % n)

    class Meta:
        model = Author
