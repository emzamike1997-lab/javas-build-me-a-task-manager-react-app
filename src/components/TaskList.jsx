import React from 'react'

function TaskList({ tasks, deleteTask }) {
    return (
        <div className="task-list">
            <h2>Tasks</h2>
            <ul>
                {tasks.map((task) => (
                    <li key={task.id}>
                        <span>{task.title}</span>
                        <button onClick={() => deleteTask(task.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default TaskList