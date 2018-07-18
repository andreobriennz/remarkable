import markdown
import bleach


def html(path):
    file = open(path, 'r+')

    text = file.read()
    
    text = bleach.clean(text)

    html = markdown.markdown(text)
    html = bleach.linkify(html)

    file.close()

    return html


def raw(path):
    file = open(path, 'r+')

    html = file.read()

    file.close()

    return html