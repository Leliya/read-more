import { Form } from '../../components/Form/Form'
import { Input } from '../../components/Input/Input'

export function Register() {
  return (
    <Form
      formName="register"
      type="submit"
      classButton="auth"
      title="Регистрация"
      titleButton="Зарегистрироваться"
      caption="Уже зарегистрированы?"
      path="/sign-in"
      linkCaption="Войти">
      <Input
        type="text"
        inputName="username"
        required
        placeholder="Username"
        classInput="auth"
      />
      <Input
        type="text"
        inputName="first_name"
        required
        placeholder="Имя"
        classInput="auth"
      />
      <Input
        type="email"
        inputName="email"
        required
        placeholder="Email"
        classInput="auth"
      />
      <Input
        type="password"
        inputName="password"
        required
        placeholder="Пароль"
        classInput="auth"
      />
    </Form>
  )
}
