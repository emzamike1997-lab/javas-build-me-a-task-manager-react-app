### Project Structure
```markdown
task-manager/
|---- backend/
|       |---- app.py
|       |---- models.py
|       |---- routes.py
|       |---- tests/
|       |       |---- test_api.py
|       |       |---- test_models.py
|---- frontend/
|       |---- src/
|       |       |---- components/
|       |       |       |---- TaskList.js
|       |       |       |---- TaskForm.js
|       |       |---- App.js
|       |---- index.js
|---- requirements.txt
|---- README.md
```

### === test_api.py ===

```python
# test_api.py
import unittest
from unittest.mock import patch
from flask import Flask, jsonify
from app import app, db
from models import Task

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.db = db

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_get_tasks(self):
        # Create some tasks
        task1 = Task(title='Task 1', description='This is task 1')
        task2 = Task(title='Task 2', description='This is task 2')
        self.db.session.add(task1)
        self.db.session.add(task2)
        self.db.session.commit()

        # Get tasks
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)

    def test_get_task(self):
        # Create a task
        task = Task(title='Task 1', description='This is task 1')
        self.db.session.add(task)
        self.db.session.commit()

        # Get task
        response = self.app.get('/tasks/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['title'], 'Task 1')

    def test_create_task(self):
        # Create a new task
        data = {'title': 'Task 1', 'description': 'This is task 1'}
        response = self.app.post('/tasks', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], 'Task 1')

    def test_update_task(self):
        # Create a task
        task = Task(title='Task 1', description='This is task 1')
        self.db.session.add(task)
        self.db.session.commit()

        # Update task
        data = {'title': 'Task 2', 'description': 'This is task 2'}
        response = self.app.put('/tasks/1', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['title'], 'Task 2')

    def test_delete_task(self):
        # Create a task
        task = Task(title='Task 1', description='This is task 1')
        self.db.session.add(task)
        self.db.session.commit()

        # Delete task
        response = self.app.delete('/tasks/1')
        self.assertEqual(response.status_code, 200)

class TestAPIAuthentication(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login(self):
        # Login
        data = {'username': 'user', 'password': 'password'}
        response = self.app.post('/login', json=data)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        # Logout
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```

### === test_models.py ===

```python
# test_models.py
import unittest
from unittest.mock import patch
from app import db
from models import Task

class TestTaskModel(unittest.TestCase):
    def setUp(self):
        self.db = db

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_task_creation(self):
        # Create a new task
        task = Task(title='Task 1', description='This is task 1')
        self.db.session.add(task)
        self.db.session.commit()
        self.assertEqual(task.title, 'Task 1')
        self.assertEqual(task.description, 'This is task 1')

    def test_task_update(self):
        # Create a task
        task = Task(title='Task 1', description='This is task 1')
        self.db.session.add(task)
        self.db.session.commit()

        # Update task
        task.title = 'Task 2'
        task.description = 'This is task 2'
        self.db.session.commit()
        self.assertEqual(task.title, 'Task 2')
        self.assertEqual(task.description, 'This is task 2')

    def test_task_deletion(self):
        # Create a task
        task = Task(title='Task 1', description='This is task 1')
        self.db.session.add(task)
        self.db.session.commit()

        # Delete task
        self.db.session.delete(task)
        self.db.session.commit()
        self.assertIsNone(Task.query.get(1))

if __name__ == '__main__':
    unittest.main()
```

### === test_routes.py ===

```python
# test_routes.py
import unittest
from unittest.mock import patch
from app import app
from models import Task

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_tasks(self):
        # Create some tasks
        task1 = Task(title='Task 1', description='This is task 1')
        task2 = Task(title='Task 2', description='This is task 2')
        self.app.application.db.session.add(task1)
        self.app.application.db.session.add(task2)
        self.app.application.db.session.commit()

        # Get tasks
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 2)

    def test_get_task(self):
        # Create a task
        task = Task(title='Task 1', description='This is task 1')
        self.app.application.db.session.add(task)
        self.app.application.db.session.commit()

        # Get task
        response = self.app.get('/tasks/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['title'], 'Task 1')

    def test_create_task(self):
        # Create a new task
        data = {'title': 'Task 1', 'description': 'This is task 1'}
        response = self.app.post('/tasks', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], 'Task 1')

    def test_update_task(self):
        # Create a task
        task = Task(title='Task 1', description='This is task 1')
        self.app.application.db.session.add(task)
        self.app.application.db.session.commit()

        # Update task
        data = {'title': 'Task 2', 'description': 'This is task 2'}
        response = self.app.put('/tasks/1', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['title'], 'Task 2')

    def test_delete_task(self):
        # Create a task
        task = Task(title='Task 1', description='This is task 1')
        self.app.application.db.session.add(task)
        self.app.application.db.session.commit()

        # Delete task
        response = self.app.delete('/tasks/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```

### === test_api_authentication.py ===

```python
# test_api_authentication.py
import unittest
from unittest.mock import patch
from app import app
from models import Task

class TestAPIAuthentication(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login(self):
        # Login
        data = {'username': 'user', 'password': 'password'}
        response = self.app.post('/login', json=data)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        # Logout
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```

### === test_models_authentication.py ===

```python
# test_models_authentication.py
import unittest
from unittest.mock import patch
from app import db
from models import Task

class TestTaskModelAuthentication(unittest.TestCase):
    def setUp(self):
        self.db = db

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_task_creation(self):
        # Create a new task
        task = Task(title='Task 1', description='This is task 1')
        self.db.session.add(task)
        self.db.session.commit()
        self.assertEqual(task.title, 'Task 1')
        self.assertEqual(task.description, 'This is task 1')

    def test_task_update(self):
        # Create a task
        task = Task(title='Task 1', description='This is task 1')
        self.db.session.add(task)
        self.db.session.commit()

        # Update task
        task.title = 'Task 2'
        task.description = 'This is task 2'
        self.db.session.commit()
        self.assertEqual(task.title, 'Task 2')
        self.assertEqual(task.description, 'This is task 2')

    def test_task_deletion(self):
        # Create a task
        task = Task(title='Task 1', description='This is task 1')
        self.db.session.add(task)
        self.db.session.commit()

        # Delete task
        self.db.session.delete(task)
        self.db.session.commit()
        self.assertIsNone(Task.query.get(1))

if __name__ == '__main__':
    unittest.main()
```