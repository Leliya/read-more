import "./Button.scss"

export function Button({ type, classButton, title }) {
  return (
    <button type={type} className={`button button_place_${classButton}`} >
      {title}
    </button>
  )
}
