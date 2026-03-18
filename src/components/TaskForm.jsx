import React, { useState } from 'react'

function TaskForm({ addTask }) {
  const [title, setTitle] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    addTask({ id: Date.now(), title })
    setTitle('')
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Task title"
      />
      <button type="submit">Add Task</button>
    </form>
  )
}

export default TaskForm