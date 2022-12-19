from git import Repo

with open('gitnames.txt', 'r') as url:
    data = url.readlines()

cond = ''
for git in data:
    gitstr = git.rstrip('\n')
    print('Копируем', gitstr)
    try:
        Repo.clone_from(gitstr, gitstr.split('/')[-1]+'-https')
    except:
        cond += f'{gitstr} - FAIL\n'
    else:
        cond += f'{gitstr} - OK\n'

with open('gitkvit.txt', 'w') as kvit:
    kvit.write(cond)