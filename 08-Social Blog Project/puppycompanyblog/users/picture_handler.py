#users/picture_handler.py
"""File allows us to upload pictures"""

import os
from PIL import Image
from flask import url_for, current_app

#allows user to add profile picture
def add_profile_pic(pic_upload,username):

    #ex: mypic.jpg
    filename = pic_upload.filename

    #grab extention type  'mypicture.jpg' --> jpg
    ext_type = filename.split('.')[-1]

    #saves it as user's unique username username.jpg'
    storage_filename = str(username)+'.'+ext_type

    #create file path to save it
    filepath = os.path.join(current_app.root_path,'static/profile_pics',storage_filename)

    output_size = (200,200)

    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
