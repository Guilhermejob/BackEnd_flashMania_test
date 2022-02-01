class TypeNotAllowedError(Exception):
    types = {
        str: "string",
        int: "integer",
        float: "float",
        list: "list",
        dict: "dictionary",
        bool: "boolean",
    }

    def __init__(self, name, price, content):

        self.message = {
            'wrong fields': [
                {
                    "title": f'{self.types[type(name)]}'
                },
                {
                    "price": f'{self.types[type(price)]}'
                },
                {
                    "content": f'{self.types[type(content)]}'
                },
            ]
        }
