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
    lab_name = "OCP_" + c.split(" ")[1]
    os.system(c)
    os.system("cd ~/DO380")
    os.system("zip -r %s *" % lab_name)
    os.system("mv %s ~" % lab_name)
    os.system("cd ")
    os.system(c.replace('start', 'finish'))
