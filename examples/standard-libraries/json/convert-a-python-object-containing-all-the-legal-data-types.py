import json
import pprint

pp = pprint.PrettyPrinter(indent=4)
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": (
        "Ann",
        "Billy"
    ),
    "pets": None,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]
}
breakpoint()
pp.pprint(json.dumps(x))
