import imp
from pathlib import Path
import datetime
tasks = imp.load_source('tasks', 'projects/projects.py')
load = imp.load_source('loader', 'core/lib/loader.py')
saver = imp.load_source('saver', 'core/lib/saver.py')

def load_section( path, default, tag = 'div' ):
    end_tag = tag.split()[0]

    if '.css' in path:
        if Path( path ).is_file():
            file = '\n<style>\n'+load.raw( path )+'\n</style>\n'
    elif Path( path+'.html' ).is_file():
        file = load.raw( path+'.html' )
    elif Path( path+'.md' ).is_file():
        file = '\n<'+tag+'>\n'+load.html( path+'.md' )+'\n</'+end_tag+'>\n'
    # consider removing default if created automatically:
    elif Path( default+'.html' ).is_file():
        file = load.raw( default+'.html' )
    
    return file

def index():
    task = tasks.tasks[0]

    name = tasks.tasks[0]['name']
    style = tasks.tasks[0]['theme'] != '' and tasks.tasks[0]['theme'] or tasks.tasks[0]['style']
    root = task['root_file']
    
    markdowns = task['sections']
    main = ''
    for markdown_path in markdowns:
        markup = load.html( 'projects/'+root+'content/'+markdown_path+'.md' )
        main += "<article id='{}'>\n{}\n</article>\n\n".format( markdown_path, markup )

    style = load_section(
        'projects/'+root+'assets/custom.css',
        '',
    )
    print('projects/'+root+'assets/custom.css')
    nav = load_section( 
        'projects/' + root + 'partials/nav',
        'core/default_project/partials/nav',
        'nav id="nav" class="nav"',
    )

    footer = load_section( 
        'projects/' + root + 'partials/footer',
        'core/default_project/partials/footer',
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

    saver.save(page, 'public/'+root+'index.html')
