document.getElementById("demo").addEventListener("mouseover", mouseOver);
document.getElementById("demo").addEventListener("mouseout", mouseOut);

function mouseOver(str) {
  document.getElementById("demo").border = str;
}

function mouseOut() {
  document.getElementById("demo").border = none;
}