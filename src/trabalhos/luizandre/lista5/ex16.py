import os
from pathlib import Path

os.rename('numeros.txt', 'numeros.txt')

for item in Path('.').glob('*.txt'):
    os.rename(item.name, '_' + item.name)
