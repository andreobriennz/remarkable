from core.lib import load
from core.lib import save
from core.lib import get_html
from core.lib import create
from core.lib import Layout

import os
import json


with open('projects/projects.json') as f:
    data = json.load(f)


def compile(project_name):
    project_details = data['projects'][project_name]

    name = project_details['name']
    root = 'projects/'+name+'/'
    markdown_paths = project_details['sections']

    create.ensurePathsExist(['public/'+name, 'public/'+name+'/content/'])

    main = get_html(markdown_paths, root)

    layout = Layout.Layout(
        project_details,
        main,
        [
            ['style', 'assets/custom.css'],
            ['nav', 'partials/nav', 'nav id="nav" class="nav"'],
            ['footer', 'partials/footer']
        ]
    )
    layout.load_sections()
    page = layout.page()

    save.save(page, 'public/'+name+'/index.html')
    print('Compiled!')
