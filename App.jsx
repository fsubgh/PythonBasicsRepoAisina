import React, { useReducer } from "react";
import ContactForm from "./ContactForm";
import ContactList from "./ContactList";
import SearchBar from "./SearchBar";

const initialState = {
  contacts: [],
  search: "",
  error: "",
};

function reducer(state, action) {
  switch (action.type) {
    case "ADD_CONTACT":
      if (!action.payload.name || !action.payload.phone) {
        return {
          ...state,
          error: "Введите имя и номер телефона!",
        };
      }

      return {
        ...state,
        error: "",
        contacts: [
          ...state.contacts,
          {
            id: Date.now(),
            ...action.payload,
          },
        ],
      };

    case "DELETE_CONTACT":
      return {
        ...state,
        contacts: state.contacts.filter(
          (contact) => contact.id !== action.payload
        ),
      };

    case "SET_SEARCH":
      return {
        ...state,
        search: action.payload,
      };

    default:
      return state;
  }
}

function App() {
  const [state, dispatch] = useReducer(reducer, initialState);

  const filteredContacts = state.contacts.filter((contact) =>
    contact.name.toLowerCase().includes(state.search.toLowerCase())
  );

  return (
    <div style={{ width: "400px", margin: "20px auto" }}>
      <h2>Контакты</h2>

      <ContactForm dispatch={dispatch} />

      {state.error && (
        <p style={{ color: "red" }}>{state.error}</p>
      )}

      <SearchBar
        search={state.search}
        dispatch={dispatch}
      />

      <ContactList
        contacts={filteredContacts}
        dispatch={dispatch}
      />
    </div>
  );
}

export default App;