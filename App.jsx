import "./App.css";

let clickCount = 0;

function handleClick() {
  clickCount++;
  console.log("Нажатий:", clickCount);
}

function handleChange(event) {
  console.log("Имя:", event.target.value);
}

function handleMouseOver() {
  console.log("Мышь наведена!");
}

function App() {
  return (
    <div className="App">
      {/* 1. Кнопка-счетчик */}
      <button onClick={handleClick}>Нажми меня</button>
      <p>Количество нажатий смотрите в консоли</p>

      {/* 2. Поле ввода */}
      <input
        type="text"
        placeholder="Введите имя"
        onChange={handleChange}
      />
      <p>Смотрите имя в консоли</p>

      {/* 3. Наведение мышки */}
      <div className="highlight" onMouseOver={handleMouseOver}>
        Наведи на меня
      </div>
    </div>
  );
}

export default App;