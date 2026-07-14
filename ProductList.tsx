import React from "react";

interface Product {
  id: number;
  name: string;
  price: number;
  inStock: boolean;
}

interface ProductListProps {
  products: Product[];
}

const ProductList: React.FC<ProductListProps> = ({ products }) => {
  return (
    <div>
      <h2>Список товаров</h2>

      {products.map((product) => (
        <div
          key={product.id}
          style={{
            border: "1px solid #ccc",
            padding: "15px",
            marginBottom: "10px",
            borderRadius: "8px",
          }}
        >
          <h3>{product.name}</h3>
          <p>Цена: {product.price} ₽</p>
          <p>
            {product.inStock ? "✅ В наличии" : "❌ Нет в наличии"}
          </p>
        </div>
      ))}
    </div>
  );
};

export default ProductList;