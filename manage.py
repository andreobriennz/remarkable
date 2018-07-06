import imp
projects = imp.load_source('projects', 'lib/projects.py')

def index():
    projects.index()
index()