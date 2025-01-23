import React, { useEffect } from 'react';
import '../static/css/Dashboard.css';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import markerIconPng from 'leaflet/dist/images/marker-icon.png';
import markerShadowPng from 'leaflet/dist/images/marker-shadow.png';

const Dashboard = () => {
    useEffect(() => {
        // Initialize the map
        const map = L.map('map').setView([20, 0], 2);

        // Add tile layers
        const osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 18,
            attribution: '© OpenStreetMap contributors',
        });

        const satellite = L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
            maxZoom: 18,
            attribution: '© OpenStreetMap contributors, Humanitarian OSM',
        });

        osm.addTo(map); // Default layer

        // Define custom marker icon
        const customIcon = L.icon({
            iconUrl: markerIconPng,
            shadowUrl: markerShadowPng,
            iconSize: [25, 41],
            iconAnchor: [12, 41],
            popupAnchor: [1, -34],
            shadowSize: [41, 41],
            shadowAnchor: [12, 41],
        });

        // Example migration datasets
        const birdMigrations = [
            { coords: [51.5074, -0.1278], description: "Bird migration in London." },
            { coords: [55.7558, 37.6173], description: "Bird migration in Moscow." },
        ];

        const humanMigrations = [
            { coords: [40.7128, -74.0060], description: "Seasonal migration in New York." },
            { coords: [34.0522, -118.2437], description: "Human migration in Los Angeles." },
        ];

        const extraterrestrialSightings = [
            { coords: [19.4326, -99.1332], description: "UFO spotted in Mexico City." },
            { coords: [28.6139, 77.2090], description: "UFO activity in Delhi." },
        ];

        // Create marker layers
        const birdLayer = L.layerGroup(
            birdMigrations.map(event =>
                L.marker(event.coords, { icon: customIcon }).bindPopup(event.description)
            )
        );

        const humanLayer = L.layerGroup(
            humanMigrations.map(event =>
                L.marker(event.coords, { icon: customIcon }).bindPopup(event.description)
            )
        );

        const extraterrestrialLayer = L.layerGroup(
            extraterrestrialSightings.map(event =>
                L.marker(event.coords, { icon: customIcon }).bindPopup(event.description)
            )
        );

        birdLayer.addTo(map); // Default overlay

        // Add layer controls
        L.control.layers(
            {
                "OpenStreetMap": osm,
                "Satellite": satellite,
            },
            {
                "Bird Migrations": birdLayer,
                "Human Migrations": humanLayer,
                "Extraterrestrial Sightings": extraterrestrialLayer,
            }
        ).addTo(map);

        // Add scale control
        L.control.scale().addTo(map);

        // Log clicks on the map
        map.on('click', function (e) {
            console.log(`Map clicked at ${e.latlng}`);
        });
    }, []);

    return (
        <div style={{ height: "100vh", width: "100%" }} id="map"></div>
    );
};

export default Dashboard;
