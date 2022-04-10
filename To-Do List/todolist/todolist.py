from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Date, create_engine
from datetime import datetime, timedelta

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.string_field


def menu():
    print('1) Today\'s tasks\n2) Week\'s tasks\n3) All tasks\n4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit')
    c = int(input())
    if c == 1:
        date = datetime.strftime(datetime.today(), 'Today %d %b:\n')
        print(date)
        tasks = session.query(Task).filter(Task.deadline == datetime.today()).all()
        if tasks:
            i = 1
            for task in tasks:
                print(f'{i}. {task.task}')
                i += 1
        else:
            print("Nothing to do!")
    elif c == 2:
        today = datetime.today()
        for day in range(0, 7):
            day = today + timedelta(days=day)
            date = day.strftime('%A')
            date += datetime.strftime(day, ' %d %b:')
            print('\n' + date)
            tasks = session.query(Task).filter(Task.deadline == day.date()).all()
            if tasks:
                i = 1
                for task in tasks:
                    print(f'{i}. {task.task}\n')
                    i += 1
            else:
                print("Nothing to do!")
    elif c == 3:
        print('All tasks:\n')
        tasks = session.query(Task).order_by(Task.deadline).all()
        if tasks:
            i = 1
            for task in tasks:
                date = datetime.strftime(task.deadline, '%d %b')
                print(f'{i}. {task.task}. {date}')
                i += 1
        else:
            print("Nothing to do!")
    elif c == 4:
        print('Missed tasks:')
        tasks = session.query(Task).filter(Task.deadline < datetime.today().date()).all()
        if tasks:
            i = 1
            for task in tasks:
                date = datetime.strftime(task.deadline, '%d %b')
                print(f'{i}. {task.task}. {date}')
                i += 1
        else:
            print("Nothing is missed!")
        print('\n')
    elif c == 5:
        task = input('Enter task\n')
        deadline = datetime.strptime(input('Enter deadline\n'), '%Y-%m-%d').date()
        session.add(Task(task=task, deadline=deadline))
        session.commit()
        print('The task has been added!')
    elif c == 6:
        print('Choose the number of the task you want to delete:\n')
        tasks = session.query(Task).order_by(Task.deadline).all()
        if tasks:
            i = 1
            for task in tasks:
                date = datetime.strftime(task.deadline, '%d %b')
                print(f'{i}. {task.task}. {date}')
                i += 1
        else:
            print("Nothing to do!")
        index = int(input()) - 1
        session.delete(tasks[index])
        session.commit()
    elif c == 0:
        print('Bye!')
        exit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    while True: menu()
