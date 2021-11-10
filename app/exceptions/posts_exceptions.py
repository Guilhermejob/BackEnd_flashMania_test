class TypeNotAllowedError(Exception):
    types = {
        str: "string",
        int: "integer",
        float: "float",
        list: "list",
        dict: "dictionary",
        bool: "boolean",
    }

    def __init__(self, title, author, tags, content):

        self.message = {
            'wrong fields': [
                {
                    "title": f'{self.types[type(title)]}'
                },
                {
                    "author": f'{self.types[type(author)]}'
                },
                {
                    "tags": f'{self.types[type(tags)]}'
                },
                {
                    "content": f'{self.types[type(content)]}'
                },
            ]
        }
