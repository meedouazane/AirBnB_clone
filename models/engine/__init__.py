#!/usr/bin/python3
''' __init__.py file unique FileStorage instance '''
from models.engine.file_storage import FileStorage


''' the variable storage, an instance of FileStorage '''
storage = FileStorage()
storage.reload()
