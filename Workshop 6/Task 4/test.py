import getList

def main():
    FILENAME = 'list.txt'  
    lineList = getList.getList(FILENAME)  
    
  
    print("Content of the list from file:")
    for line in lineList:
        print(line.strip())  

if __name__ == "__main__":
    main()