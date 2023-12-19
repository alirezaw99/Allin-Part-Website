import os

def get_tumbnail_upload_path(instance, filename):
    folder = instance.part_number
    ext = filename.split('.')[-1]
    path = os.path.join('images','tumbnails', folder)
    filename = f'{folder}-thumbnail.{ext}'
    
    return os.path.join(path, filename)

def get_images_upload_path(instance, filename):
    id = 0
    folder = instance.part.part_number
    ext = filename.split('.')[-1]
    path = os.path.join('images', folder)
    
    while os.path.isfile(f'./media/images/{folder}/{folder}-{id}.{ext}'):
        id += 1
    
    filename = f'{folder}-{id}.{ext}'
    
    return os.path.join(path, filename)

