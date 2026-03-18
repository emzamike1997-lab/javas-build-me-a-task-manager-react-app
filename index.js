This is the entry point of the application.

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