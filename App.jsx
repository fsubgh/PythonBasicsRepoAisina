import { useState } from "react";
import {
  IntlProvider,
  FormattedMessage,
  FormattedTime,
  FormattedNumber,
} from "react-intl";

const messages = {
  en: {
    greeting: "Hello! Welcome to our application!",
    time: "Current time:",
    price: "Price:",
  },
  ru: {
    greeting: "Привет! Добро пожаловать в наше приложение!",
    time: "Текущее время:",
    price: "Цена:",
  },
  fr: {
    greeting: "Bonjour ! Bienvenue dans notre application !",
    time: "Heure actuelle :",
    price: "Prix :",
  },
};

function App() {
  const [locale, setLocale] = useState("en");

  const now = new Date();
  const price = 2500.5;

  // Валюта зависит от выбранного языка
  const currency = {
    en: "USD",
    ru: "RUB",
    fr: "EUR",
  }[locale];

  return (
    <IntlProvider
      locale={locale}
      messages={messages[locale]}
    >
      <div className="app">
        <h1>
          <FormattedMessage id="greeting" />
        </h1>

        <p>
          <FormattedMessage id="time" />{" "}
          <FormattedTime
            value={now}
            hour="2-digit"
            minute="2-digit"
          />
        </p>

        <p>
          <FormattedMessage id="price" />{" "}
          <FormattedNumber
            value={price}
            style="currency"
            currency={currency}
          />
        </p>

        <div className="buttons">
          <button onClick={() => setLocale("en")}>
            English
          </button>

          <button onClick={() => setLocale("ru")}>
            Русский
          </button>

          <button onClick={() => setLocale("fr")}>
            Français
          </button>
        </div>
      </div>
    </IntlProvider>
  );
}

export default App;

