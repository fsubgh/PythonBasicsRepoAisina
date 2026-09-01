
import { useState } from "react";
import {
  BrowserRouter,
  Routes,
  Route,
  Navigate,
  useLocation,
  useNavigate,
  Link,
} from "react-router-dom";

// Middleware для защищённых страниц
function Middleware({ isAuthenticated, children }) {
  const location = useLocation();

  if (!isAuthenticated) {
    return (
      <Navigate
        to="/"
        state={{
          message: "Для доступа к этой странице необходимо авторизоваться.",
          from: location.pathname,
        }}
        replace
      />
    );
  }

  return children;
}

// Главная страница
function Home({ isAuthenticated, setIsAuthenticated }) {
  const location = useLocation();

  return (
    <div>
      <h1>Главная страница</h1>

      {location.state?.message && (
        <p style={{ color: "red" }}>
          {location.state.message}
        </p>
      )}

      {!isAuthenticated ? (
        <button onClick={() => setIsAuthenticated(true)}>
          Войти
        </button>
      ) : (
        <p style={{ color: "green" }}>
          Вы авторизованы!
        </p>
      )}

      <hr />

      <nav>
        <Link to="/">Главная</Link>{" "}
        <Link to="/profile">Профиль</Link>{" "}
        <Link to="/settings">Настройки</Link>
      </nav>
    </div>
  );
}

// Страница профиля
function Profile() {
  return (
    <div>
      <h1>Профиль пользователя</h1>
      <p>Вы успешно вошли в систему и получили доступ к профилю.</p>

      <Link to="/">Вернуться на главную</Link>
    </div>
  );
}

// Страница настроек
function Settings() {
  return (
    <div>
      <h1>Настройки</h1>
      <p>Вы успешно вошли в систему и получили доступ к настройкам.</p>

      <Link to="/">Вернуться на главную</Link>
    </div>
  );
}

// Основное приложение
function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  return (
    <BrowserRouter>
      <Routes>
        {/* Главная доступна всем */}
        <Route
          path="/"
          element={
            <Home
              isAuthenticated={isAuthenticated}
              setIsAuthenticated={setIsAuthenticated}
            />
          }
        />

        {/* Защищённый профиль */}
        <Route
          path="/profile"
          element={
            <Middleware isAuthenticated={isAuthenticated}>
              <Profile />
            </Middleware>
          }
        />

        {/* Защищённые настройки */}
        <Route
          path="/settings"
          element={
            <Middleware isAuthenticated={isAuthenticated}>
              <Settings />
            </Middleware>
          }
        />

        {/* Если такого адреса нет — на главную */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
