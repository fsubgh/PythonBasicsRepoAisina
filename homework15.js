import React, { useReducer, useState } from "react";

const initialUsers = [
  { id: 1, name: "Иван", active: true },
  { id: 2, name: "Мария", active: false },
  { id: 3, name: "Алексей", active: true },
];

function reducer(state, action) {
  switch (action.type) {
    case "UPDATE_NAME":
      return state.map((user) =>
        user.id === action.payload.id
          ? { ...user, name: action.payload.name }
          : user
      );

    case "TOGGLE_ACTIVE":
      return state.map((user) =>
        user.id === action.payload
          ? { ...user, active: !user.active }
          : user
      );

    case "DELETE_USER":
      return state.filter((user) => user.id !== action.payload);

    default:
      return state;
  }
}

function UserList() {
  const [users, dispatch] = useReducer(reducer, initialUsers);

  const [editedNames, setEditedNames] = useState({});

  const handleInputChange = (id, value) => {
    setEditedNames({
      ...editedNames,
      [id]: value,
    });
  };

  const saveName = (id) => {
    dispatch({
      type: "UPDATE_NAME",
      payload: {
        id,
        name: editedNames[id] || "",
      },
    });
  };

  return (
    <div>
      <h2>Список пользователей</h2>

      {users.map((user) => (
        <div
          key={user.id}
          style={{
            marginBottom: "15px",
            padding: "10px",
            border: "1px solid black",
            color: user.active ? "green" : "gray",
          }}
        >
          <p>
            <strong>{user.name}</strong>
          </p>

          <p>
            Статус: {user.active ? "Активен" : "Неактивен"}
          </p>

          <input
            type="text"
            placeholder="Новое имя"
            value={editedNames[user.id] || ""}
            onChange={(e) =>
              handleInputChange(user.id, e.target.value)
            }
          />

          <button onClick={() => saveName(user.id)}>
            Сохранить
          </button>

          <button
            onClick={() =>
              dispatch({
                type: "TOGGLE_ACTIVE",
                payload: user.id,
              })
            }
          >
            Сменить статус
          </button>

          <button
            onClick={() =>
              dispatch({
                type: "DELETE_USER",
                payload: user.id,
              })
            }
          >
            Удалить
          </button>
        </div>
      ))}
    </div>
  );
}

export default UserList;