# git extensions

Place these on your `$PATH` somewhere and git will pick them up automagically.

#### Requirements

Place the following configurations in your gitconfig:

    [github]
       username = yourusername
       token = yourgithubapitoken

## git-view-diffs

    usage: git-view-diffs [-h] [-v] repo [base] [head]
    
    git-view-diffs
    
    positional arguments:
      repo           user/repo
      base           base ref/tag, defaults to 'latest'
      head           head ref/tag, defaults to 'master'
    
    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  print full commit messages


### examples

These examples assume your repo is `org/repo` and the latest tag is `v1.0.0`.

#### viewing commits since the latest tag

    $ git view-diffs org/repo
    https://github.com/org/repo/compare/v1.0.0...master

    $ git view-diffs org/repo latest
    https://github.com/org/repo/compare/v1.0.0...master

#### viewing commits between specific tags

    $ git view-diffs org/repo latest
    https://github.com/org/repo/compare/v1.0.0...master

    $ git view-diffs org/repo v0.5.0
    https://github.com/org/repo/compare/v0.5.0...master

    $ git view-diffs org/repo v0.5.0 v0.9.0
    https://github.com/org/repo/compare/v0.5.0...v0.9.0

#### viewing commit messages

    $ git view-diffs -v org/repo v0.9.0
    [2016-10-13] @user1
    commit 1

    [2016-10-13] @user2
    commit 2

    https://github.com/org/repo/compare/v0.5.0...v0.9.0
