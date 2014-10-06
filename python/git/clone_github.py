from gittle import Gittle, GittleAuth

repo_path = '/tmp/gittle_test'
repo_url = 'https://github.com/fimafeng/fimafeng-protos.git'

auth = GittleAuth(username='[user github]',password='[pass github]')
# TODO : PB avec auth
#repo = Gittle.clone(repo_url, repo_path, auth=auth)
repo = Gittle.clone(repo_url, repo_path)
 



