import requests

api_url = "https://jsonplaceholder.typicode.com/todos"

def url(rest, id=1):
    url = {
        "get-all": api_url,
        "get-one": api_url + "/" + str(id),
        "post": api_url,
        "put": api_url + "/" + str(id),
        "patch": api_url + "/" + str(id),
        "delete": api_url + "/" + str(id)
    }
    return url[rest]

while True:
    choice = input("What do you want to do? (get-all, get-one, post, put, patch, delete, exit): ")

    if choice == "exit":
        break

    # Get all todos
    if choice == "get-all":
        response = requests.get(url(choice))
        if response.status_code == 200:
            print(response.text)
        else:
            print("Error: " + str(response.status_code))

    # Get a single todo
    if choice == "get-one":
        id = input("Enter id: ")
        response = requests.get(url(choice, id))
        if response.status_code == 200:
            print(response.text)
        else:
            print("Error: " + str(response.status_code))

    # Create a new todo
    if choice == "post":
        title = input("Enter title: ")
        completed = input("Enter completed: ")
        response = requests.post(url(choice), json={"title": title, "completed": completed})
        if response.status_code == 201:
            print(response.text)
        else:
            print("Error: " + str(response.status_code))

    # Update an existing todo
    if choice == "put":
        title = input("Enter title: ")
        completed = input("Enter completed: ")
        response = requests.put(url(choice), json={"title": title, "completed": completed})
        if response.status_code == 200:
            print(response.text)
        else:
            print("Error: " + str(response.status_code))

    # Update an existing todo
    if choice == "patch":
        title = input("Enter title: ")
        response = requests.patch(url(choice), json={"title": title})
        if response.status_code == 200:
            print(response.text)
        else:
            print("Error: " + str(response.status_code))

    # Delete an existing todo
    if choice == "delete":
        id = input("Enter id: ")
        response = requests.delete(url(choice, id))
        if response.status_code == 200:
            print(response.text)
        else:
            print("Error: " + str(response.status_code))

    print("====================================")