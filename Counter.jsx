import React from "react";
import useCounter from "./useCounter";

function Counter() {
  const { count, increment, decrement, reset } = useCounter(10, 2);

  return (
    <div style={{ textAlign: "center", marginTop: "30px" }}>
      <h2>Пользовательский счетчик</h2>

      <h1>{count}</h1>

      <button onClick={increment}>Увеличить</button>

      <button onClick={decrement} style={{ marginLeft: "10px" }}>
        Уменьшить
      </button>

      <button onClick={reset} style={{ marginLeft: "10px" }}>
        Сбросить
      </button>
    </div>
  );
}

export default Counter;