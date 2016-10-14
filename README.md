# git extensions

Place these on your `$PATH` somewhere and git will pick them up automagically.

#### Requirements

Place the following configurations in your gitconfig:

    [github]
       username = yourusername
       token = yourgithubapitoken

## [git-view-diffs](git-view-diffs/)

    usage: git-view-diffs [-h] [-v] repo [base] [head]
    
    git-view-diffs
    
    positional arguments:
      repo           user/repo
      base           base ref/tag, defaults to 'latest'
      head           head ref/tag, defaults to 'master'
    
    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  print full commit messages

# todo

* Ability to figure out current repository so the repo param is not necessary.
