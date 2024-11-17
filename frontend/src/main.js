async function fetchWeather() {
    const city = document.getElementById('city').value || 'London';
    const response = await fetch(`http://localhost:5000/weather?city=${city}`);
    const data = await response.json();
    const weatherInfo = document.getElementById('weather-info');
    weatherInfo.innerHTML = `
        <p>City: ${data.name}</p>
        <p>Temperature: ${data.main.temp} °C</p>
        <p>Weather: ${data.weather[0].description}</p>
    `;
}
