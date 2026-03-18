This component will render a list of tasks. It will receive the tasks and a deleteTask function as props.

```javascript
import React from 'react';

function TaskList({ tasks, deleteTask }) {
  return (
    <ul>
      {tasks.map((task, index) => (
        <li key={index}>
          {task}
          <button onClick={() => deleteTask(index)}>Delete</button>
        </li>
      ))}
    </ul>
  );
}

export default TaskList;
```