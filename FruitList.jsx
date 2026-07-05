function FruitList({ fruits }) {
  return (
    <ul>
      {fruits.map((fruit, index) => (
        <li key={fruit}>
          {fruit}
        </li>
      ))}
    </ul>
  );
}

export default FruitList;