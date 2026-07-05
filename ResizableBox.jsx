import { useState, useRef, useEffect } from "react";

function ResizableBox() {
  const boxRef = useRef(null);

  const [size, setSize] = useState({
    width: 0,
    height: 0,
  });

  useEffect(() => {
    console.log("useEffect выполнен");

    const updateSize = () => {
      if (boxRef.current) {
        const rect = boxRef.current.getBoundingClientRect();

        setSize({
          width: Math.round(rect.width),
          height: Math.round(rect.height),
        });

        console.log("Размер:", rect.width, rect.height);
      }
    };

    updateSize();

    window.addEventListener("resize", updateSize);

    return () => {
      window.removeEventListener("resize", updateSize);
    };
  }, []);

  return (
    <div>
      <div
        ref={boxRef}
        style={{
          width: "50vw",
          height: "200px",
          backgroundColor: "skyblue",
          marginBottom: "20px",
        }}
      ></div>

      <p>Ширина: {size.width}px</p>
      <p>Высота: {size.height}px</p>
    </div>
  );
}

export default ResizableBox;