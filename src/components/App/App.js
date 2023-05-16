import "./App.scss"
import { Route, Routes } from "react-router-dom";
import { Board } from "../../pages/Board/Board";
import { Login } from "../../pages/Login/Login";


function App() {
  return (
    <div className="page">
      <Routes>
        <Route path="/" element={<Board/>}/>
        <Route path="/sign-in" element={<Login/>}/>
      </Routes>
      {/*<Switch>
      <Route exact path="/">
          <Presentation />
  </Route>
        <Route exact path="/profile">*/}

      {/*</Route>
        <Route path="/articles">
          <AllArticles />
        </Route>
        <Route path="/sign-up">
          <Register />
        </Route>
        <Route path="/sign-in">
          <Login />
        </Route>
      </Switch>*/}

      {/* <FormAddArticle />
      <PopupConfirmDelete />  */}
    </div>
  );
}

export default App;
