#!/usr/bin/env python

import sys
import requests

from subprocess import call, check_output, CalledProcessError

# Generic error status code.
ERROR = 1

def get_credentials():
    '''
    Pull github credentials from ~/.gitconfig.
    Expects: github.username
             github.password
    Will fail if both are not found.
    '''
    try:
        username = check_output([
                'git',
                'config',
                '--get',
                'github.username'
            ]).decode('utf-8').strip()
    except CalledProcessError:
        raise Exception('github.username not set.')

    try:
        password = check_output([
                'git',
                'config',
                '--get',
                'github.password'
            ]).decode('utf-8').strip()
    except CalledProcessError:
        print('github.password not set.')
        raise Exception('github.password not set.')

    return (username, password)


def main():
    (username, password) = get_credentials()


if __name__ == '__main__':
    sys.exit(main())
