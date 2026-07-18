import { useState } from "react";
import { produce } from "immer";

function App() {
  const [projects, setProjects] = useState([]);
  const [projectName, setProjectName] = useState("");

  // Добавление проекта
  const addProject = () => {
    if (!projectName.trim()) return;

    setProjects([
      ...projects,
      {
        name: projectName,
        tasks: [],
      },
    ]);

    setProjectName("");
  };

  // Добавление задачи
  const addTask = (index) => {
    const task = prompt("Введите задачу");

    if (!task) return;

    setProjects(
      produce(projects, (draft) => {
        draft[index].tasks.push({
          text: task,
          done: false,
        });
      })
    );
  };

  // Выполнена / не выполнена
  const toggleTask = (projectIndex, taskIndex) => {
    setProjects(
      produce(projects, (draft) => {
        draft[projectIndex].tasks[taskIndex].done =
          !draft[projectIndex].tasks[taskIndex].done;
      })
    );
  };

  // Удаление задачи
  const deleteTask = (projectIndex, taskIndex) => {
    setProjects(
      produce(projects, (draft) => {
        draft[projectIndex].tasks.splice(taskIndex, 1);
      })
    );
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Управление проектами</h1>

      <input
        type="text"
        placeholder="Название проекта"
        value={projectName}
        onChange={(e) => setProjectName(e.target.value)}
      />

      <button onClick={addProject}>
        Добавить проект
      </button>

      <hr />

      {projects.map((project, projectIndex) => (
        <div
          key={projectIndex}
          style={{
            border: "1px solid gray",
            margin: 10,
            padding: 10,
          }}
        >
          <h2>{project.name}</h2>

          <button onClick={() => addTask(projectIndex)}>
            Добавить задачу
          </button>

          <ul>
            {project.tasks.map((task, taskIndex) => (
              <li key={taskIndex}>
                <span
                  style={{
                    textDecoration: task.done ? "line-through" : "none",
                    marginRight: 10,
                  }}
                >
                  {task.text}
                </span>

                <button
                  onClick={() => toggleTask(projectIndex, taskIndex)}
                >
                  {task.done ? "Отменить" : "Выполнено"}
                </button>

                <button
                  onClick={() => deleteTask(projectIndex, taskIndex)}
                >
                  Удалить
                </button>
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}

export default App;