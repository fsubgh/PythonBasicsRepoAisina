import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { useState } from "react";

const API_URL = "https://jsonplaceholder.typicode.com/todos";

function App() {
  const [title, setTitle] = useState("");

  const queryClient = useQueryClient();

  // Получение задач
  const {
    data: todos = [],
    isLoading,
    isError,
    error,
  } = useQuery({
    queryKey: ["todos"],
    queryFn: async () => {
      const response = await fetch(`${API_URL}?_limit=10`);

      if (!response.ok) {
        throw new Error("Ошибка загрузки задач");
      }

      return response.json();
    },
  });

  // Добавление задачи
  const mutation = useMutation({
    mutationFn: async (newTodo) => {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newTodo),
      });

      if (!response.ok) {
        throw new Error("Ошибка добавления задачи");
      }

      return response.json();
    },

    onSuccess: (newTodo) => {
      // JSONPlaceholder не сохраняет POST-запросы,
      // поэтому добавляем новую задачу прямо в кеш.
      queryClient.setQueryData(["todos"], (oldTodos = []) => [
        newTodo,
        ...oldTodos,
      ]);

      setTitle("");
    },

    onError: (error) => {
      console.error("Ошибка:", error);
    },
  });

  const handleSubmit = (event) => {
    event.preventDefault();

    if (!title.trim()) return;

    mutation.mutate({
      title: title,
      completed: false,
      userId: 1,
    });
  };

  if (isLoading) {
    return <p>Загрузка задач...</p>;
  }

  if (isError) {
    return <p>Ошибка: {error.message}</p>;
  }

  return (
    <div>
      <h1>Todo List</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={title}
          onChange={(event) => setTitle(event.target.value)}
          placeholder="Введите задачу"
          disabled={mutation.isPending}
        />

        <button
          type="submit"
          disabled={mutation.isPending}
        >
          {mutation.isPending ? "Добавление..." : "Добавить"}
        </button>
      </form>

      {mutation.isError && (
        <p>Не удалось добавить задачу: {mutation.error.message}</p>
      )}

      {mutation.isSuccess && (
        <p>Задача успешно добавлена!</p>
      )}

      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            {todo.title}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;