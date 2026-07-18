import React, { Component } from "react";
import QuoteViewer from "./QuoteViewer";

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      showQuotes: true
    };
  }

  toggleQuotes = () => {
    this.setState({
      showQuotes: !this.state.showQuotes
    });
  };

  render() {
    return (
      <div style={{ textAlign: "center", marginTop: "30px" }}>
        <button onClick={this.toggleQuotes}>
          {this.state.showQuotes
            ? "Скрыть цитаты"
            : "Показать цитаты"}
        </button>

        {this.state.showQuotes && <QuoteViewer />}
      </div>
    );
  }
}

export default App;