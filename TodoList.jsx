import { useState } from "react";

function TodoList() {
  const [tasks, setTasks] = useState([]);
  const [text, setText] = useState("");

  // Добавление задачи
  const addTask = () => {
    if (text.trim() === "") return;

    const newTask = {
      id: Date.now(),
      text: text,
      completed: false,
    };

    setTasks([...tasks, newTask]);
    setText("");
  };

  // Изменение состояния задачи
  const toggleTask = (id) => {
    setTasks(
      tasks.map((task) =>
        task.id === id
          ? { ...task, completed: !task.completed }
          : task
      )
    );
  };

  // Удаление задачи
  const deleteTask = (id) => {
    setTasks(tasks.filter((task) => task.id !== id));
  };

  const completedCount = tasks.filter(
    (task) => task.completed
  ).length;

  return (
    <div>
      <input
        type="text"
        placeholder="Введите задачу"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <button onClick={addTask}>
        Добавить
      </button>

      <p>
        Выполнено {completedCount} из {tasks.length}
      </p>

      {tasks.length === 0 ? (
        <p>Нет задач</p>
      ) : (
        <ul>
          {tasks.map((task) => (
            <li key={task.id}>
              <input
                type="checkbox"
                checked={task.completed}
                onChange={() => toggleTask(task.id)}
              />

              {task.text}

              <button onClick={() => deleteTask(task.id)}>
                Удалить
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default TodoList;