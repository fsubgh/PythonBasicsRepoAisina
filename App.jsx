import { useState } from "react";
import {
  BrowserRouter,
  Routes,
  Route,
  Navigate,
  useLocation,
  useNavigate,
} from "react-router-dom";

import "./App.css";

// Универсальный middleware для защищённых страниц
function ProtectedRoute({ isAuthenticated, children }) {
  const location = useLocation();

  if (!isAuthenticated) {
    return (
      <Navigate
        to="/"
        replace
        state={{
          from: location.pathname,
          message: "Для доступа к этой странице необходимо войти.",
        }}
      />
    );
  }

  return children;
}

// Главная страница
function Home({ isAuthenticated, setIsAuthenticated }) {
  const location = useLocation();

  const redirectedMessage = location.state?.message;

  return (
    <div className="page">
      <h1>Главная страница</h1>

      {redirectedMessage && (
        <div className="error">
          {redirectedMessage}
        </div>
      )}

      {isAuthenticated ? (
        <p>Вы успешно вошли в систему!</p>
      ) : (
        <>
          <p>Вы не авторизованы.</p>

          <button onClick={() => setIsAuthenticated(true)}>
            Войти
          </button>
        </>
      )}
    </div>
  );
}

// Страница профиля
function Profile() {
  return (
    <div className="page">
      <h1>Профиль</h1>
      <p>Вы успешно вошли в систему.</p>
      <p>Это защищённая страница профиля.</p>
    </div>
  );
}

// Страница настроек
function Settings() {
  return (
    <div className="page">
      <h1>Настройки</h1>
      <p>Вы успешно вошли в систему.</p>
      <p>Это защищённая страница настроек.</p>
    </div>
  );
}

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  return (
    <BrowserRouter>
      <nav>
        <a href="/">Главная</a>
        <a href="/profile">Профиль</a>
        <a href="/settings">Настройки</a>
      </nav>

      <Routes>
        {/* Открытая страница */}
        <Route
          path="/"
          element={
            <Home
              isAuthenticated={isAuthenticated}
              setIsAuthenticated={setIsAuthenticated}
            />
          }
        />

        {/* Защищённый маршрут профиля */}
        <Route
          path="/profile"
          element={
            <ProtectedRoute isAuthenticated={isAuthenticated}>
              <Profile />
            </ProtectedRoute>
          }
        />

        {/* Защищённый маршрут настроек */}
        <Route
          path="/settings"
          element={
            <ProtectedRoute isAuthenticated={isAuthenticated}>
              <Settings />
            </ProtectedRoute>
          }
        />

        {/* Если страницы не существует */}
        <Route
          path="*"
          element={<Navigate to="/" replace />}
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
