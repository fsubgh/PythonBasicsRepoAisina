function ButtonWithCallback({ onButtonClick }) {
  return (
    <button onClick={() => onButtonClick("Кнопка была нажата!")}>
      Нажми меня
    </button>
  );
}

export default ButtonWithCallback;