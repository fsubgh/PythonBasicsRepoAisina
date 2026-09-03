function App() {
  const name = "Айсина";
  const profession = "Frontend-разработчик";

  return (
    <div className="card">
      <h1 style={{ color: "purple" }}>
        Привет, я {name}!
      </h1>

      <h2>{profession}</h2>

      <p>
        Я изучаю программирование и создаю сайты и приложения
        с помощью React, JavaScript и других технологий.
      </p>

      <p className="quote">
        💻 «Каждая ошибка — это ещё один шаг к тому, чтобы стать лучше».
      </p>
    </div>
  );
}

export default App;