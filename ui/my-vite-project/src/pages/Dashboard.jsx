import React, { useEffect, useState } from 'react'; 
import { useNavigate } from 'react-router-dom';
import '../static/css/Dashboard.css';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import html2canvas from 'html2canvas'; 
import { jsPDF } from 'jspdf';
import birdBlack from '../assets/birdBlack.png';
import birdWhite from '../assets/birdWhite.png';
import birdColored from '../assets/birdColored.png';
import extraterrestrialBlack from '../assets/extraterrestrialBlack.png';
import extraterrestrialWhite from '../assets/extraterrestrialWhite.png';
import extraterrestrialColored from '../assets/extraterrestrialColored.png';
import humansBlack from '../assets/humansBlack.png';
import humansWhite from '../assets/humansWhite.png';
import humansColored from '../assets/humansColored.png';
import markerShadowPng from 'leaflet/dist/images/marker-shadow.png';

const Dashboard = () => {
    const [isPanelOpen, setIsPanelOpen] = useState(false);
    const [markerType, setMarkerType] = useState('black');
    const navigate = useNavigate();

    useEffect(() => {
        const map = L.map('map').setView([20, 0], 2);

        const osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 18,
            attribution: '© OpenStreetMap contributors',
        });

        const satellite = L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
            maxZoom: 18,
            attribution: '© OpenStreetMap contributors, Humanitarian OSM',
        });

        osm.addTo(map); 

        const markerIcons = {
            bird: {
                black: birdBlack,
                white: birdWhite,
                colored: birdColored,
            },
            extraterrestrial: {
                black: extraterrestrialBlack,
                white: extraterrestrialWhite,
                colored: extraterrestrialColored,
            },
            humans: {
                black: humansBlack,
                white: humansWhite,
                colored: humansColored,
            },
        };

        const createCustomIcon = (type, color) => {
            return L.icon({
                iconUrl: markerIcons[type][color],
                shadowUrl: markerShadowPng,
                iconSize: [25, 41],
                iconAnchor: [12, 41],
                popupAnchor: [1, -34],
                shadowSize: [41, 41],
                shadowAnchor: [12, 41],
            });
        };

        const birdMigrations = [
            { coords: [51.5074, -0.1278], description: "Bird migration in London." },
            { coords: [55.7558, 37.6173], description: "Bird migration in Moscow." },
        ];

        const humanMigrations = [
            { coords: [40.7128, -74.0060], description: "Seasonal migration in New York." },
            { coords: [34.0522, -118.2437], description: "Human migration in Los Angeles." },
        ];

        const extraterrestrialMigrations = [
            { coords: [19.4326, -99.1332], description: "UFO spotted in Mexico City." },
            { coords: [28.6139, 77.2090], description: "UFO activity in Delhi." },
        ];

        const birdLayer = L.layerGroup(
            birdMigrations.map(event =>
                L.marker(event.coords, { icon: createCustomIcon('bird', markerType) }).bindPopup(event.description)
            )
        );

        const extraterrestrialLayer = L.layerGroup(
            extraterrestrialMigrations.map(event =>
                L.marker(event.coords, { icon: createCustomIcon('extraterrestrial', markerType) }).bindPopup(event.description)
            )
        );

        const humanLayer = L.layerGroup(
            humanMigrations.map(event =>
                L.marker(event.coords, { icon: createCustomIcon('humans', markerType) }).bindPopup(event.description)
            )
        );
        birdLayer.addTo(map);
        humanLayer.addTo(map);
        extraterrestrialLayer.addTo(map);

        L.control.layers(
            {
                "OpenStreetMap": osm,
                "Satellite": satellite,
            },
            {
                "Bird Migrations": birdLayer,
                "Extraterrestrial Migrations": extraterrestrialLayer,
                "Human Migrations": humanLayer,
            }
        ).addTo(map);

        const updateMarkers = () => {
            birdLayer.clearLayers();
            birdMigrations.forEach(event =>
                birdLayer.addLayer(
                    L.marker(event.coords, { icon: createCustomIcon('bird', markerType) }).bindPopup(event.description)
                )
            );

            humanLayer.clearLayers();
            humanMigrations.forEach(event =>
                humanLayer.addLayer(
                    L.marker(event.coords, { icon: createCustomIcon('humans', markerType) }).bindPopup(event.description)
                )
            );

            extraterrestrialLayer.clearLayers();
            extraterrestrialMigrations.forEach(event =>
                extraterrestrialLayer.addLayer(
                    L.marker(event.coords, { icon: createCustomIcon('extraterrestrial', markerType) }).bindPopup(event.description)
                )
            );
        };

        updateMarkers();

        return () => {
            map.remove();
        };
    }, [markerType]);

    const exportMap = (format) => {
        const mapElement = document.getElementById('map');
    
        if (!mapElement) {
            console.error("Map element not found");
            return;
        }
    
        const leafletTiles = document.querySelectorAll('.leaflet-tile');
    
        let tilesLoaded = 0;
        const totalTiles = leafletTiles.length;
    
        if (totalTiles === 0) {
            console.error("No tiles found. Try again.");
            return;
        }

        leafletTiles.forEach(tile => {
            if (tile.complete) {
                tilesLoaded++;
            } else {
                tile.onload = () => {
                    tilesLoaded++;
                    if (tilesLoaded === totalTiles) {
                        captureMap(format);
                    }
                };
            }
        });
    
        if (tilesLoaded === totalTiles) {
            captureMap(format);
        }
    };
    
    const captureMap = (format) => {
        const mapElement = document.getElementById('map');
        
        html2canvas(mapElement, {
            useCORS: true, 
            logging: false,
            allowTaint: true,
            backgroundColor: null, 
        }).then(canvas => {
            const imageData = format === 'png' ? canvas.toDataURL("image/png") 
                           : format === 'jpg' ? canvas.toDataURL("image/jpeg", 0.9) 
                           : null;
    
            if (format === 'pdf') {
                const pdf = new jsPDF({
                    orientation: 'landscape',
                    unit: 'mm',
                    format: 'a4'
                });
                pdf.addImage(canvas.toDataURL("image/png"), 'PNG', 10, 10, 277, 190);
                pdf.save('map.pdf');
            } else {
                const link = document.createElement('a');
                link.href = imageData;
                link.download = `map.${format}`;
                link.click();
            }
        }).catch(err => console.error("Error capturing map:", err));
    };

    return (
        <div className="dashboard-container">
            <h1 className="dashboard-title">Dashboard</h1>

            <div className="map-container">
                <div id="map"></div>
            </div>
            {/* Control Panel Toggle Button */}
            <button
                className="toggle-panel-btn"
                onClick={() => setIsPanelOpen(prev => !prev)} // Toggle panel state
                style={{
                    padding: '12px',
                    background: isPanelOpen ? '#dc3545' : '#28a745', // Red when open and green when closed
                    color: 'white',
                    border: 'none',
                    borderRadius: '50%',
                    cursor: 'pointer',
                    boxShadow: '0px 4px 10px rgba(0,0,0,0.2)',
                    transition: 'background 0.3s ease',
                }}
            >
                {isPanelOpen ? 'Close' : 'Panel'}
            </button>
            {/* Control Panel */}
            <div className={`control-panel ${isPanelOpen ? 'open' : ''}`}>
                <h3>Control Panel</h3>
                <h4>Marker types</h4>
                <div className="marker-buttons">
                    <button onClick={() => setMarkerType('black')} className={markerType === 'black' ? 'active' : ''}>Black</button>
                    <button onClick={() => setMarkerType('white')} className={markerType === 'white' ? 'active' : ''}>White</button>
                    <button onClick={() => setMarkerType('colored')} className={markerType === 'colored' ? 'active' : ''}>Colored</button>
                </div>
                <h4>Save Map</h4>
                <div className="save-buttons">
                    <button onClick={() => exportMap('png')}>PNG</button>
                    <button onClick={() => exportMap('jpg')}>JPG</button>
                    <button onClick={() => exportMap('pdf')}>PDF</button>
                </div>
                <h4>Topic distribution</h4>
                <div className="topic-buttons">
                    <h5>Bird migrations</h5>
                    <button onClick={() => navigate('/BirdMigrationsStats')}>Stats</button>
                    <button onClick={() => navigate('/BirdMigrationsSubtopics')}>Subtopics</button>

                    <h5>Extraterrestrial migrations</h5>
                    <button onClick={() => navigate('/ExtraterrestrialMigrationsStats')}>Stats</button>
                    <button onClick={() => navigate('/ExtraterrestrialMigrationsSubtopics')}>Subtopics</button>

                    <h5>Human migrations</h5>
                    <button onClick={() => navigate('/HumanMigrationsStats')}>Stats</button>
                    <button onClick={() => navigate('/HumanMigrationsSubtopics')}>Subtopics</button>
                </div>
            </div>
        </div>
    );
};

export default Dashboard;
