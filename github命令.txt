Git Bash 命令
新建代码仓库
#在当前目录新建一个Git代码库
git init

#下载一个项目和它的整个代码历史
git clone [ url ]

#添加指定文件到暂存区
git add [ file1 ] [ file2 ]

#删除工作区文件，并且将这次删除放入暂存区
git rm [ file1 ] [ file2 ]

#改名文件，并且将这个改名放入暂存区
git mv [ file-origin ] [ file-renamed ]

#提交暂存区到仓库
git commit -m  [message]

#直接从工作区提交到仓库

#前提该文件已经有仓库中的历史版本
git commit -lsa -m [message]

#显示变更信息
git status

#显示当前分支的历史版本
git log
git log --oneline

同步远程仓库

#增加远程仓库，并命名
git remote add [ shortname ] [ url ]

#将本地的提交推送到远程仓库
git push [ remote ] [branch]

#将远程仓库的提交下拉到本地
git pull [ remote ] [ branch ] 

#将远程仓库克隆到本地
git clone [url]