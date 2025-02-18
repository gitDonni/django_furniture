from django.db.models.signals import post_delete
from django.dispatch import receiver


def delete_file(instance, field_name):
    field = getattr(instance, field_name, None)
    if field and hasattr(field, 'delete'):
        field.delete(False)


MODEL_FILE_FIELDS = {
    'User': ['image'],
}


@receiver(post_delete)
def delete_files(sender, instance, **kwargs):
    model_name = sender.__name__
    if model_name in MODEL_FILE_FIELDS:
        for field_name in MODEL_FILE_FIELDS[model_name]:
            delete_file(instance, field_name)