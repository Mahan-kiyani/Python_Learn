# Git Learn Commands 

1- git init

2- git status

3- Git add to stage
    
    [path] git add 'file name' \#{selected file to stage}
    [path] git add . \#{all file to stage}

4-Git removed stage
    
    [path] git rm --cached 'file name'
    
5-Git send to repo
    
    [path] git commit -m 'your_message'
    git push origin main
    
6-Git Log

    git log
    git log --oneline
    git log --stat
    git log --graph
    git log --graph --oneline
    git log --after='year-month-day'
    git log --before='year-month-day'
    git log --authorr='UserName'
    
7-Git Add and Commit both

    git commit -am "file name"

8- Git Show 

    git show \# last changes in project
    git show 'commit_ID'
    
9-Git shortcut create

    git config --local alias.lgo "log --oneline"
    git config --global alias.am "commit -am"
    
    git config --local --get-regexp ^alias\. \#see alias was created in local
    git config --global --get-regexp ^alias\. \#see alias was created in global

-------------------------------------------------------------------------------------------------------------------------------------------------------

10-Git Branch

    git branch \# show branchs on your project
    git branch branch_name  \# create a branch
    git switch branch_name \# go to the branch you wish
    gir switch -c branch_name \# create and go to the branch 
    
11-Git remove a branch
    
    git branch -d branch name \# if you on that task you cant delete it, you must be switch
    git branch -D branch name \# if you’ve committed or added changes but haven’t merged them into the branch, you need to use -D to delete it.
    
    
12-Git rename branch

    git branch -m new_branch_name \# First, switch to the branch you want, then run this command.
    
13- install gitlens on VsCode and see branch graph on thay

14-Git Merge 
    
    git merge name_of_branch \# First, switch to the branch you want, then run this command. {fast forward}
    git merge name_of_branch name_commit \# First, switch to the branch you want, then run this command. {non-fast forward}


15-Commit Message Semantic
    
    feat: add hat wobble
    ^--^  ^------------^
    |     |
    |     +-> Summary in present tense.
    |
    +-------> Type: chore, docs, feat, fix, refactor, style, or test.
    
    More Examples:

    feat: (new feature for the user, not a new feature for build script)
    fix: (bug fix for the user, not a fix to a build script)
    docs: (changes to the documentation)
    style: (formatting, missing semi colons, etc; no production code change)
    refactor: (refactoring production code, eg. renaming a variable)
    test: (adding missing tests, refactoring tests; no production code change)
    chore: (updating grunt tasks etc; no production code change)

16-Git Comparison

    git diff \# comparison work directory with staging area
    git diff --staged \# comparison stage area with last commits
    git diff {HEAD or head} \# comparison work directory with last commits
    
17-
