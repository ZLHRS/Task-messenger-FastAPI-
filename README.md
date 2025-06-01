# 🚀 Task Messenger — Backend

**Task Messenger** is a task management system with the roles of **administrators** and **employees**.
Employees receive tasks, change their status as they complete them, and receive email notifications.
Administrators create accounts, assign tasks, and monitor their progress.

---

## 📚 Functionality

- 👤 **Admin panel** — create employee accounts, assign and edit tasks.
- 🧑‍💼 **User panel** — view tasks and change their status.
- ✉️ **Email notifications** — when a new task is assigned to an employee, an email is sent to Gmail.
- 📊 **Execution control** — the administrator sees what stage each task is at.

---

## 🛠️ Technologies

| Technology                        | Purpose                            |
|-----------------------------------|------------------------------------|
| Python 3.12                       | Development language               |
| FastAPI                           | Web framework                      |
| PostgreSQL + SQLAlchemy + Alembic | Database and migrations            |
| Redis                             | Cache                              |
| Celery + RabbitMQ                 | Asynchronous tasks (notifications) |
| Docker + Docker Compose           | Containerization                   |
| black / flake8                    | Formatting and linting             |
| pytest                            | Testing                            |

---

## ⚙️ Install and run

```bash
git clone https://github.com/ZLHRS/Task-messenger-FastAPI.git
cd task_messenger
cp .env.example .env
```
Fill in .env and you can use docker-compose configuration.
```bash
docker-compose up --build -d
```

http://localhost:8000/docs , Note: During first use you need to create tables using endpoint
![image](https://github.com/user-attachments/assets/5aeeff84-d2a9-4784-8564-639523bec483)
in .env you wrote the name and password for the admin, you need to log in and now you can do whatever you want
