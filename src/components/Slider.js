import Article from "./Article";

function Slider() {
  return (
    <div className="articles-last__slider">
      <div className="articles-last__arrow articles-last__arrow_type_left"></div>
      <Article/>
      <Article/>
      <div className="articles-last__arrow articles-last__arrow_type_right"></div>
    
    </div>
    
  );
}

export default Slider;
