import { useState, lazy, Suspense } from "react";

// UserList будет загружен только тогда,
// когда пользователь нажмёт кнопку
const UserList = lazy(() => import("./UserList"));

function App() {
  const [showUsers, setShowUsers] = useState(false);

  return (
    <div>
      <h1>Главная страница</h1>

      {!showUsers && (
        <button onClick={() => setShowUsers(true)}>
          Показать пользователей
        </button>
      )}

      {showUsers && (
        <Suspense fallback={<p>Загрузка списка пользователей...</p>}>
          <UserList />
        </Suspense>
      )}
    </div>
  );
}

export default App;
