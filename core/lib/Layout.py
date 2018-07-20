from core.lib.crud import load
from core.lib.crud import load_sections

import datetime


class Layout:
    def __init__(self, project_details, main, sections):
        self.name = project_details['name']
        self.root = 'projects/'+self.name+'/'
        self.main = main
        self.sections = sections
        self.partials = {}

    
    def load_sections(self):
        for section in self.sections:
            self.partials[section[0]] = load_sections.load_section(self.root+section[1])
    

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
