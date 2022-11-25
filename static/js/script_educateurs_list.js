//console.log(database)
'use strict';

const displayMapButton = document.querySelector('.display-map-button')
const mapElement = document.querySelector('#map')
const searchAroundMeButton = document.querySelector('.search-around-me-button')

const seeAllEducateursButton = document.querySelector(".see-all-educateurs")
const hiddenEducateurs = document.querySelectorAll('.educateur.hidden')

class App {
    map;
    mapEvent;
    latLng;
    database = database;
    markerIcon;
    markers = [];
    latLongMarkersTEST = [
        [48.5092884, 2.6335495],
        [48.565139, 2.7766934],
        [48.6026308, 2.3149944],
        [48.737491, 2.7366616]
    ]

    constructor() {
        // console.log(this.database);
        this.loadMap();
        this.initiateMarker();
        this.loadMarkers();
        // searchAroundMeButton.addEventListener("click", this.getPosition)
        // displayMapButton.addEventListener("click", this.displayMap);
        seeAllEducateursButton.addEventListener("click", this.displayAllEducateurs)
    }

    loadMap() {
        let mapView = this.database ? Object.values(this.database)[0]["lat_long"] : [48.565139, 2.7766934]
        this.map = L.map('map').setView(mapView, 6);
        L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors | Mon Educateur Canin'
        }).addTo(this.map);
    }

    initiateMarker() {
        const markerIconFilepath = '/static/assets/favicon.png'
        this.markerIcon = L.icon({
            iconUrl: markerIconFilepath,
            iconSize: [60, 60], // size of the icon
            iconAnchor: [30, 30], // point of the icon which will correspond to marker's location
            popupAnchor: [0, -30] // point from which the popup should open relative to the iconAnchor
        });
    }

    loadMarkers() {
        Object.keys(this.database).forEach(key => {
            let id = key;
            let latLong = this.database[key]["lat_long"];
            let name = this.database[key]["name"];
            let image = this.database[key]["image"];
            let website = this.database[key]["website"];
            let address = this.database[key]["address"];
            let googleReviews = this.database[key]["googleReviews"]
            let page = `/educateur/${key}`;
            let popup = `
                <div class="educateur educateur-popup" data-id="${id}">
                    <div class="educateur-bio">
                        <img src="${image}" alt="">
                        <p class="educateur-name">${name}</p>
                    </div>
                    <div class="educateur-details">
                        <p class="educateur-address">📍${address}</p>
                        <p class="educateur-review">${googleReviews}</p>
                        <div class="educateur-buttons">
                            <a class="educateur-button educateur-page" href="${page}">En savoir plus</a>
                            <a class="educateur-button educateur-website" href="${website}" target="_blank">Voir le site</a>
                        </div>
                    </div>
                </div>
            `;
            let marker = L.marker(latLong, {icon: this.markerIcon}).addTo(this.map).bindPopup(popup);
            this.markers.push(marker);
        })
    }

    getPosition() {
        const options = {
          enableHighAccuracy: true,
          timeout: 5000,
          maximumAge: 0
        };
        if (navigator.geolocation)
			navigator.geolocation.getCurrentPosition(this.moveMapToLocation.bind(this), function () {
				alert('Veuillez autoriser la localisation pour utiliser cette fonction.');
			}, options);
    }

    moveMapToLocation(position) {
        const { latitude, longitude } = position.coords;
        this.map.setView([latitude, longitude], 13, {animate: true, duration: 0.5});
    }

    // displayMap() {
    //     mapElement.classList.toggle('map-hidden');
    //     displayMapButton.innerText === 'Afficher la carte' ? (displayMapButton.innerText = 'Cacher la carte') : (displayMapButton.innerText = 'Afficher la carte');
    // }

    displayAllEducateurs() {
        hiddenEducateurs.forEach(hiddenEducateur => {
            hiddenEducateur.classList.toggle('hidden');
        })
        seeAllEducateursButton.innerText === 'Voir tous les éducateurs' ? (seeAllEducateursButton.innerText = 'Cacher les éducateurs') : (seeAllEducateursButton.innerText = 'Voir tous les éducateurs');
    }
}

const app = new App();

searchAroundMeButton.addEventListener("click", function(){
    const options = {
          enableHighAccuracy: true,
          timeout: 5000,
          maximumAge: 0
        };
        if (navigator.geolocation)
			navigator.geolocation.getCurrentPosition(function(position){
                app.moveMapToLocation(position);
            }, function () {
				alert('Veuillez autoriser la localisation pour utiliser cette fonction.');
			}, options);
})