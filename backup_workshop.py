import os

# Generate lab commands
commands = []
file = open("raw.txt", "r")
for line in file:
    if "[student@workstation ~]$ lab" in line and "start" in line:
        commands.append(line.split('$')[1][1:-1])
print(commands)
# for each lab create repo
for c in commands:
    print(c)
    repo_name = "OCP_" + c.split(" ")[1]
    github_creation = "curl -F 'login=paulaborde' -F 'token=418f9cf634f53b49417acfa9ed220cace7a771f7' https://github.com/api/v2/yaml/repos/create -F name=%s" % repo_name
    os.system(github_creation)
    os.system("cd DO380")
    os.system("git add *")
    os.system("git commit -am 'init data in repo'")
    os.system("git remote add origin https://github.com/paulaborde/%s.git" % repo_name)
    os.system("git push")
    os.system("cd ")
    os.system(c.replace('start', 'finish'))
