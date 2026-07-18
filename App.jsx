import { useState } from "react";
import useTaskStore from "./store";

function App() {
  const [text, setText] = useState("");

  const { tasks, addTask, toggleTask, deleteTask } = useTaskStore();

  const handleAdd = () => {
    if (!text.trim()) return;

    addTask(text);
    setText("");
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Список задач</h1>

      <input
        type="text"
        placeholder="Введите задачу"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <button onClick={handleAdd}>
        Добавить
      </button>

      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            <input
              type="checkbox"
              checked={task.done}
              onChange={() => toggleTask(task.id)}
            />

            <span
              style={{
                textDecoration: task.done ? "line-through" : "none",
                margin: "0 10px",
              }}
            >
              {task.text}
            </span>

            <button onClick={() => deleteTask(task.id)}>
              Удалить
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;