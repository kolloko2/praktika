import os

class Database:
    def __init__(self, filename="database.txt"):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        """Загружает данные из файла."""
        data = {}
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                for line in f:
                    try:
                        key, value = line.strip().split(":", 1) # Разбиваем по первому : для обработки значений с двоеточиями
                        data[key] = value
                    except ValueError:
                        print(f"Ошибка чтения строки: {line.strip()}") # Обработка некорректных строк
        return data

    def save_data(self):
        """Сохраняет данные в файл."""
        with open(self.filename, "w", encoding="utf-8") as f:
            for key, value in self.data.items():
                f.write(f"{key}:{value}\n")

    def view_record(self, key):
        """Просматривает запись по ключу."""
        if key in self.data:
            print(f"Ключ: {key}, Значение: {self.data[key]}")
        else:
            print("Запись не найдена.")

    def add_record(self, key, value):
        """Добавляет новую запись."""
        if key in self.data:
            print("Такой ключ уже существует. Используйте 'edit', чтобы изменить запись.")
        else:
            self.data[key] = value
            self.save_data()
            print("Запись добавлена.")

    def edit_record(self, key, new_value):
        """Редактирует существующую запись."""
        if key in self.data:
            self.data[key] = new_value
            self.save_data()
            print("Запись отредактирована.")
        else:
            print("Запись не найдена.")

    def delete_record(self, key):
        """Удаляет запись по ключу."""
        if key in self.data:
            del self.data[key]
            self.save_data()
            print("Запись удалена.")
        else:
            print("Запись не найдена.")

def main():
    db = Database()

    while True:
        print("\nФайловая база данных")
        print("1. Просмотр записи")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Удалить запись")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            key = input("Введите ключ записи для просмотра: ")
            db.view_record(key)
        elif choice == "2":
            key = input("Введите ключ новой записи: ")
            value = input("Введите значение новой записи: ")
            db.add_record(key, value)
        elif choice == "3":
            key = input("Введите ключ записи для редактирования: ")
            new_value = input("Введите новое значение: ")
            db.edit_record(key, new_value)
        elif choice == "4":
            key = input("Введите ключ записи для удаления: ")
            db.delete_record(key)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()