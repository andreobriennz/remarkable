# remarkable 
**Python Site and Subsite Generator: Combine and compile markdown files into a website with automatically generated styling to suit**

Note: This project is currently under development. There will be bugs, and the project may change suddenly. It is also recommended to keep a backup of any important work as there is a small chance of a bug causing a loss of content when workign through the GUI.

Note: This project assumes a basic knowledge of the terminal, HTML and markdown files in order to use it.

## What Does this Project Do?
- Takes markdown files, convert them to HTML, concatenate these files together, along with page partials, and generates a website from this
- Automates and simplifies this process via a GUI and CLI to create and edit projects
- Lets you manage multiple sites/projects together in a modular way
- Generates sites as a single page app (coming soon)

## How to Use
### 1. Create Project
First, make sure Python 3 is installed on your computer. If not, install it [here](https://www.python.org/downloads)

Then choose one of the following methods:

**Via User Interface**
- `python manage.py open` or `python manage.py start` to create the project via the new user interface!
- Follow on screen prompts to create a project (note that editing project is not yet supported)

**Via CLI or manually**
- Create a new project with `python manage.py create=name_of_project`

**Manually**
- There will be a folder created in the 'projects/' directory matching the name of your new project. This is where all your project specific code and content is. Inside here, you will see a directory called 'content' - this is where you put all your content (blogs, book chapters, etc). Content in here should be all in markdown (files ending in .md)


### 2. Edit Project
For now editing project needs to be done by creating and editing markdown files in projects/name_of_project/content/. A user interface (GUI) is currently being developed.

### 3. Compile to Website
- Compile changes with `python manage.py compile=name_of_project`
- Site will appear in public/name_of_project


### 4. Advanced: Creating Custom Sections and Layout
- You can edit existing sections in the 'partials/' directory to create a custom nav or footer. Both markdown and HTML files are supported
- Documentation for creating new, custom sections and editing layout coming soon (once a few bugs have been fixed)