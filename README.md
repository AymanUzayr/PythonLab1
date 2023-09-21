# PythonLab1
# Git Basics: Pull Requests and Pushes

This guide will help you understand the basic Git commands for creating and managing pull requests and pushing your changes to a remote repository.

## Forking a Repository

1. Go to the repository you want to contribute to.
2. Click the "Fork" button in the upper right corner to create a copy of the repository in your own GitHub account.

## Cloning a Repository
To work on a local copy of the forked repository:

> git clone <repository-url>
> cd <repository-directory>

Creating a Branch
Create a new branch for your changes:
> git checkout -b <branch-name>

Committing Changes
Commit your changes with a descriptive message:
> git add .
> git commit -m "Description of changes"

Pushing Changes
Push your branch to your forked repository on GitHub:
> git push origin <branch-name>

Creating a Pull Request
Go to your forked repository on GitHub.
Click on the "Pull Requests" tab.
Click the "New Pull Request" button.
Select the base repository and branch you want to merge your changes into.
Provide a descriptive title and comment explaining your changes.
Click "Create Pull Request."
Reviewing and Merging Pull Requests
Collaborators or project maintainers can review your pull request. Once approved:

Click the "Merge Pull Request" button.
Confirm the merge.
Your changes are now part of the base repository.





