import requests
from common import BASE_GITHUB_API_URL
from requests.auth import HTTPBasicAuth


def get_github(repo, endpoint, username, token):
    """
    Attempt to request the endpoint from github.
    :param repo user/repo repository
    :param endpoint the github API endpoint
    """

    response = requests.get(
            BASE_GITHUB_API_URL + '/repos/' + repo + endpoint,
            auth=HTTPBasicAuth(username, token)
    )

    if response.status_code >= 400:
        raise Exception('Unable to read from GitHub, status={}'.format(response.status_code))

    return response.json()
