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
    greeting: "Здравствуйте! Добро пожаловать в наше приложение!",
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

  const currency = {
    en: "USD",
    ru: "RUB",
    fr: "EUR",
  };

  const currentTime = new Date();

  return (
    <IntlProvider
      locale={locale}
      messages={messages[locale]}
    >
      <div>
        <h1>
          <FormattedMessage id="greeting" />
        </h1>

        <p>
          <FormattedMessage id="time" />{" "}
          <FormattedTime
            value={currentTime}
            hour="2-digit"
            minute="2-digit"
          />
        </p>

        <p>
          <FormattedMessage id="price" />{" "}
          <FormattedNumber
            value={2500.5}
            style="currency"
            currency={currency[locale]}
          />
        </p>

        <div>
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