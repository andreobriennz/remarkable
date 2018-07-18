import imp
Layout = imp.load_source('Layout', 'core/lib/Layout.py')


custom_layout = False


class CustomLayout(Layout):
    def __init__(self):
        super()
