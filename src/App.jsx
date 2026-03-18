import React, { useState, useEffect } from 'react'
import { Routes, Route, Link } from 'react-router-dom'
import TaskList from './components/TaskList'
import TaskForm from './components/TaskForm'

function App() {
  const [tasks, setTasks] = useState([])

  useEffect(() => {
    const storedTasks = localStorage.getItem('tasks')
    if (storedTasks) {
      setTasks(JSON.parse(storedTasks))
    }
  }, [])

  const addTask = (task) => {
    setTasks([...tasks, task])
    localStorage.setItem('tasks', JSON.stringify([...tasks, task]))
  }

  const deleteTask = (id) => {
    setTasks(tasks.filter((task) => task.id !== id))
    localStorage.setItem('tasks', JSON.stringify(tasks.filter((task) => task.id !== id)))
  }

  return (
    <div className="app">
      <nav>
        <Link to="/">Task List</Link>
        <Link to="/add-task">Add Task</Link>
      </nav>
      <Routes>
        <Route path="/" element={<TaskList tasks={tasks} deleteTask={deleteTask} />} />
        <Route path="/add-task" element={<TaskForm addTask={addTask} />} />
      </Routes>
    </div>
  )
}

export default App