from pathlib import Path


path = Path()

for file in path.glob('*'):
    print(file)



if(path.exists()):
    print(file)
else:
    path.mkdir()
