const ACCESS_KEY = "C2DiM1BfxxUM5--zCiZoGiZ18-nwVq0cK0BxqOvVvoA";
const SECRET_KEY = "l5C_JYPo5ss8pUdE247n3L9l1O50fVhYMe09MXjcZBE";
let UNSPLASH_URL = `https://api.unsplash.com/search/photos/?client_id=${ACCESS_KEY}&query=interior&per_page=30`;

const body = document.querySelector("body"),
  links = document.querySelector(".links");

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);

  return Math.floor(Math.random() * (max - min)) + min;
}
function initApp() {
  let cnt = getRandomInt(0, 30);
  fetch(UNSPLASH_URL)
    .then((response) => response.json())
    .then((json) => {
      const image = json;
      body.style.backgroundImage = `linear-gradient(rgba(0, 0, 0, 0.4),rgba(0, 0, 0, 0.4)), url(${image.results[cnt].urls.full})`;
      links.href = `${image.results[cnt].links.html}`;
    });

  return;
}

initApp();
