import FruitList from "./FruitList";

function App() {
  const fruits = ["Яблоко", "Банан", "Апельсин", "Груша", "Киви"];

  return (
    <div>
      <h1>Список фруктов</h1>
      <FruitList fruits={fruits} />
    </div>
  );
}

export default App;