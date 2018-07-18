import os
import imp
import json
load = imp.load_source('loader', 'core/lib/loader.py')
saver = imp.load_source('saver', 'core/lib/saver.py')
Layout = imp.load_source('Layout', 'core/lib/Layout.py')


with open('projects/projects.json') as f:
    data = json.load(f)


def index(project_name):
    project_details = data['projects'][project_name]
    name = project_details['name']
    root = 'projects/'+name+'/'

    if not os.path.exists('public/'+name):
        os.makedirs('public/'+name)
        os.makedirs('public/'+name+'/content/')
    
    markdown_paths = project_details['sections']
    main = ''

    def get_html(markdown_paths):
        main = ''
        for markdown_path in markdown_paths:
            if '*' in markdown_path:
                markdown_path = markdown_path.split('*')[0]
                files = os.listdir(root+'content/'+markdown_path)
                files = sorted(files)

                markdown_paths = []
                for file in files:
                    markdown_paths.append(markdown_path+file[:-3])
                main += get_html(markdown_paths)
                    
            else:
                markup = load.html(root+'content/'+markdown_path+'.md')
                markdown_path = markdown_path.replace('/', '__')
                main += "<article id='{}'>\n{}\n</article>\n\n".format(markdown_path, markup)
                
                saver.save(markup, 'public/'+name+'/content/'+markdown_path+'.html')

        return main
    
    main += get_html(markdown_paths)

    layout = Layout.Layout(
        'projects/book/',
        main,
        [
            ['style', 'assets/custom.css'],
            ['nav', 'partials/nav', 'nav id="nav" class="nav"'],
            ['footer', 'partials/footer']
        ]
    )
    layout.load_sections()
    page = layout.page()

    saver.save(page, 'public/'+name+'/index.html')