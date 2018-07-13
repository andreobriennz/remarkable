# remarkable 
**Python Site and Subsite Generator: Combine and compile markdown files into a website with automatically generated styling to suit**

Note: This project is currently under development. There will be bugs, and the project may change suddenly.

Note: This project assumes a basic knowledge of the terminal, HTML and markdown files in order to use it.

# What Can this Project Do?
- Create a new project via the terminal
- Take markdown files, convert them to HTML, concatenate these files together
- Template this HTML in a layout file
- Automatically partials and styling into the layout
- Manage multiple sites/projects
- Generate sites as a single page app (coming soon)

# How to Use
## Basic Usage
- Make sure Python 3 is installed on your computer. If not, install it [here](https://www.python.org/downloads)
- Create a new project with `python -c "import manage; manage.create('name_of_project')"`
- There will be a folder created in the 'projects/' directory matching the name of your new project. This is where all your project specific code and content is. Inside here, you will see a directory called 'content' - this is where you put all your content (blogs, book chapters, etc). Content in here should be all in markdown (files ending in .md)
- For remarkable to recognize your content files and know what order to include them in, you must declare them. In the 'projects/projects.json' file, find the name of your project (automatically added) and add all your content filenames to the array called 'content' in the order they should appear (you don't need to add the full path, as remarkable will assume everything is in the content/ directory)
- Compile changes with `python -c "import manage; manage.index()"` or `runp manage.py run`

## Creating Custom Sections and Layout
- You can edit existing sections in the 'partials/' directory to create a custom nav or footer. Both markdown and HTML files are supported
- Documentation for creating new, custom sections and editing layout coming soon (once a few bugs have been fixed)