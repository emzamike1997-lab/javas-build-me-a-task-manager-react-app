### Project Structure

Before we begin, let's assume our project structure is as follows:

```bash
project/
app/
__init__.py
models/
__init__.py
task.py
routes/
__init__.py
task.py
tests/
__init__.py
unit/
__init__.py
test_task.py
test_task_routes.py
integration/
__init__.py
test_task_manager.py
requirements.txt
```

### Backend API Tests

We'll use the `unittest` framework for our tests. We'll write unit tests for our models and routes, and integration tests for our API endpoints.

#### === test_task.py ===

```python
# tests/unit/test_task.py

import unittest
from app.models.task import Task

class TestTaskModel(unittest.TestCase):
    def test_task_creation(self):
        task = Task(title="Test Task", description="This is a test task")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is a test task")

    def test_task_update(self):
        task = Task(title="Test Task", description="This is a test task")
        task.title = "Updated Task"
        self.assertEqual(task.title, "Updated Task")

    def test_task_deletion(self):
        task = Task(title="Test Task", description="This is a test task")
        del task
        self.assertIsNone(Task.get_task_by_id(1))
```

#### === test_task_routes.py ===

```python
# tests/unit/test_task_routes.py

import unittest
from app.routes.task import task_routes
from app.models.task import Task

class TestTaskRoutes(unittest.TestCase):
    def setUp(self):
        self.app = task_routes.test_client()

    def test_get_all_tasks(self):
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)

    def test_get_task_by_id(self):
        task = Task(title="Test Task", description="This is a test task")
        task.save()
        response = self.app.get('/tasks/1')
        self.assertEqual(response.status_code, 200)

    def test_create_task(self):
        response = self.app.post('/tasks', data={'title': 'Test Task', 'description': 'This is a test task'})
        self.assertEqual(response.status_code, 201)

    def test_update_task(self):
        task = Task(title="Test Task", description="This is a test task")
        task.save()
        response = self.app.put('/tasks/1', data={'title': 'Updated Task'})
        self.assertEqual(response.status_code, 200)

    def test_delete_task(self):
        task = Task(title="Test Task", description="This is a test task")
        task.save()
        response = self.app.delete('/tasks/1')
        self.assertEqual(response.status_code, 204)
```

#### === test_task_manager.py ===

```python
# tests/integration/test_task_manager.py

import unittest
from app.routes.task import task_routes
from app.models.task import Task

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.app = task_routes.test_client()

    def test_task_manager(self):
        # Create a task
        response = self.app.post('/tasks', data={'title': 'Test Task', 'description': 'This is a test task'})
        self.assertEqual(response.status_code, 201)

        # Get all tasks
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)

        # Get task by id
        response = self.app.get('/tasks/1')
        self.assertEqual(response.status_code, 200)

        # Update task
        response = self.app.put('/tasks/1', data={'title': 'Updated Task'})
        self.assertEqual(response.status_code, 200)

        # Delete task
        response = self.app.delete('/tasks/1')
        self.assertEqual(response.status_code, 204)
```

### Running Tests

To run the tests, navigate to the project directory and run the following command:

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

This will discover all test files in the `tests` directory and run the tests.