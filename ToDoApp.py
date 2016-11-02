




class ToDo():
    def __init__(self):
        self.todo = open("todo.txt", "r") 
        self.todo_mark = open("todo_mark.txt", "r") 
        self.todo_list = []
        self.todo_mark_list = []

        for line in self.todo: 
            self.todo_list.append(line.strip())

        for line in self.todo_mark:
            self.todo_mark_list.append(line.strip())
        
    def list(self):
        k = 0
        i = 1
        print("You saved the following to-do items:\n")
        for j in self.todo_list:
            print(str(i) + ". [" + str(self.todo_mark_list[k]) + "] " + str(j))
            k = k + 1
            i = i + 1

    def add(self):
        new = input("Add an item: ")
        self.todo_list.append(new)
        self.todo_mark_list.append("")
        print("Item Added.")

    def mark(self):
        c = int(input("Which one you want to mark as completed: "))
        n = 0        
        for line in self.todo_list:
            n = n + 1
            if n == c:
                self.todo_mark_list[n - 1] = "x"
                print(self.todo_list[n - 1] + " is completed.")


    def archive(self):
        d = 0
        while d < len((self.todo_mark_list)):
	        if self.todo_mark_list[d] == "x":
		        del(self.todo_mark_list[d])
		        del(self.todo_list[d])
	        else:
		        d = d + 1
        print("All completed tasks got deleted.")
  

start1 = ToDo()

while True:
    ask = input("Please specify a command [list, add, mark, archive] or type 'exit' to save & quit: ")
    if ask == "list":
        start1.list()
    
    elif ask == "add":
        start1.add()
    
    elif ask == "mark":
        start1.mark()
    
    elif ask == "archive": 
        start1.archive()
    
    elif ask == "exit":
        todo = open("todo.txt", "w")
        todo_mark = open("todo_mark.txt", "w") 
        
        for line in start1.todo_list:
            todo.write(line + "\n")
        for line in start1.todo_mark_list: 
            todo_mark.write(line + "\n")
        
        todo.close
        todo_mark.close
        
        break




    