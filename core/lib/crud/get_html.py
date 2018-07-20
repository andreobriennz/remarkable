from core.lib.crud import load
from core.lib.crud import save

import os

def get(markdown_paths, root_path, name):
    main = ''
    
    for markdown_path in markdown_paths:
        if '*' in markdown_path:
            markdown_path = markdown_path.split('*')[0]
            files = os.listdir(root_path+'content/'+markdown_path)
            files = sorted(files)

            markdown_paths = []
            for file in files:
                markdown_paths.append(markdown_path+file[:-3])
            main += get(markdown_paths, root_path, name)
                
        else:
            markup = load.html(root_path+'content/'+markdown_path+'.md')
            markdown_path = markdown_path.replace('/', '__')
            main += "<article id='{}'>\n{}\n</article>\n\n".format(markdown_path, markup)
            
            save.save(markup, 'public/'+name+'/content/'+markdown_path+'.html')

    return main