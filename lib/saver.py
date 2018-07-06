import sys
import os
import markdown

def save(html, file):
    test_file = open(file, 'wb')

    test_file.write( bytes( html, 'utf-8' ) )

    test_file.close()
