This is the main application file where we will render all the components. 
We will use React Hooks to manage the state of the application.

```javascript
import React, { useState, useEffect } from 'react';
import TaskList from './TaskList.js';
import TaskForm from './TaskForm.js';

function TaskManager() {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState('');

  const addTask = (task) => {
    setTasks([...tasks, task]);
  };

  const deleteTask = (taskId) => {
    setTasks(tasks.filter((task) => task.id !== taskId));
  };

  return (
    <div>
      <TaskForm addTask={addTask} />
      <TaskList tasks={tasks} deleteTask={deleteTask} />
    </div>
  );
}

export default TaskManager;
```