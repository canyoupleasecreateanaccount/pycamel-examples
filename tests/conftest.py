from pycamel import CamelConfig, RouterMaker

WRONG_PARAMETERS = [
    123123123,
    "asdasd",
    "!@413aaa"
]

CamelConfig(host='https://send-request.me/api', project_validation_key='data')
v1_maker = RouterMaker('')

