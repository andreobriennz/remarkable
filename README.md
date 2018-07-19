# remarkable 

## What Does this Project Do?
Remarkable turns a folder full of *markdown* files into a single *markup* file, complete with styling and partials such as a nav and footer. You can do this via a GUI (user interface) of manually by creating the files (if editing manually use the CLI to compile code). It can also handle multiple projects.

Note: Remarkable is currently under development. There will be bugs, and the project may change suddenly. It is also recommended to keep a backup of any important work as there is a very small chance of a bug causing a loss of content when working through the GUI.

Note: Remarkable assumes a basic knowledge of the terminal, HTML and markdown files in order to use it.

## How to Use
### 1. Create Project
First, make sure Python 3 is installed on your computer. If not, install it [here](https://www.python.org/downloads) or via homebrew
You will also need pip installed (`sudo easy_install pip`), as well as the markdown (`pip3 install markdown`) and bleach (`pip3 install bleach`) packages to safely handle markdown files.

Then choose one of the following methods:

**Via User Interface**
- `python3 manage.py start` to create the project via the new user interface!
- Follow on screen prompts to create a project

**Manually**
- Create a new project with `python3 manage.py create=name_of_project` and Remarkable will create a new project in the 'projects/' directory matching the name of your new project


### 2. Edit Project
**Via User Interface**
- Open the user interface with `python3 manage.py start`
- Select the project name from the menu
- If you wish to create a new file, type the file name and click create
- If you wish to edit a file, select it from the menu. Type the changes in the large text area and click 'Save changes'. The project will then automatically recompile.

**Manually**
Editing projects can easily be done manually by creating and editing markdown files in projects/name_of_project/content/

### 3. Compile to Website (automatic when working via user interface)
If not using the GUI:
- Compile changes with `python3 manage.py compile=name_of_project`
- Site will appear in public/name_of_project


### 4. Advanced: Creating Custom Sections and Layout
- You can edit existing sections in the 'partials/' directory to create a custom nav or footer. Both markdown and HTML files are supported
- Documentation for creating new, custom sections and editing layout coming soon (once a few bugs have been fixed)