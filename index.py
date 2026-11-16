from flask import Flask, request, render_template_string

app = Flask(__name__)

page = """
<!DOCTYPE html>
<html>
<head>
<title>My Location Map</title>

<meta name="viewport" content="width=device=width, initial scale=1">

<link rel="stylesheet"
href="https://unpkg.com/leaflet/dist/leaflet.css">
<script src="https://unpkg.com/leaflet/dist/leaflet.js"</script>
</head>

<body>

<h1>My Interactive Map</h1>
<p>Enter a place you want to explore!</p>
<input id="place" placeholders="e.g. Lagos">
<button onclick="findPlace()">Find Location</button>
<div id="map"</div>

<script>
let map = L.map('map').setView([0.0236, 37.9062], e);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png' , {
attribution: 'OpenStreetMap'
}).addTo(map);

let marker;
async function findPlace() {
 let place = document.getElementById("place").value;
 
if (!place) {
 alert("Please enter a place!");
 return;
}
let url = "https://nominatin.openstreetmap.org/search?format=json&q="
+encodeURIComponent(place);
let response = await fetch(url);
let data = await response.json();

if (data.length > 0) {
let lat= Number(data[0].lat);
let lon= Number(data[0].lon);

map.setView([lat, lon], 13);

if (marker)  {
   map.removeLayer(marker);

}
marker = L.marker([lat, lon]).addto(map);
marker.bindPopup("You Found: * + place").openPopup();
} else {
    alert("Location Not Found! Try Again!");
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(page)
if  __name__  == " __main__":
        app.run(debug-True)