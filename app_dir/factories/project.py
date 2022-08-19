import factory
from faker import Factory
from ..core.loading import get_model

faker = Factory.create()


class ProjectFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_model('project', 'Project')

    name = faker.name()
    description = faker.text()
