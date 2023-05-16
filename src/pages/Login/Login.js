import { Form } from '../../components/Form/Form'
import { Input } from '../../components/Input/Input'

export function Login() {
  return (
    <Form
      formName="login"
      type="submit"
      classButton="auth"
      title="Авторизация"
      titleButton="Войти"
      caption="Ещё не зарегистрированы?"
      path="/sign-up"
      linkCaption="Зарегистрироваться"
      >
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
