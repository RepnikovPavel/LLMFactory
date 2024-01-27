import os
import pathlib

base_python_path = 'C:/Python3/ml/Scripts'
current_file_path = pathlib.Path(__file__)
path = pathlib.Path(current_file_path)
project_path_ = path.parent.parent
requirements_path = os.path.join(project_path_, 'requirements.txt')
python_ = os.path.join(base_python_path, 'python.exe')
os.system(f'{python_} -m pip freeze > {requirements_path}')