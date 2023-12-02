# Git Flow
### Why do we need this
Variety of habits using Git could make the entire commit history of a project really messy.  
A working flow that everyone follows or does not break is recommended to exist.

### Branch Overview
It's based on 
https://gitbook.tw/chapters/gitflow/why-need-git-flow

- Remote Branches: `main`, `dev`
- Local Branches: `main`, `dev`, `hotfix`, `features`, `release`

### Details
[The concept](https://itknowledgeexchange.techtarget.com/coffee-…k/files/2021/01/gitflow-hotfix-branch-diagram.jpg)

#### want to publish `dev`
- [img](https://itknowledgeexchange.techtarget.com/coffee-talk/files/2021/01/gitflow-release-branch.jpg)
- switch to `dev`
- new a branch `release/<version>`, ex: release/1.2
- fix small bugs, commit... until stable
- merge into `main` and `dev`
- stick a version tag on `main`, ex: v1.2
- delete `release/<version>`

#### Urgent Bugs Appear on Stable Version
> `Hotfix`. Individual work at local. 

- switch to `main`
  - new a hotfix branch ex: hotfix/intensity_unit_error
- switch to `hotfix/<name>`
  - fix it and test it
- switch to `main`
  - merge `hotfix/<name>` with parameter `--no-ff `
  - format of commit message: `hotfix: <your description>`
  - push to remote
- switch to `dev`
  - merge `hotfix/<name>` with parameter `--no-ff `
  - format of commit message: `hotfix: <your description>`
  - push to remote
- delete local hotfix branch (optional)


#### Dev Branch is about to Publish
> `Release`. Individual work at local. 

- switch to `dev`
  - new a release branch ex: release/1.2
- switch to `release/<v. to release>`
  - fix it and test it
- switch to `main`
  - merge `release/<v. to release>` with parameter `--no-ff `
  - format of commit message: `release: <v. to release>`
  - push to remote
- switch to `dev`
  - merge `release/<v. to release>` with parameter `--no-ff `
  - format of commit message: `release: <v. to release>`
  - push to remote
- delete local release branch (optional)



- switch to `dev`
- new a branch `release/<version>`, ex: release/1.2
- fix small bugs, commit... until stable
- merge into `main` and `dev`
- stick a version tag on `main`, ex: v1.2
- delete `release/<version>`


#### Develop a Feature
> `Feature`. Individual work at local. 

- switch to `dev`
  - new a feature branch ex: feature/utils_auto_stretching
- switch to `feature/<name>`
  - fix it and test it
- switch to `dev`
  - merge `feature/<name>` with parameter `--no-ff `
  - format of commit message: `feature: <your description>`
  - push to remote
- delete local feature branch (optional)



### Reference
- https://gitbook.tw/chapters/gitflow/why-need-git-flow
- https://nvie.com/posts/a-successful-git-branching-model/
- https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/Gitflow-release-branch-process-start-finish