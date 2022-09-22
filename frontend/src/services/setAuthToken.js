import axios from 'axios'

const setToken = newToken => {
  axios.defaults.headers.common['Authorization'] = ''
  delete axios.defaults.headers.common['Authorization']

  if (newToken) {
    axios.defaults.headers.common['Authorization'] = `Token ${newToken}`
  }
}

export default setToken