from core.lib import load


def load_section(path, tag='div'):
    end_tag = tag.split()[0]

    if '.css' in path and Path(path).is_file():
        file = '\n<style>\n'+load.raw(path)+'\n</style>\n'
    elif Path(path+'.html').is_file():
        file = load.raw(path+'.html')
    elif Path(path+'.md').is_file():
        file = '\n<'+tag+'>\n'+load.html(path+'.md')+'\n</'+end_tag+'>\n'
    else:
        print('Path does not exist: '+path)
        file = ''

    return file


# def load_sections(root_path, sections):
#     for section in sections:
#         partials[section[0]] = load_section(root_path+section[1])