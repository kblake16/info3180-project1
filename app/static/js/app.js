/* Add your Application JavaScript */
console.log('this is some JavaScript code');
"use strict";
function notify() {
  alert('in here I will do something');
}
window.onload = function()
{
  let prices = document.querySelectorAll(".price span"); 
  for (let i = 0, len = prices.length; i < len; i++) { 
    let price = Number(prices[i].innerHTML).toLocaleString('en'); 
    prices[i].innerHTML = price; 
  }
}

// notify();
