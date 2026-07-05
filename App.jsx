import ButtonWithCallback from "./ButtonWithCallback";

function App() {
  const handleClick = (message) => {
    console.log(message);
  };

  return (
    <div>
      <h1>Callback в React</h1>
      <ButtonWithCallback onButtonClick={handleClick} />
    </div>
  );
}

export default App;