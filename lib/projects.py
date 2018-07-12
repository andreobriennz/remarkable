import imp
from pathlib import Path
import datetime
tasks = imp.load_source('tasks', 'settings/projects.py')
load = imp.load_source('loader', 'lib/loader.py')
saver = imp.load_source('saver', 'lib/saver.py')

def load_section( path, default, tag = 'div' ):
    end_tag = tag.split()[0]

    if Path( path+'.html' ).is_file():
        nav = load.raw( path+'.html' )
    elif Path( path+'.md' ).is_file():
        nav = '\n<'+tag+'>\n'+load.html( path+'.md' )+'\n</'+end_tag+'>\n'
    else:
        nav = load.raw( default )
    
    return nav

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
        nav = nav,
        main = main,
        footer = footer,
        style = name,
        script = name,
    )

    saver.save(page, 'public/' + root + 'index.html')
