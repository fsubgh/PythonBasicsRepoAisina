const ERROR_MSG = "Ошибка: неверный формат номера телефона.";

function formatPhoneNumber(phone) {
  const trimmed = String(phone).trim();

  if (/^\+7 \d{3} \d{3} \d{4}$/.test(trimmed)) {
    return trimmed;
  }

  const digits = trimmed.replace(/\D/g, "");

  let rest;
  if (digits.length === 11 && digits[0] === "8") {
    rest = digits.slice(1);
  } else if (digits.length === 11 && digits[0] === "7") {
    rest = digits.slice(1);
  } else {
    return ERROR_MSG;
  }

  if (rest.length !== 10 || !/^\d{10}$/.test(rest)) {
    return ERROR_MSG;
  }

  return `+7 ${rest.slice(0, 3)} ${rest.slice(3, 6)} ${rest.slice(6, 10)}`;
}

const phone1 = "89161234567";
console.log(formatPhoneNumber(phone1));

const phone2 = "+79161234567";
console.log(formatPhoneNumber(phone2));

const phone3 = "1234567890";
console.log(formatPhoneNumber(phone3));
