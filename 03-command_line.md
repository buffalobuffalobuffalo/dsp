# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > 
1. $ pwd : shows current working directory path
2. $ mkdir directoryname : makes a directory
3. $ rm -r directoryname	: deletes a directory
4. $ touch filename.filetype : creates a file
5. $ rm name.txt : deletes a file
6. $ mv filename.filetype newname.filetype : renames a file
7. $ ls -d .* - lists all hidden files
8. $ cp directory/filename.filetext newdirectory/ : copies a file from one directory to another
9. $ cd ~ : changes to root directory 
10. $ mv name.type directory/ : move file to directory

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
ls : list all files in directory
ls -a : list all files in directory, including hidden files
ls -l : list all files in directory, in long form
ls -lh : list all files in directory, in long form, with readable format
ls -lah : list all files in directory, including hidden files, in long form, in readable format
ls -t : list all files in directory, sorted by time and date
ls - Glp : list all files in directory, ?, in long format, with /
---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
1. -m : display the names as a comma separated list
2. -c : display files by timestamp
3. -R : display subdirectories as well
4. -u : display files by file access time
5. -d : display only directories

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > It applies a given command to a series of things in order.

Say you wanted to change the ownership of all the files in a directory from one group to another called "forcedxmpls"
you could write
$ ls | xargs -n 1 chgrp forcedxmpls

 

