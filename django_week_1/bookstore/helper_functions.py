def get_object_by_id(id, list_of_objects):
    for obj in list_of_objects:
        if obj['id'] == id:
            return obj
    return
