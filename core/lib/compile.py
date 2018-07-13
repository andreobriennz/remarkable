import os
import imp
from pathlib import Path
import datetime
# tasks = imp.load_source('tasks', 'projects/projects.py')
load = imp.load_source('loader', 'core/lib/loader.py')
saver = imp.load_source('saver', 'core/lib/saver.py')

# switch to using projects.json instead of projects.py:
import json
from pprint import pprint

with open('projects/projects.json') as f:
    data = json.load(f)


def load_section( path, tag = 'div' ):
    end_tag = tag.split()[0]

    if '.css' in path and Path( path ).is_file():
        file = '\n<style>\n'+load.raw( path )+'\n</style>\n'
    elif Path( path+'.html' ).is_file():
        file = load.raw( path+'.html' )
    elif Path( path+'.md' ).is_file():
        file = '\n<'+tag+'>\n'+load.html( path+'.md' )+'\n</'+end_tag+'>\n'
    else:
        print('path does not exist:'+path)
        file = ''
    
    return file


def index( project_name ):
    project_details = data['projects'][project_name]
    name = project_details['name']
    style = project_details['theme']
    root = 'projects/'+name+'/'

    if not os.path.exists( 'public/'+name ):
        os.makedirs( 'public/'+name )
        os.makedirs( 'public/'+name+'/content/' )
    
    markdowns = project_details['sections']
    main = ''
    for markdown_path in markdowns:
        markup = load.html( root+'content/'+markdown_path+'.md' )
        markdown_path = markdown_path.replace('/', '__')
        main += "<article id='{}'>\n{}\n</article>\n\n".format( markdown_path, markup )
        
        saver.save( markup, 'public/'+name+'/content/'+markdown_path+'.html' )

    style = load_section(
        root+'assets/custom.css'
    )

    nav = load_section( 
        root + 'partials/nav',
        'nav id="nav" class="nav"',
    )

    footer = load_section( 
        root + 'partials/footer',
        'footer',
    ).format( year = datetime.date.today().year )

    page = load.raw( 'core/default_project/layouts/index.html' ).format(
        title = name.title(),
        name = name,
        style = style,
        nav = nav,
        main = main,
        footer = footer,
        script = name,
    )

    saver.save( page, 'public/'+name+'/index.html' )
