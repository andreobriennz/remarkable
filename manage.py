import imp
projects = imp.load_source('projects', 'core/lib/projects.py')

# run with: runp manage.py test
# def test():
#     print('test passed!')

def index():
    projects.index()
index()