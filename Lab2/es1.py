'''
Created on Mar 23, 2015

@author: lorenzo
'''
import os 


def index(root):
    libreria = []
    for directory in os.walk(root, followlinks = True):
        for filename in directory[2]:
            if(filename.endswith(".mp3")):
                libreria.append(directory[0]+filename)
                print directory[0]+filename 
    return libreria
                
    
    
def search(tag_name, text):
    print tag_name, text

def display():
    print "Display"

def show(track_ID):
    print track_ID


def main():
    s = "init"
    while s != "exit":
        s = raw_input("Inserisci comando: ")
        l = s.split()
        if l[0] == "index":
            libreria = index(l[1])
        elif l[0] == "search":
            search(l[1], l[2], libreria)
        elif l[0] == "display":
            display(libreria)
        elif l[0] == "show":
            show(l[1], libreria)

            
if __name__ == '__main__':
    main()