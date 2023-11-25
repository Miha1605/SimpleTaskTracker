import json

# Инициализация пустого списка задач
tasks = []

# Функция для добавления задачи
def add_task():
    title = input("Введите название задачи: ")
    description = input("Введите описание задачи: ")
    task_id = len(tasks) + 1  # Генерация уникального идентификатора
    task = {"id": task_id, "title": title, "description": description, "status": "не выполнена"}
    tasks.append(task)
    save_data()
    print(f"Задача {task_id} добавлена!")

# Функция для просмотра задач
def list_tasks():
    for task in tasks:
        print(f"ID: {task['id']}, Название: {task['title']}, Описание: {task['description']}, Статус: {task['status']}")

# Функция для удаления задачи
def delete_task():
    task_id = int(input("Введите ID задачи для удаления: "))
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_data()
            print(f"Задача {task_id} удалена!")
            break
    else:
        print(f"Задача с ID {task_id} не найдена.")

# Функция для обновления статуса задачи
def update_status():
    task_id = int(input("Введите ID задачи для обновления статуса: "))
    new_status = input("Введите новый статус (выполнена/не выполнена): ")
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = new_status
            save_data()
            print(f"Статус задачи {task_id} обновлен!")
            break
    else:
        print(f"Задача с ID {task_id} не найдена.")

# Функция для сохранения данных в файл
def save_data():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

# Загрузка данных из файла (если он существует)
try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    pass

# Основной цикл программы
while True:
    print("\nВыберите действие:")
    print("1. Добавить задачу")
    print("2. Просмотреть задачи")
    print("3. Удалить задачу")
    print("4. Обновить статус задачи")
    print("5. Выход")
    choice = input("Введите номер действия: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        update_status()
    elif choice == '5':
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")