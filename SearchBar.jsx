import React, { useEffect, useRef } from "react";

function SearchBar({ search, dispatch }) {
  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current.focus();
  }, []);

  return (
    <div style={{ marginTop: "20px" }}>
      <input
        ref={inputRef}
        type="text"
        placeholder="Поиск..."
        value={search}
        onChange={(e) =>
          dispatch({
            type: "SET_SEARCH",
            payload: e.target.value,
          })
        }
      />
    </div>
  );
}

export default SearchBar;