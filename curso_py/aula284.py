import os
from itertools import count


caminho = r'C:\\Users\\T-Gamer\\Desktop\\Nova f'
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'pasta atual', root)
    
    for dirs_ in dirs:
        print(the_counter, 'Dir', dirs_) 
    
    for file_ in files:
        caminho_completo = os.path.join(root,file_)
        print(the_counter, 'file', caminho_completo) 
