# midtermprojectdjango

# Task Manager

A simple Django-based Task Manager that allows users to create, read, update, delete, and search tasks based on their titles.

## Features
- Create, update, and delete tasks
- Search tasks by title
- Track task statuses (Upcoming, Due Today, Overdue)
- Responsive design with Bootstrap

## Setup
```sh
# Clone the repository
git clone https://github.com/riaguanzon/midtermprojectdjango.git
cd task_manager

# Create a virtual environment and activate it
pipenv shell


# Apply database migrations
python manage.py migrate

# Run the development server
cd task_manager
python manage.py runserver
```

Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Usage
- View all tasks on the homepage.
- Click **Add Task** to create a new task.
- Click **Edit Icon** to modify an existing task.
- Click **Delete Icon** to remove a task.
- Use the search bar to find tasks by title.


