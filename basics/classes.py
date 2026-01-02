class Vehicle:
    def __init__(self, make, model):
        self.model = model
        self.make = make
        self.engine = self.Engine()

    class Engine:
        def __init__(self):
            self.status = "Off"

        def start(self):
            self.status = "Running"
            print("Engine started")

        def stop(self):
            self.status = "Off"
            print("Engine stopped")

    def __str__(self):
        return f"{self.make} {self.model}\n"

    def moves(self):
        print(f"Vrooom, {self.make} {self.model} is running...")

    def get_name(self):
        print(f"I'm a {self.make} {self.model}!\n")


lambo = Vehicle("Lamborghini", "Revuelto")
lambo.moves()
lambo.get_name()

print("************")
Vehicle.moves(lambo)
print("************")
rolls = Vehicle("Rolls Royce", "Down")
rolls.moves()
rolls.get_name()


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print(f"{self.make} {self.model} is flying...")


class Train(Vehicle):
    def moves(self):
        print(f"{self.make} {self.model} is going...")


class Truck(Vehicle):
    pass


plane = Airplane("Jet", "Model 3", "AIR-2665")
plane.moves()
plane.get_name()
print(plane.faa_id)

train = Train("Train", "z33")
train.moves()
train.get_name()

truck = Truck("Optimus", "Prime")
truck.moves()
truck.get_name()

print("\n\n************")
for v in (lambo, plane, train, truck, rolls):
    print(v)
    v.get_name()
    v.moves()
    v.engine.start()
    print("\n")
