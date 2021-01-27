const ACCESS_KEY = "C2DiM1BfxxUM5--zCiZoGiZ18-nwVq0cK0BxqOvVvoA";
const SECRET_KEY = "l5C_JYPo5ss8pUdE247n3L9l1O50fVhYMe09MXjcZBE";
const UNSPLASH_URL = `https://api.unsplash.com/photos/random/?client_id=${ACCESS_KEY}&query=interiors`;

const body = document.querySelector("body");

function initApp() {
  fetch(UNSPLASH_URL)
    .then((response) => response.json())
    .then((json) => {
      const image = json;
      // body.style.backgroundImage = `linear-gradient(rgba(0, 0, 0, 0.4),rgba(0, 0, 0, 0.4)), url(${image.urls.full})`;
      body.style.backgroundImage = `linear-gradient(rgba(0, 0, 0, 0.4),rgba(0, 0, 0, 0.4)), url(${image.urls.full})`;
    });
  return;
}

initApp();
