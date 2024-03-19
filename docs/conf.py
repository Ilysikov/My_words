
import sys
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent.parent.parent
project = BASE_DIR.name

# Добавляем проект с модулями в путь Python
sys.path.insert(0, str(BASE_DIR /'Users/ivanlysikov/PycharmProjects/pythonProject6'))
# extensions = [,
# ]
master_doc = 'index'
templates_path = ["_templates"]
exclude_patterns = []
language = "ru"
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
