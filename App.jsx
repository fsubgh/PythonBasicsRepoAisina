import { useState } from "react";
import UserCard from "./UserCard";

function App() {
  const [age, setAge] = useState(20);
  const [color, setColor] = useState("lightblue");

  const changeAge = () => {
    setAge(age + 1);
  };

  const changeColor = () => {
    setColor(color === "lightblue" ? "lightgreen" : "lightblue");
  };

  return (
    <div>
      <UserCard
        name="Айжан"
        age={age}
        color={color}
      />

      <button onClick={changeAge}>
        Изменить возраст
      </button>

      <button onClick={changeColor}>
        Изменить цвет
      </button>
    </div>
  );
}

export default App;