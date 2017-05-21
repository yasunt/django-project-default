from accounts.models import CustomUser
from .models import Something, Tag


def make_example_objects():
    
    user = CustomUser.objects.create_user(username='test_user01', password='testuser01')

    for i in range(10):
        tag = Tag(name='Tag {0}'.format(i+1))
        tag.save()

        smt = Something(
            name='Something: {0}'.format(i+1),
            description='This is a object example {0}'.format(i+1),
            user=user,
        )
        smt.save()
        smt.tags.add(tag)
        smt.save()
