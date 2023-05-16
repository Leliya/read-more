import { Link } from 'react-router-dom'
import { Button } from '../Button/Button'
import './Form.scss'

export function Form({
  children,
  formName,
  type,
  classButton,
  title,
  titleButton,
  caption,
  path,
  linkCaption,
}) {
  return (
    <div className="box">
      <h1 className="box__title">{title}</h1>
      <form className="form" name={formName}>
        <fieldset className="form__fieldset">{children}</fieldset>
      </form>
      <Button type={type} classButton={classButton} title={titleButton} />
      <span className="box__caption">
        {caption}
        <Link to={path} className="box__link">
          {linkCaption}
        </Link>
      </span>
    </div>
  )
}
