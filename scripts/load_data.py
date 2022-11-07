from stats.tests.factories import AuthorFactory


def populate_authors():
    AuthorFactory.create_batch(1000)
