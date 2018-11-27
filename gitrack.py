import subprocess

# your specific user name
user = 'zack441'

# append paths to repos
repos = []

repos.append('/Users/corneria/Documents/Research/pbrttest')

filesChanged = 0
insertions = 0
deletions = 0

for repo in repos:
    command = "cd " + repo
    command = command + " && git log --shortstat --author "
    command = command + "\"" + user + "\" --since \"1 day ago\" | grep \"files changed\" | awk '{files+=$1; inserted+=$4; deleted+=$6} END {print \"files changed\", files, \"lines inserted:\", inserted, \"lines deleted:\", deleted}'"
    output = subprocess.check_output(command, shell=True)
    split = output.split(" ")
    filesChanged = filesChanged + int(split[2])
    insertions = insertions + int(split[5])
    deletions = deletions + int(split[8])

print 'Files Changed Since Yesterday:', filesChanged
print 'Total Insertions Accross All Projects:', insertions
print 'Total Deletions Accross All Projects:', deletions
