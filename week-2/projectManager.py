import time

class TODO:
    # todos = [{
    #     'id':'',
    #     'desc':'',
    #     'is_completed':False
    # }]

    todos = []

    def add_todo(self, desc):

        todo = {
            "id": int(time.time()),
            "desc": desc,
            "is_completed": False
        }

        self.todos.append(todo)


    def remove_todo(self, id):

        for i in self.todos:
            if i["id"] == id:
                self.todos.remove(i)

    def display_todos(self):

        print(self.todos)


    def update_todo(self, id, new_desc):

        for i in self.todos:
            if i["id"] == id:
                i["desc"] = new_desc



    def toggle_mark_as_completed(self, id):

        for i in self.todos:
            if i["id"] == id:
                i["is_completed"] = True


    def completed_todos(self):

        
        for i in self.todos:
            if i["is_completed"]:
                print(f'--> {i['desc']}')


    def incompleted_todos(self):

        for i in self.todos:
            if i["is_completed"] == False:
                print(f'--> {i['desc']}')