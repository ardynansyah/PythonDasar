class person:
    def _init_(self, name, age):
        self.name = name 
        self.age = age
p1 = person("john", 36)
print(p1.name)
print(p1.age)