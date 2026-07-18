import { useContext, useState } from "react";
import { AuthContext } from "./AuthContext";

function LevelThree() {
  const { user } = useContext(AuthContext);

  return (
    <div>
      <h3>Уровень 3</h3>
      {user ? <p>Добро пожаловать, {user}!</p> : <p>Пользователь не вошел</p>}
    </div>
  );
}

function LevelTwo() {
  return (
    <div>
      <h3>Уровень 2</h3>
      <LevelThree />
    </div>
  );
}

function LevelOne() {
  return (
    <div>
      <h3>Уровень 1</h3>
      <LevelTwo />
    </div>
  );
}

function App() {
  const { user, login, logout } = useContext(AuthContext);
  const [name, setName] = useState("");

  return (
    <div style={{ padding: "20px" }}>
      <h1>Авторизация через useContext</h1>

      {user ? (
        <>
          <p>Вы вошли как: <b>{user}</b></p>
          <button onClick={logout}>Выйти</button>
        </>
      ) : (
        <>
          <input
            type="text"
            placeholder="Введите имя"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          <button onClick={() => login(name)}>Войти</button>
        </>
      )}

      <hr />

      <LevelOne />
    </div>
  );
}

export default App;