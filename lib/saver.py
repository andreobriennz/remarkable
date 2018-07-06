import sys
import os
import markdown
# import bleach

def save(html, file):
    test_file = open(file, 'wb')

    test_file.write( bytes( html, 'utf-8' ) )

    test_file.close()


# # read/write file
# test_file = open('test-files/file1.md', 'wb')

# print( test_file.mode ) # 'wb'
# print( test_file.name ) 

# test_file.write( bytes("# Added to the file").encode("utf-8") )

# test_file.close()

# print( test_file.mode ) # 'wb'


# test_file = open('test-files/file1.md', 'r+') # read/write
# text = test_file.read()
# print(text)

# # os.remove('test-files/file1.md') # delete file

# html = markdown.markdown(text)
# print(html)