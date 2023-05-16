import React from "react";
import "./Search.scss"

function Search({ }) {
  const [searchString, setSearchString] = React.useState('')

  function handleChange(evt) {
    setSearchString(evt.target.value)
  }

  return (
    <form className="search">
      <input type="search" name="search" className="search__input" value={searchString} onChange={handleChange} placeholder={"Искать статью"}></input></form>
  )
}

export default Search;
