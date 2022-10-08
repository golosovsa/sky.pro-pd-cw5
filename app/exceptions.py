"""
    App exceptions
"""

from werkzeug.exceptions import NotFound, BadRequest


class ItemNotFound(NotFound):

    def __init__(self, message, *args, **kwargs):
        super(ItemNotFound, self).__init__(*args, **kwargs)
        self.description = f"{message} {self.description}"


class InvalidDataContent(BadRequest):

    def __init__(self, message, *args, **kwargs):
        super(InvalidDataContent, self).__init__(*args, **kwargs)
        self.description = f"{message} {self.description}"
