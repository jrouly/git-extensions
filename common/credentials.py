from subprocess import call, check_output, CalledProcessError

def get_credentials():
    """
    Pull github credentials from ~/.gitconfig.
    Expects: github.username
             github.token
    Will fail if both are not found.

    :return: (username, token)
    """

    try:
        username = check_output([
                'git',
                'config',
                '--get',
                'github.username'
            ]).decode('utf-8').strip()
    except CalledProcessError:
        raise Exception('github.username not set in gitconfig')

    try:
        token = check_output([
                'git',
                'config',
                '--get',
                'github.token'
            ]).decode('utf-8').strip()
    except CalledProcessError:
        raise Exception('github.token not set in gitconfig')

    return (username, token)
