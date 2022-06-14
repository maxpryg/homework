from django.http import Http404


def get_object_by_id_or_404(id, list_of_objects):
    for obj in list_of_objects:
        if obj['id'] == id:
            return obj

    raise Http404('Object not found.')
