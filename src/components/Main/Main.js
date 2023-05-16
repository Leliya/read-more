import Slider from "../Slider/Slider";
import "./Main.scss"
import "./button.scss"

function Main() {
  return (
    <main className="main">
      <div className="buttons">
        <button type="button" className="button button_place_buttons">
          Добавить статью
        </button>
        <button type="button" className="button button_place_buttons">
          Случайная статья
        </button>
      </div>
      <section className="articles-last">
        <h2 className="articles-last__title">Последние добавленные статьи</h2>
        <Slider />
        {/*<div className="articles-last__slider">
          
          <div className="articles-last__arrow articles-last__arrow_type-left"></div>
           <article className="article article_type_last article_position_left">

          </article> 
          <article className="article article_type_last article_position_right">
            
          </article>
          <div className="articles-last__arrow articles-last__arrow_type-right"></div>
        </div>*/}
        <button className="button_place_articles articles-last__button-articles">Все статьи</button>
      </section>
    </main>
  )
}
export default Main;
