function Article() {
  const link = "https://sass-scss.ru/guide/";
  const name =
    "Адаптивный или отзывчивый? Разбираем структуру React-компонентов";
  const thematics = ["CSS", "React", "HTML"];
  return (
    <article className="article article_type_last article_position_right">
      <a className="article__link" href={link} target={"_blank"}>
        <h3 className="article__title">{name}</h3>
      </a>
      <p className="article__comment">Еще одна очень полезная статья</p>
      <p className="article__remark">прочитано</p>
      <div className="article__elements">
        <ul className="article__thematics">
          {thematics.map((thematic, i) => (
            <li className="article__thematic-item" key={i}>
              <p className="article__thematic">{thematic}</p>
            </li>
          ))}
        </ul>
        <div className="article__control">
          <div className="article__icon article__icon_type_like"></div>
          <div className="article__icon article__icon_type_edit"></div>
          <div className="article__icon article__icon_type_delete"></div>
        </div>
      </div>
    </article>
  );
}

export default Article;
