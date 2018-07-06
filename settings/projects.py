tasks = []
def task(task):
    tasks.append( task )

thesis = {
    'type': 'writings',
    'theme': '',
    'title': '',
    'subtitle': '',
    'root_file': 'thesis/',
    'sections': [

    ]
}

book = {
    'type': 'book',
    'theme': '',
    'title': 'The Day of Pillows',
    'subtitle': '',
    'root_file': 'book/',
    'sections': [ # consider allowing an array of arrays to imply multiple parts (or alt have 'parts')
        'part_1/chapter_1.md',
        'part_1/chapter_2.md',
        'part_1/chapter_3.md',
    ]
}

# task( thesis )
task( book )

def run():
    return tasks