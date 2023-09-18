export const formatCurrency = (number, digits = 0) => {
  return new Intl.NumberFormat("zh-TW", {
    style: "currency",
    currency: "TWD",
    minimumFractionDigits: digits,
  }).format(number);
};
