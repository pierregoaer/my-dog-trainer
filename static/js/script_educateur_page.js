class App {
    map;
    educateur = educateur;
    latLong;

    constructor() {
        this.getLatLong()
        this.loadMap();
        this.initiateMarker();
        this.loadMarker();
    }

    getLatLong() {
        this.latLong = this.educateur["lat_long"];
    }

    loadMap() {
        this.map = L.map('map').setView(this.latLong, 13);
        L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
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

    loadMarker() {
        let id = this.educateur["id"];
        let name = this.educateur["name"];
        let image = this.educateur["image"];
        let website = this.educateur["website"];
        let googleReviews = this.educateur["googleReviews"]
        let popup = `
            <div class="educateur educateur-popup" data-id="${id}">
                <div class="educateur-bio">
                    <img src="${image}" alt="">
                    <p class="educateur-name">${name}</p>
                </div>
                <div class="educateur-details">
                    <div class="educateur-buttons">
                        <a class="educateur-button educateur-website" href="${website}" target="_blank">Voir le site</a>
                    </div>
                </div>
            </div>
        `;
        let marker = L.marker(this.latLong, {icon: this.markerIcon}).addTo(this.map);
    }
}

const app = new App();
