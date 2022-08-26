//import logo from './logo.svg';
//import "./App.css";
import Header from "./Header";

function App() {
  return (
    <div className="page">
       <Header username={"username"} loggedIn={true}/>
      {/*<Switch>
      <Route exact path="/">
          <Presentation />
        </Route>
        <Route exact path="/profile">
          <Main />
        </Route>
        <Route path="/articles">
          <AllArticles />
        </Route>
        <Route path="/sign-up">
          <Register />
        </Route>
        <Route path="/sign-in">
          <Login />
        </Route>
      </Switch>
      <Footer />
      <FormAddArticle />
      <PopupConfirmDelete /> */}
    </div>
  );
}

export default App;
