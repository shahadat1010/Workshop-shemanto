import todo_List

def main():
    FILENAME = 'list.txt'
    lineList = todo_List.getList(FILENAME)
    todo_List.showList(lineList)

if __name__ == "__main__":
    main()
