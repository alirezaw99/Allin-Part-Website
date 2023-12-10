import os

def get_upload_path(instance, filename):
    file = instance.part_number
    ext = filename.split('.')[-1]
    filename = f'img{instance.id}.{ext}'
    
    path = os.path.join('images', file)
    
    return os.path.join(path, filename)

