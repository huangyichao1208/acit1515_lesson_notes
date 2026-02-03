"""
Terminology

Terminal - GUI application (Terminal/Powershell)

Shell - program that runs inside the terminal
    the shell allows you to interact with your o/s / filesystem
    text-only

    the shell (bash on windows, zsh windows) has a prompt

Powershell (windows) prompt
    PS C:\Users\punks>

Mac prompt
    user@usersmacbook~: 

Linux
    student@bobacafe:~$ 

    user@machine PATH
                  ~ (alias for your home folder)

    A path is the hierarchy of folders that leads to a particular location

    student@bobacafe:~$
    student@bobacafe:/home/user$

    The 'root' folder is the folder that contains all other folders in your filesystem
            / means root

            start at the root, go inside the home folder, then go inside the user folder inside of home
            /home/user

URLs are similar
https://www.bcit.ca/study/computing-it/

https://www.bcit.ca/        root (home)
https://www.bcit.ca/study/  folder called study inside the root
https://www.bcit.ca/study/computing-it/   folder called computing-it inside the study folder

Linux commands (you can only run these when you see a linux/mac prompt, not windows)

    NOTE: the arrows will move/back and forth in your command history, so you don't have to retype commands that you use often

    NOTE: tab key will autocomplete file/folder names

    pwd (+enter)    present working directory (tells you where you are in the filesystem)

    clear (+enter)  clears the terminal

    Commands with (optional) 'arguments

    ls (+enter)     list all files/folders at my current location

        ls ./assignment2   list everything inside the assignment2 folder that is inside the current folder

        ls /var/www/html

        ls ../      list everything in the parent directory

        ls ../../   list everything two folders up

        ls /        list everything in the root folder  

    cd      change directory (directory = folder)

        cd (+enter)     go to your home folder

        cd -            goes to the last visited folder

        cd ./assignment2   go inside the assignment2 folder in the current folder

        cd /var/www/html

        cd ~

        cd /home/students/Documents/1515
        cd ~/Documents/1515

    mkdir   make directory (required argument - the folder name)

        mkdir ./setB     make a folder called setB in the current folder

        mkdir /var/www/acit1515

    mv      moves and/or renames

        mv test.txt testing.txt    rename a file in the current directory called test.txt to testing.txt

        mv test.txt ../test.txt     move the file up one directory

        mv test.txt ../testing.txt  move the file up one directory and rename

    rmdir   remove (empty) directory

        rmdir ./setB        remove the setB folder if empty

    rm      remove files/directory (including non-empty directories)

        rm test.txt         remove a file called test.txt


        rm -rf ./setB       removes a non-empty directory called setB

                rm is the command
                -rf are 'flags' (commands can be modified using these - or -- options)

IMPORTANT NOTE: rm is permanent/unrecoverable

        *******************
        DON'T EVER DO THIS
        *******************
        rm -rf /     DELETES YOUR ENTIRE FILESYSTEM

    touch   create a file

        touch ./test.txt

    cat     outputs the contents of a file

        cat ./test.txt


./      start at the current folder
./setB  a folder called setB inside the current folder

/       root

../     go up one folder
../../  go up two folders
../../../ etc.

    linux command that runs the Python interpreter
    (the interpreter is the program that runs your Python scripts)

    python          
    python3
    py

    e.g. running a script (python code inside of a file with a .py extension)

    python3 script.py       run the script.py file if it exists

    NOTE:
    if you type
        python3 (and hit enter with no filename/arguments) it will open the REPL (read-evaluate-print-loop)

        The REPL is an interactive python environment

Python (REPL) prompt
>>>

If you are inside the REPL (i.e. you see the >>> prompt) you can only write Python (no linux commands)

99% of the time you DO NOT WANT to be in the REPL

If you see the >>> prompt, type
    exit() (+enter)
    or
    quit()
to get back to the linux prompt
"""

"""
For assignment 1 - click the invite link under Content > Week 3
    click through authorizing Github Classroom
    Accept assignment
        - if error, check email and click invitation link
"""

"""
Set up git and SSH (so that we can download/upload assignments)

SSH is a secure way to authenticate when connecting to Github (or many other servers/services)

    SSH is a pair of 'keys' - the keys are encrypted files that match one another

        public key          the copy that you give github
        private key         stays on your machine, privately

STEP 1:
To create an ssh key, run the following command:

ssh-keygen -t ed25519 -C "emailaddress" -f ~/.ssh/acit1515

    NOTE: skip (enter through) the passphrase (twice)

    on success, you'll see a random art image

The above command creates two files:
    ~/.ssh/acit1515         the private key
    ~/.ssh/acit1515.pub     the public key

STEP 2: giving github the public key

First, run this command to output the contents of the public key in the terminal

    cat ~/.ssh/acit1515.pub

Next, go to github.com in the browser
    sign in
    enter this URL: https://github.com/settings/profile
    click the 'SSH and GPG keys' link the left-hand menu
    click New SSH key button top right-hand
    choose a title (anything you want)

    go back to the terminal, select the contents of the public key and copy (ctrl-c)
    go back to the browser, ctrl-v to paste in the 'key' textbox

    click Add SSH key

STEP 3:
    downloading and uploading code to/from git

    Git is 'version-control' software - it allows to save (backups) different versions of all the files in a folder over time

        e.g. workflow
        Week 1      week 2       week 3
        start ---- add page ---- more pages/styles ---
         |            |                 |
         create a git repository        |
                      |                 |
                make a 'commit'         |
                (a commit is a snapshot of how files look at a moment in time)                   |
                                        |
                                    create another commit

    Commits form a history of the project
    And we can move back/forth in time between different versions of the files/folders

Downloading code from github is called 'cloning'
Uploading code to github is called 'pushing'

cd ~
OR
cd ~/Documents
OR
cd ~/Documents/1515

git clone git@github.com:CIT-BCIT/___your personal link___

e.g.
git clone git@github.com:CIT-BCIT/b1-yourgithubusername assignment1

if you need your assignment link, click the invite link on the learning hub again

If you see any error messages related to permissions to read the remote repository, run these two commands

    eval $(ssh-agent -s)
    ssh-add ~/.ssh/acit1515

and re-run git clone command again

After successfully cloning, 
    in Windows

    code <folder_name>
    code assignment1
    code b1-yourusername

Git commands:

    git status - tells you the status of the repo
        e.g.
            modified: src/assignment1.py

ONE-TIME CONFIGURATION

git config --global user.name "Chris Harris"
git config --global user.email "chris_harris@bcit.ca"

Three-step process for committing and uploading to git (after clone) INSIDE THE ASSIGNMENT FOLDER

    git add --all                       tells git that you have changes
                                        to include in a new commit

    git commit -m "Done"               creates the commit (i.e. snapshot)

    git push

"""