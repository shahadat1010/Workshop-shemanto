
import todo_List

def main():
    FILENAME = 'list.txt'
    lineList = todo_List.getList(FILENAME)
    todo_List.deleteFromList(FILENAME, lineList)
    todo_List.showList(todo_List.getList(FILENAME))

if __name__ == "__main__":
    main()
