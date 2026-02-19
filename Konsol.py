import json
import os
FILE_NAME = "projects.json"
def load_data():
    if not os.path.exists(FILE_NAME):
        return {"projects": []}
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)
def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
def show_projects(data):
    if not data["projects"]:
        print("Проектов пока нет.")
        return
    for i, project in enumerate(data["projects"], start=1):
        print(f"{i}. {project['name']} | Статус: {project['status']}")
def create_project(data):
    name = input("Введите название проекта: ")
    project = {
        "name": name,
        "status": "планирование",
        "tasks": []
    }
    data["projects"].append(project)
    save_data(data)
    print("Проект создан.")
def add_task(data):
    show_projects(data)
    try:
        project_index = int(input("Выберите номер проекта: ")) - 1
        project = data["projects"][project_index]
    except (IndexError, ValueError):
        print("Неверный выбор.")
        return
    title = input("Введите название задачи: ")
    project["tasks"].append({
        "title": title,
        "done": False
    })
    save_data(data)
    print("Задача добавлена.")
def show_tasks(data):
    show_projects(data)
    try:
        project_index = int(input("Выберите номер проекта: ")) - 1
        project = data["projects"][project_index]
    except (IndexError, ValueError):
        print("Неверный выбор.")
        return
    if not project["tasks"]:
        print("Задач пока нет.")
        return
    print(f"\nЗадачи проекта '{project['name']}':")
    for i, task in enumerate(project["tasks"], start=1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. {task['title']} [{status}]")
def change_status(data):
    show_projects(data)
    try:
        project_index = int(input("Выберите номер проекта: ")) - 1
        project = data["projects"][project_index]
    except (IndexError, ValueError):
        print("Неверный выбор.")
        return
    print("Выберите новый статус:")
    print("1. Готов")
    print("2. В работе")
    print("3. Планирование")
    choice = input("Ваш выбор: ")
    statuses = {
        "1": "готов",
        "2": "в работе",
        "3": "планирование"
    }
    if choice in statuses:
        project["status"] = statuses[choice]
        save_data(data)
        print("Статус обновлён.")
    else:
        print("Неверный выбор.")
def main():
    while True:
        data = load_data()
        print("\n=== МЕНЮ ===")
        print("1. Показать проекты")
        print("2. Создать проект")
        print("3. Добавить задачу")
        print("4. Показать задачи проекта")
        print("5. Изменить статус проекта")
        print("0. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            show_projects(data)
        elif choice == "2":
            create_project(data)
        elif choice == "3":
            add_task(data)
        elif choice == "4":
            show_tasks(data)
        elif choice == "5":
            change_status(data)
        elif choice == "0":
            break
        else:
            print("Неверный ввод.")
if __name__ == "__main__":
    main()