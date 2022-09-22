import axios from 'axios'

const baseUrl = process.env.REACT_APP_API_URL ?? 'http://127.0.0.1:8000'
const tasksUrl = `${baseUrl}/api/tasks`

const getAllTasks = () => {
  const request = axios.get(tasksUrl)
  return request.then(response => response.data)
}

const updatedTask = (id, newObject) => {
  const request = axios.put(`${tasksUrl}/${id}/`, newObject)
  return request.then(response => response.data)
}

const createTask = newObject => {
  const request = axios.post(`${tasksUrl}/`, newObject)
  return request.then(response => response.data)
}

const deleteTask = id => {
  const request = axios.delete(`${tasksUrl}/${id}/`)
  return request.then(response => response.data)
}

export default {
  getAllTasks,
  updatedTask,
  deleteTask,
  createTask
}
