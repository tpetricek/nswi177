# Lab 15: Sample problems

The following problems let you practice a range of simple tasks from all categories of topics (shell, git, devel, admin, net) covered in the course. They are examples of what may appear in the test. Can you do those without Google?

## Problem #1: Create submission repository

- Create a git repository `demo` in your home directory on `linux.ms.mff.cuni.cz`
- You will use this to submit parts of your solution to branches in this repository.

## Problem #2: Report available memory

- Find out how much available memory there is on your current machine and on `linux.ms.mff.cuni.cz`
- Create a `meminfo.txt` file in `meminfo` branch in your Git repository with the two numbers (in KB):

      Local: 123456
      Remote: 123456
      
## Problem #3: Write a `gitinfo.sh` shell script 

- Write a shell script `gitinfo` that prints information about the last `git` commit in the current directory.
- It can be called with two parameters: `./gitinfo.sh title` and `./gitinfo.sh email`.
  * For `title`, print the title provided for the last commit
  * For `email`, print the email of the author of the last commit  
- If no parameter is specified, assume it is `title`, for any other parameter, report an error and fail.
- Add your script to `gitinfo` branch of your repository 

## Problem #4: Install and run `tldr` in Alpine

- Using podman, install the `tldr` tool in the latest distribution of Alpine available
- You will need to use the Alpine package manager to install packages `nodejs` and `npm` first
- Then use `npm install -g tldr` to install the `tldr` tool
- Get the `tldr` info for the `grep` command and put the **second** example given in the `grepinfo.txt` file in the `grepinfo` branch of your repository.
