This is the entry point of our application. We will render the TaskManager component here.

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import TaskManager from './TaskManager.js';

ReactDOM.render(
  <React.StrictMode>
    <TaskManager />
  </React.StrictMode>,
  document.getElementById('root')
);
```