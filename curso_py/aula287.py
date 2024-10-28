import os
import shutil

HOME =  os.path.expanduser('~')
DESKTOP =os.path.join(HOME, 'Área de Trabalho')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Nova f')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')
print(NOVA_PASTA)

shutil.rmtree(NOVA_PASTA)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)