### Gestión de Paquetes para Python ###

# pip/PIP
# pip list
# pip uninstall <libreria>
# pip show <libreria>
# https://pypi.org

# Importaciones

import pandas as pd
import numpy as np
import requests as rq
import datetime as dt
from package import arithmetics

# x = 42
# x = x + 1
# print(help(np.sort))
print(np.version.version)

# Numpy
print('Numpy')
numpy_array = np.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array)) # <class 'numpy.ndarray'>
print(numpy_array) # [35 24 62 52 30 30 17]
print(numpy_array * 2) # [ 70  48 124 104  60  60  34]
print()

# Pandas
print('Pandas')
print(pd.__version__) # 2.2.2(04/09/24)
print()

# Requests
print('Requests')
res = rq.get('https://pokeapi.co/api/v2/pokemon?limit=151')
print(res) # <Response [200]>
print(res.status_code) # 200
# print(res.json())

# Datetime
print('Datetime')
today = dt.date.today()
print(today)  
print()

# Aritmetics Package
print('Aritmetics Package')
print(arithmetics.sum(1, 4)) # 5
