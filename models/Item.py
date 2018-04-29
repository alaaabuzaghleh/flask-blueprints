class Item:
    id = ""
    title = ""
    desc = ""

    def __init__(self, id, title, desc):
        self.id = id
        self.title = title
        self.desc = desc

    def toJson(self):
        in_json = {"id":self.id, "title":self.title, "desc":self.desc}
        return in_json

    def toJson2(self):
        return self.__dict__

toDoList = []

item1 = Item(id="1", title="Learn Flask", desc="Start Learning Flask")
item2 = Item(id="2", title="Learn Spring", desc="Start Learning Spring Framework")

toDoList.append(item1.toJson())
toDoList.append(item2.toJson2())
