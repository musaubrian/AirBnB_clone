#!/usr/bin/env python3
"""
initialize package
"""

from models.engine.file_storage import FileStorage

storage = FileStorage
storage.reload()
