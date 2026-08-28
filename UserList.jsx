function UserList() {
  const users = [
    {
      id: 1,
      name: "Анна Иванова",
      email: "anna@example.com",
    },
    {
      id: 2,
      name: "Иван Петров",
      email: "ivan@example.com",
    },
    {
      id: 3,
      name: "Мария Смирнова",
      email: "maria@example.com",
    },
    {
      id: 4,
      name: "Алексей Кузнецов",
      email: "alex@example.com",
    },
  ];

  return (
    <div>
      <h2>Список пользователей</h2>

      {users.map((user) => (
        <div key={user.id}>
          <h3>{user.name}</h3>
          <p>{user.email}</p>
        </div>
      ))}
    </div>
  );
}

export default UserList;

