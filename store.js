import { create } from "zustand";

const useTaskStore = create((set) => ({
  tasks: [],

  addTask: (text) =>
    set((state) => ({
      tasks: [...state.tasks, { id: Date.now(), text, done: false }],
    })),

  toggleTask: (id) =>
    set((state) => ({
      tasks: state.tasks.map((task) =>
        task.id === id ? { ...task, done: !task.done } : task
      ),
    })),

  deleteTask: (id) =>
    set((state) => ({
      tasks: state.tasks.filter((task) => task.id !== id),
    })),
}));

export default useTaskStore;