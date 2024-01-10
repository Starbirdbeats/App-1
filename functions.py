FILEPATH = "tasks.txt"

def create_tasks(tasks, filepath=FILEPATH):
    with open(filepath, "w") as file:
            file.writelines(tasks)


def read_tasks(filepath=FILEPATH):
    with open(FILEPATH, "r") as file:
        tasks = file.readlines()
    return tasks


if __name__ == "__main__":
      ...