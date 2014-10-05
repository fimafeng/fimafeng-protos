from github3 import login

gh = login('[login_github]',password='[pass_github]')

mon_user = gh.user()

print (mon_user.name)
