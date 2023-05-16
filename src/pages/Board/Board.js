import Footer from "../../components/Footer/Footer";
import Header from "../../components/Header/Header";
import Main from "../../components/Main/Main";

export function Board() {
  return (
    <>
      <Header username={"username"} loggedIn={true} />
      <Main />
      <Footer />
    </>
  )
}
