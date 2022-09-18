import axios from 'axios'

const baseUrl = process.env.REACT_APP_API_URL ?? 'http://127.0.0.1:8000'

const login = async (credentials) => {
  const response = await axios.post(`${baseUrl}/auth/`, credentials)
  return response.data
}

export default { login }