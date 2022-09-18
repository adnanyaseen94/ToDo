import { useEffect, useState } from 'react'
import LoginForm from './components/LoginForm'
import loginService from './services/login'

function App() {
  const [userLogged, setUserLogged] = useState(false)
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  useEffect(() => {
    const token = window.localStorage.getItem('userToken')
    if (token) setUserLogged(true)
  }, [])

  const handleLogin = async (event) => {
    event.preventDefault()
    try {
      const token = await loginService.login({
        username, password
      })
      setUserLogged(true)
      window.localStorage.setItem(
        'userToken', token.token
      )
      setUsername('')
      setPassword('')
    } catch (exception) {
      console.log('wrong credentials')
      console.log(exception)
    }
  }

  const handleLogout = () => {
    setUserLogged(false)
    window.localStorage.removeItem('userToken')
  }

  return (
    <>
      <h2>
        To do list
      </h2>
      <div>
        { userLogged ?
          <div>
            welcome
            <button onClick={ handleLogout }>logout</button>
          </div> :
          <LoginForm
            username={ username }
            password={ password }
            handleUsernameChange={({ target }) => setUsername(target.value) }
            handlePasswordChange={({ target }) => setPassword(target.value) }
            handleSubmit={ handleLogin }
          />
        }
      </div>
    </>
  );
}

export default App;
