import React, { useState } from "react";

function ContactForm({ dispatch }) {
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");

  const addContact = () => {
    dispatch({
      type: "ADD_CONTACT",
      payload: {
        name,
        phone,
      },
    });

    setName("");
    setPhone("");
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Имя"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <input
        type="text"
        placeholder="Телефон"
        value={phone}
        onChange={(e) => setPhone(e.target.value)}
      />

      <button onClick={addContact}>
        Добавить
      </button>
    </div>
  );
}

export default ContactForm;