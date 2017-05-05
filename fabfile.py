from fabric.api import local



def test3():


	local("cd /home/devops/python/fabric-scripts/fbtest3 && touch file1 file2 file3")


	local("cd /home/devops/python/fabric-scripts/fbtest3 && git add . && git commit -m test")


	local("cd /home/devops/python/fabric-scripts/fbtest3 && git push origin master")
