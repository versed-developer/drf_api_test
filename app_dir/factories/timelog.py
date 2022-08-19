import factory
from faker import Factory

from . import ProjectFactory
from ..core.loading import get_model

faker = Factory.create()


class TimeLogFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_model('timelog', 'TimeLog')

    project = ProjectFactory()
    description = faker.text()
