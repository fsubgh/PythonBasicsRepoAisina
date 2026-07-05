import "./App.css";
import UserCard from "./UserCard";

function App() {
  const users = [
    {
      id: 1,
      name: "Иван Иванов",
      age: 20,
      email: "ivan@example.com",
    },
    {
      id: 2,
      name: "Анна Смирнова",
      age: 22,
      email: "anna@example.com",
    },
    {
      id: 3,
      name: "Петр Петров",
      age: 19,
      email: "petr@example.com",
    },
  ];

  return (
    <div className="App">
      <h1>Список пользователей</h1>

      {users.map((user) => (
        <UserCard key={user.id} user={user} />
      ))}
    </div>
  );
}

export default App;