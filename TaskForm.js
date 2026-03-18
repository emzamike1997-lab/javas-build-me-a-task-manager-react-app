This component will render a form where users can input new tasks.

```javascript
import React, { useState } from 'react';

function TaskForm({ addTask }) {
  const [newTask, setNewTask] = useState('');
  const [taskId, setTaskId] = useState(1);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (newTask) {
      addTask({ id: taskId, task: newTask });
      setTaskId(taskId + 1);
      setNewTask('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={newTask}
        onChange={(e) => setNewTask(e.target.value)}
        placeholder="Enter new task"
      />
      <button type="submit">Add Task</button>
    </form>
  );
}

export default TaskForm;
```