from pycamel import CamelConfig, RouterMaker

CamelConfig(host='https://reqres.in/api', project_validation_key='data')

v1_maker = RouterMaker('')

