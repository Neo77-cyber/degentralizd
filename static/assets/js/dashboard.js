// add hovered class to selected list item
let list = document.querySelectorAll(".navigation li");

function activeLink() {
  list.forEach((item) => {
    item.classList.remove("hovered");
  });
  this.classList.add("hovered");
}

list.forEach((item) => item.addEventListener("mouseover", activeLink));

// Menu Toggle
let toggle = document.querySelector(".toggle");
let navigation = document.querySelector(".navigation");
let main = document.querySelector(".main");

toggle.onclick = function () {
  navigation.classList.toggle("active");
  main.classList.toggle("active");
};

// getting  the values from the btc section

document.getElementById("buy-button").addEventListener("click", () => {
  const crypto = document.getElementById("crypto-select").value;
  const paymentMethod = document.getElementById("payment-method").value;
  const walletAddress = document.getElementById("wallet-address").value;
  const usdAmount = document.getElementById("usd-amount").value;
  const btcAmount = document.getElementById("btc-amount").value;

  // Replace with actual purchase logic.
  alert(
    `Cryptocurrency purchased!\n\nDetails:\nCrypto: ${crypto}\nPayment Method: ${paymentMethod}\nWallet Address: ${walletAddress}\nUSD Amount: ${usdAmount}\nBTC Amount: ${btcAmount}`
  );
});

// COPY CRYPTO ADDRESS
function copyToClipboard(id) {
  var range = document.createRange();
  range.selectNode(document.getElementById(id));
  window.getSelection().removeAllRanges(); // clear current selection
  window.getSelection().addRange(range); // to select text
  document.execCommand("copy");
  window.getSelection().removeAllRanges(); // to deselect

  // Show an alert
  var walletType;
  if (id === "bitcoinAddress") {
    walletType = "Bitcoin";
  } else if (id === "litecoinAddress") {
    walletType = "Litecoin";
  } else if (id === "ethereumAddress") {
    walletType = "Ethereum";
  }
  alert(
    `Copied ${walletType} wallet address: ${
      document.getElementById(id).textContent
    }`
  );
}
