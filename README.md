# bedoff.Api
A RESTful service serving the entire backend

#### Important Git information

Before you start committing code, please install our pre-commit hook for Git, which will check for code quality issues
(as per PEP8 conventions) and imports sorted incorrectly.

The file `pre-commit-hook.sh` is the hook script. To install this in your local repository, you need to symlink the script
in your ``.git/hooks`` folder.

The following commands will create the link.

```
$ sudo chmod +x pre-commit-hook.sh
$ cd .git/hooks/
$ ln -s ../../pre-commit-hook.sh pre-commit
$ cd ../..
```

For kickstarting the project, follow DOCKER-README.md