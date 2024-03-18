'''
Created on Nov 17, 2020

@author: Sergiu Ciubotariu
'''

from ui.console import VectorUI
from infrastructure.vectorrepository import VectorRepository

repo = VectorRepository()
ui = VectorUI(repo)
ui.start()