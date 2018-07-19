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
First, make sure Python 3 is installed on your computer. If not, install it [here](https://www.python.org/downloads) or via homebrew
You will also need pip installed (`sudo easy_install pip`), as well as the markdown (`pip3 install markdown`) and bleach (`pip3 install bleach`) packages to safely handle markdown files.

Then choose one of the following methods:

**Via User Interface**
- `3 manage.py open` or `python3 manage.py start` to create the project via the new user interface!
- Follow on screen prompts to create a project (note that editing project is not yet supported)

**Via CLI or manually**
- Create a new project with `python3 manage.py create=name_of_project`


- There will be a folder created in the 'projects/' directory matching the name of your new project. This is where all your project specific code and content is. Inside here, you will see a directory called 'content' - this is where you put all your content (blogs, book chapters, etc). Content in here should be all in markdown (files ending in .md)


### 2. Edit Project
**Via User Interface**
- Open the user interface with `python3 manage.py start`
- Select the project name from the menu
- If you wish to create a new file, type the file name and click create
- If you wish to edit a file, select it from the menu. Type the changes in the large text area and click 'Save changes'. The project will then automatically recompile.

**Manually**
Editing projects can easily be done manually by creating and editing markdown files in projects/name_of_project/content/

### 3. Compile to Website
- Compile changes with `python3 manage.py compile=name_of_project`
- Site will appear in public/name_of_project


### 4. Advanced: Creating Custom Sections and Layout
- You can edit existing sections in the 'partials/' directory to create a custom nav or footer. Both markdown and HTML files are supported
- Documentation for creating new, custom sections and editing layout coming soon (once a few bugs have been fixed)