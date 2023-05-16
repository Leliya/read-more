import './Input.scss'

export function Input({
  label,
  type,
  inputName,
  required,
  placeholder,
  classInput,
}) {
  return (
    <label className="field">
      {label}
      <input
        type={type}
        name={inputName}
        required={required}
        placeholder={placeholder}
        className={`field__input field__input_type_${classInput}`}
      />
    </label>
  )
}
