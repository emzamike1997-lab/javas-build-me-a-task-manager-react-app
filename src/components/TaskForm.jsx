import React, { useState } from 'react'

function TaskForm({ addTask }) {
    const [title, setTitle] = useState('')

    const handleSubmit = (e) => {
        e.preventDefault()
        const newTask = { id: Date.now(), title }
        addTask(newTask)
        setTitle('')
    }

    return (
        <div className="task-form">
            <h2>Add Task</h2>
            <form onSubmit={handleSubmit}>
                <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Task title" />
                <button type="submit">Add Task</button>
            </form>
        </div>
    )
}

export default TaskForm