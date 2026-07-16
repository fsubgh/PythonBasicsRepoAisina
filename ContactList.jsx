import React from "react";

const ContactList = React.memo(function ContactList({
  contacts,
  dispatch,
}) {
  return (
    <div style={{ marginTop: "20px" }}>
      {contacts.length === 0 ? (
        <p>Контактов нет.</p>
      ) : (
        contacts.map((contact) => (
          <div
            key={contact.id}
            style={{
              border: "1px solid gray",
              padding: "10px",
              marginBottom: "10px",
            }}
          >
            <h4>{contact.name}</h4>

            <p>{contact.phone}</p>

            <button
              onClick={() =>
                dispatch({
                  type: "DELETE_CONTACT",
                  payload: contact.id,
                })
              }
            >
              Удалить
            </button>
          </div>
        ))
      )}
    </div>
  );
});

export default ContactList;