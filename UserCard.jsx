function UserCard({ name, age, color }) {
  console.log("Ререндер UserCard");

  return (
    <div
      style={{
        backgroundColor: color,
        padding: "20px",
        borderRadius: "10px",
        width: "200px",
        marginBottom: "20px",
      }}
    >
      <h2>{name}</h2>
      <p>Возраст: {age}</p>
    </div>
  );
}

export default UserCard;