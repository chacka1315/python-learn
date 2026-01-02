def createEntrepreneur(name):
    # name = name

    def greet():
        print("Hello ", name)

    def work():
        print(name, " only create value and innovative compagnies.")

    def describe():
        print(
            "As ",
            name,
            " is an entrepreneur, he is a free person lika a pirates and love news adventures and make money and more...",
        )

    return {"greet": greet, "work": work, "describe": describe}


siaka = createEntrepreneur("Siaka")

if __name__ == "__main__":
    siaka.get("greet")()
    siaka["describe"]()
    siaka.get("work")()
