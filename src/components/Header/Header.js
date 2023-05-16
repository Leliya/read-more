import React from "react";
import { Link } from "react-router-dom";
import Search from "../Search/Search";
import "./Header.scss"

function Header({ username, loggedIn }) {
  return (
    <header className="header">
      <div className="header__logo"></div>
      <Search />
      {/* {loggedIn ? (
        <>
          <Link to="/lk" className="header__username">
            {username}
          </Link>
          <Link to="/select" className="like header__like"></Link>
        </>
      ) : (
        <> */}
        <Link to="sign-in" className="button button_place_header">Войти</Link>
          {/* <button type="button" className="button button_place_header" >
            Войти
          </button> */}
          {/* <button type="button" className="button button_place_header">
            Регистрация
          </button> */}
        {/* </> 
      )}*/}
    </header>
  );
}
export default Header;
