import imp
tasks = imp.load_source('tasks', 'settings/projects.py')
load = imp.load_source('loader', 'lib/loader.py')
saver = imp.load_source('saver', 'lib/saver.py')

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

    page = load.raw( 'lib/theming/index.html' ).format(
        title = name.title(),
        main = main,
        style = name,
        script = name,
    )

    saver.save(page, 'public/' + root + 'index.html')
