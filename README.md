# APMA-Covid-Research 

## How to Download
* Run `git clone https://github.com/jackliu612/APMA-Covid-Research.git` This will download the repository and create a new directory with all of the files
* After you have cloned, you can use `git pull` to download and merge any future changes instead of cloning again. More on this below. 

## How to make changes
1. Save any local changes that you have made and want to push 
2. Run the following commands in the terminal after locating to the base directory (APMA-Covid-Research)
	1. `git pull` This pulls any new changes from the repository and merges them with your local copy. 
	2. `git add .` This will tell git to add all local changes to a list in preparation for pushing to the repository. Alternatively, if you only want to add some specific files you can use `git add *filename here*` instead. 
	3. `git commit -m "*message here*"` (including quotes) This commits any changes that you added in step 1 along with a message describing the changes. Since this is not a huge project, the message doesn't really matter but it does need to be there.
	4. `git push` This takes your committed changes and pushes them to the repository so other contributors can see them with a `git pull`

If at any point you are not sure what is added/commited/etc. you can use `git status` to see the status of all local changes. 

