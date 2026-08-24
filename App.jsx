import { useState, useCallback } from "react";
import TodoList from "./TodoList";
import AddTodo from "./AddTodo";

function App() {
  console.log("App");

  const [todos, setTodos] = useState([]);

  const addTodo = useCallback((text) => {
    setTodos((prevTodos) => [
      ...prevTodos,
      {
        id: Date.now(),
        text: text,
      },
    ]);
  }, []);

  return (
    <div>
      <h1>Список задач</h1>

      <AddTodo onAdd={addTodo} />

      <TodoList todos={todos} />
    </div>
  );
}

export default App;