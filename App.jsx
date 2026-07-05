import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import "./App.css";

// Компоненты страниц
function Home() {
  return (
    <div>
      <h2>Главная</h2>
      <p>Добро пожаловать на главную страницу!</p>
    </div>
  );
}

function About() {
  return (
    <div>
      <h2>О нас</h2>
      <p>Мы изучаем React и React Router.</p>
    </div>
  );
}

function Contacts() {
  return (
    <div>
      <h2>Контакты</h2>
      <p>Email: info@example.com</p>
    </div>
  );
}

function App() {
  return (
    <BrowserRouter>
      {/* Меню навигации */}
      <nav>
        <Link to="/">Главная</Link> |{" "}
        <Link to="/about">О нас</Link> |{" "}
        <Link to="/contacts">Контакты</Link>
      </nav>

      <hr />

      {/* Маршруты */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contacts" element={<Contacts />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;