import React, { Component } from "react";

class QuoteViewer extends Component {
  constructor(props) {
    super(props);

    this.quotes = [
      "Успех — это сумма маленьких усилий, повторяемых изо дня в день.",
      "Никогда не сдавайся.",
      "Действие — ключ к успеху.",
      "Ошибки делают нас сильнее.",
      "Каждый день — новый шанс."
    ];

    this.state = {
      quote: this.getRandomQuote()
    };
  }

  getRandomQuote = () => {
    const randomIndex = Math.floor(Math.random() * this.quotes.length);
    return this.quotes[randomIndex];
  };

  nextQuote = () => {
    this.setState({
      quote: this.getRandomQuote()
    });
  };

  componentDidMount() {
    console.log("QuoteViewer смонтирован");
  }

  componentDidUpdate() {
    console.log("QuoteViewer обновился");
  }

  componentWillUnmount() {
    console.log("QuoteViewer размонтирован");
  }

  render() {
    return (
      <div
        style={{
          border: "1px solid gray",
          padding: "20px",
          width: "500px",
          margin: "20px auto",
          textAlign: "center",
          borderRadius: "10px"
        }}
      >
        <h2>Случайная цитата</h2>

        <p style={{ fontSize: "20px" }}>{this.state.quote}</p>

        <button onClick={this.nextQuote}>
          Следующая цитата
        </button>
      </div>
    );
  }
}

export default QuoteViewer;