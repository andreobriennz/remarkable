import sys
import os
import markdown
import bleach

def html(path):
    file = open(path, 'r+')

    text = file.read()
    
    text = bleach.clean( text )

    html = markdown.markdown(text)
    html = bleach.linkify( html )

    file.close()

    post = {
        'html': html,
        'text': text,
    }

    return post
