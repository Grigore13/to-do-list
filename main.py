tasks = []
def add_task():
    task = input('Write your task for today:')
    tasks.append(task)
    print('Done ✅')


def delete_task():
    if len(tasks) == 0:
        print('Nothing to do 😴')

    list_tasks() #Show the list

    n = input('Write the number: ')

    if n.isdigit():
        n = int(n)
        if 1 <= n <= len(tasks):
            remove_task = tasks.pop(n -1)
            print(f'Task {remove_task} deleted 💥')
        else:
            print('NOT FOUND ❌')
    else:
        print('Write a corect number!!! 🔴 ')


def list_tasks():
    if len(tasks) >=1:
        print('Here are your tasks: ')
        for i, task in enumerate(tasks, start = 1):
            print(f'{i}. {task}')
    else:
        print('Relax, your list is clean 😁')


def close_list():
    print('BYE 👋🏻')

while True:
    if __name__ == "__main__":

        print('Hey 👋, here is the to do list app 📔')
        print('Choose one of the options to continue!😀')
        print('⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯')
        options = ['1.Add a new task', '2.Delete a task', '3.List tasks', '4.Close']
        print(*options, sep='\n')

        choice = input('Enter your choice:')
        if choice == '1':
            add_task()

        elif choice == '2':
            delete_task()

        elif choice == '3':
            list_tasks()

        elif choice == '4':
            close_list()
            break

        else:
            print('Please, enter the number 1-4')






