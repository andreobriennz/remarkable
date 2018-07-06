import imp
tasks = imp.load_source('tasks', 'settings/projects.py')

load = imp.load_source('loader', 'lib/loader.py')
saver = imp.load_source('saver', 'lib/saver.py')
# router = imp.load_source('router', 'routes.py')

# path = '/blog/welcome'

# route = router.routes['posts'][path]

# post = load.html(route['file'])

# html = post

# saver.save(html, 'public/blog.html')

# print(post['html'])

def index():
    task = tasks.tasks[0]

    root = task['root_file']

    # loop:
    html = ''

    markdowns = task['sections']
    for markdown in markdowns:
        print( 'src/' + root + markdown )
        html += load.html('src/' + root + markdown)['html'] + '\n\n'

    saver.save(html, 'public/' + root + 'index.html')