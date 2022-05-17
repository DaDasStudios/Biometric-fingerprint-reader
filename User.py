

class User:
    def __init__(self,
                 id: int,
                 code: int = 2420221234,
                 name: str = "Example name",
                 age: int = 18,
                 carrer: str = "Any",
                 semester: int = 1,
                 photo: str = "./images/default-img.png"):
        self.id = id
        self.name = name
        self.code = code
        self.age = age
        self.carrer = carrer
        self.semester = semester
        self.photo = photo

    def get_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "age": self.age,
            "carrer": self.carrer,
            "semester": self.semester,
            "photo": self.photo
        }
