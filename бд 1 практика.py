class Que:
    def __init__(self, filename):
        self.students=[]
        self.filename=filename
    
    def add_student(self, id, name, course, grade):
        student={
            'id': id,
            'name': name,
            'course': course,
            'grade': grade
        }
        self.students.append(student)
        self.sort_by_id()
        self.save_to_file()  
    
    def get_by_id(self, st_id):
        for student in self.students:
            if student['id'] == st_id:
                return student.copy()
        return None
    
    def change_name(self, st_id, new_name):
        for student in self.students:
            if student['id']==st_id:
                student['name']=new_name
                self.save_to_file()  
                return True
        return False
    
    def change_course(self, st_id, new_course):
        for student in self.students:
            if student['id'] == st_id:
                student['course'] = new_course
                self.save_to_file()  
                return True
        return False
    
    def change_grade(self, st_id, new_grade):
        for student in self.students:
            if student['id']==st_id:
                student['grade']=new_grade
                self.save_to_file()  
                return True
        return False
    
    def delete(self, st_id):
        for i, student in enumerate(self.students):
            if student['id']==st_id:
                self.students.pop(i)
                self.save_to_file()  
                return True
        return False
    
    def print(self):
        for student in self.students:
            print(f"ID: {student['id']}, Name: {student['name']}, Course: {student['course']}, Grade: {student['grade']}\n")

    def sort_by_id(self):
        try:
            self.students.sort(key=lambda x: int(x['id']))
            print("Студенты отсортированы по ID!")
            return True
        except ValueError:
            print("ID должны быть числами для сортировки!")
            return False
        except Exception as e:
            print(f"Ошибка при сортировке: {e}")
            return False
    
    def save_to_file(self):  
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                for student in self.students:
                    file.write(f"{student['id']} {student['name']} {student['course']} {student['grade']}\n")
            print("Данные успешно сохранены!")
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")

def read_students_from_file(filename):
    students=Que(filename)  
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                data=line.strip().split()
                if len(data) >= 4:
                    students.add_student(data[0], data[1], data[2], data[3])
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
    return students

def create_new_database(filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("")
        print(f"✓ Новая база данных '{filename}' создана!")
        return Que(filename)  
    except Exception as e:
        print(f"✗ Ошибка при создании файла: {e}")
        return None

def main_menu():
    print("="*50)
    print("ВЫБОР КОЛЛЕКЦИИ ИЛИ СОЗДАНИЕ НОВОЙ")
    print("(Загрузка файла, создание нового)")
    print("="*50)
    print("1. Загрузить существующую базу данных")
    print("2. Создать новую базу данных")
    print("3. Выйти из программы")
    print("="*50)
    while True:
        choice=input("Выберите действие (1-3): ").strip()
        if choice=='1':
            filename=input("Введите имя файла для загрузки: ").strip()
            students=read_students_from_file(filename)
            if students:
                return students
            else:
                print("Попробуйте снова или создайте новую базу.")
        elif choice=='2':
            filename=input("Введите имя для новой базы данных: ").strip()
            students=create_new_database(filename)
            if students:
                return students
            else:
                print("Попробуйте другое имя файла.")
        elif choice == '3':
            print("Выход из программы...")
            return None
        else:
            print("Неверный выбор! Введите 1, 2 или 3.")

def management_menu(students):
    while True:
        print("\n" + "="*50)
        print("МЕНЮ УПРАВЛЕНИЯ БАЗОЙ ДАННЫХ")
        print("="*50)
        print("1. Показать всех студентов")
        print("2. Добавить студента")
        print("3. Изменить данные студента")
        print("4. Удалить студента")
        print("5. Сохранить данные")
        print("6. Вернуться в главное меню")
        print("7. Выйти из программы")
        print("="*50)
        choice = input("Выберите действие (1-7): ").strip()
        if choice == '1':
            students.print()
        elif choice == '2':
            print("\nДобавление нового студента:")
            id = input("ID: ").strip()
            name=input("Имя: ").strip()
            course=input("Курс: ").strip()
            grade=input("Оценка: ").strip()
            students.add_student(id, name, course, grade)
            print("Студент добавлен!")
        elif choice=='3':
            st_id=input("Введите ID студента для изменения: ").strip()
            student=students.get_by_id(st_id)
            if student:
                print("\nЧто хотите изменить?")
                print("1. Имя")
                print("2. Курс")
                print("3. Оценку")
                field = input("Выберите поле (1-3): ").strip()
                if field=='1':
                    new_name=input("Новое имя: ").strip()
                    students.change_name(st_id, new_name)
                elif field == '2':
                    new_course = input("Новый курс: ").strip()
                    students.change_course(st_id, new_course)
                elif field=='3':
                    new_grade=input("Новая оценка: ").strip()
                    students.change_grade(st_id, new_grade)
                else:
                    print("Неверный выбор!")
            else:
                print("Студент с таким ID не найден!")
        elif choice == '4':
            st_id = input("Введите ID студента для удаления: ").strip()
            if students.delete(st_id):
                print("Студент удален!")
            else:
                print("Студент с таким ID не найден!")
        elif choice == '5':
            students.save_to_file()
        elif choice == '6':
            print("Возврат в главное меню...")
            return True  
        elif choice == '7':
            print("Выход из программы...")
            return False 
        else:
            print("Неверный выбор!")

def main():
    print("СИСТЕМ А УПРАВЛЕНИЯ СТУДЕНТАМИ!")
    while True:
        students = main_menu()
        if students is None:
            break
        continue_program = management_menu(students)
        if not continue_program:
            break
if __name__ == "__main__":
    main()



    


    



    

