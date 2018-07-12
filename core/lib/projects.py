import imp
from pathlib import Path
import datetime
tasks = imp.load_source('tasks', 'settings/projects.py')
load = imp.load_source('loader', 'core/lib/loader.py')
saver = imp.load_source('saver', 'core/lib/saver.py')

def load_section( path, default, tag = 'div' ):
    end_tag = tag.split()[0]

    if '.css' in path:
        file = '\n<style>\n'+load.raw( path )+'\n</style>\n'
    elif Path( path+'.html' ).is_file():
        file = load.raw( path+'.html' )
    elif Path( path+'.md' ).is_file():
        file = '\n<'+tag+'>\n'+load.html( path+'.md' )+'\n</'+end_tag+'>\n'
    else:
        file = load.raw( default )
    
    return file

def index():
    task = tasks.tasks[0]

    name = tasks.tasks[0]['name']
    style = tasks.tasks[0]['theme'] != '' and tasks.tasks[0]['theme'] or tasks.tasks[0]['style']
    root = task['root_file']
    
    markdowns = task['sections']
    main = ''
    for markdown in markdowns:
        markup = load.html( 'src/' + root + markdown )
        main += "<article id='{}'>\n{}\n</article>\n\n".format( markdown, markup )

    style = load_section(
        'lib/theming/'+root+'custom.css',
        'lib/theming/'+root+'custom.css',
    )
    
    nav = load_section( 
        'src/' + root + 'partials/nav',
        'lib/theming/partials/nav.html',
        'nav id="nav" class="nav"',
    )

    footer = load_section( 
        'src/' + root + 'partials/footer',
        'lib/theming/partials/footer.html',
        'footer',
    ).format( year = datetime.date.today().year )

    page = load.raw( 'lib/theming/index.html' ).format(
        title = name.title(),
        name = name,
        style = style,
        nav = nav,
        main = main,
        footer = footer,
        script = name,
    )

    saver.save(page, 'public/' + root + 'index.html')
