import PropTypes from 'prop-types'

const LoginForm = ({
  username,
  password,
  handleUsernameChange,
  handlePasswordChange,
  handleSubmit
}) => {

  return (
    <div>
      <form onSubmit={ handleSubmit }>
        <div>
          username
          <input
            value={ username }
            onChange={ handleUsernameChange }>
          </input>
        </div>
        <div>
          password
          <input
            type='password'
            value={ password }
            onChange={ handlePasswordChange }>
          </input>
        </div>
        <div>
          <button type='submit'>login</button>
        </div>
      </form>
    </div>
  )
}

LoginForm.propTypes = {
  username: PropTypes.string.isRequired,
  password: PropTypes.string.isRequired,
  handleUsernameChange: PropTypes.func.isRequired,
  handlePasswordChange: PropTypes.func.isRequired,
  handleSubmit: PropTypes.func.isRequired
}

export default LoginForm