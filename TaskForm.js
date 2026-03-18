This component will render a form to add new tasks. It will receive an addTask function as a prop.

```javascript
import React, { useState } from 'react';

function TaskForm({ addTask }) {
  const [newTask, setNewTask] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    addTask(newTask);
    setNewTask('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={newTask}
        onChange={(event) => setNewTask(event.target.value)}
        placeholder="Add new task"
      />
      <button type="submit">Add Task</button>
    </form>
  );
}

export default TaskForm;
```