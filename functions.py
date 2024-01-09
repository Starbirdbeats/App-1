def create_tasks(task, filepath="tasks.txt"):
    with open(filepath, "w") as file:
            file.writelines(task)


if __name__ == "__main__":
      ...