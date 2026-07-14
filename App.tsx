import React from "react";
import ProductList from "./ProductList";

interface Product {
  id: number;
  name: string;
  price: number;
  inStock: boolean;
}

const products: Product[] = [
  {
    id: 1,
    name: "Ноутбук",
    price: 75000,
    inStock: true,
  },
  {
    id: 2,
    name: "Мышь",
    price: 1500,
    inStock: false,
  },
  {
    id: 3,
    name: "Монитор",
    price: 12000,
    inStock: true,
  },
];

function App() {
  return (
    <div>
      <ProductList products={products} />
    </div>
  );
}

export default App;