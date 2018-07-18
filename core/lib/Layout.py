from core.lib import loader as load

from pathlib import Path
import datetime


class Layout:
    def __init__(self, project_details, main, sections):
        self.name = project_details['name']
        self.root = 'projects/'+self.name+'/'
        self.main = main
        self.sections = sections
        self.partials = {}

    def load_section(self, path, tag='div'):
        end_tag = tag.split()[0]

        if '.css' in path and Path(path).is_file():
            file = '\n<style>\n'+load.raw(path)+'\n</style>\n'
        elif Path(path+'.html').is_file():
            file = load.raw(path+'.html')
        elif Path(path+'.md').is_file():
            file = '\n<'+tag+'>\n'+load.html(path+'.md')+'\n</'+end_tag+'>\n'
        else:
            print('path does not exist:'+path)
            file = ''

        return file
    
    def load_sections(self):
        for section in self.sections:
            self.partials[section[0]] = self.load_section(self.root+section[1])
    
    def page(self):
        return load.raw('projects/'+self.name+'/layouts/index.html').format(
            title=self.name.title(),
            name=self.name,
            style=self.partials['style'],
            nav=self.partials['nav'],
            main=self.main,
            footer=self.partials['footer'].format(year=datetime.date.today().year),
            script=self.name,
        )
