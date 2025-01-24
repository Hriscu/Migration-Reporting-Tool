import React, { useEffect, useState } from 'react'; 
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
    const [markerType, setMarkerType] = useState('black'); // Default: black

    useEffect(() => {
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

        // Marker icons based on type
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

        // Function to create a marker with a specific icon
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

        // Example datasets
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

        // Layer groups
        const birdLayer = L.layerGroup(
            birdMigrations.map(event =>
                L.marker(event.coords, { icon: createCustomIcon('bird', markerType) }).bindPopup(event.description)
            )
        );

        const humanLayer = L.layerGroup(
            humanMigrations.map(event =>
                L.marker(event.coords, { icon: createCustomIcon('humans', markerType) }).bindPopup(event.description)
            )
        );

        const extraterrestrialLayer = L.layerGroup(
            extraterrestrialSightings.map(event =>
                L.marker(event.coords, { icon: createCustomIcon('extraterrestrial', markerType) }).bindPopup(event.description)
            )
        );

        // Add all layers to map by default
        birdLayer.addTo(map);
        humanLayer.addTo(map);
        extraterrestrialLayer.addTo(map);

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

        // Update marker icons when markerType changes
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
            extraterrestrialSightings.forEach(event =>
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

    // Save map as PNG
    const saveMapAsImage = () => {
        html2canvas(document.getElementById('map')).then(canvas => {
            const image = canvas.toDataURL("image/png");
            const link = document.createElement('a');
            link.href = image;
            link.download = 'map.png';
            link.click();
        });
    };

    // Save map as JPG
    const saveMapAsJPG = () => {
        html2canvas(document.getElementById('map')).then(canvas => {
            const image = canvas.toDataURL("image/jpeg");
            const link = document.createElement('a');
            link.href = image;
            link.download = 'map.jpg';
            link.click();
        });
    };

    const saveMapAsPDF = () => {
        html2canvas(document.getElementById('map')).then(canvas => {
            const imgData = canvas.toDataURL('image/png');
            const doc = new jsPDF({
                unit: 'mm', 
                format: 'a4'
            });
    
            // Adding the image to the PDF with adjusted size
            doc.addImage(imgData, 'PNG', 10, 10, 180, 160); // Fit image to A4 size
            doc.save('map.pdf');
        });
    };
    

    return (
        <div style={{ position: 'relative', height: "100vh", width: "100%", display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center' }}>
            {/* Title */}
            <h1 style={{ position: 'absolute', top: '5px', zIndex: 2000, fontSize: '30px', fontWeight: 'bold' }}>
                Dashboard
            </h1>

            {/* Container for map with specific size */}
            <div id="map" style={{ height: "80%", width: "80%" }}></div>

            {/* Toggle Panel Button */}
            <div
                style={{
                    position: 'absolute',
                    top: '80px',
                    left: '190px', 
                    zIndex: 2000,
                }}
            >
                <button
                    onClick={() => setIsPanelOpen((prev) => !prev)}
                    style={{
                        padding: '12px',
                        background: isPanelOpen ? '#dc3545' : '#28a745', 
                        color: 'white',
                        border: 'none',
                        borderRadius: '50%',
                        cursor: 'pointer',
                        boxShadow: '0px 4px 10px rgba(0,0,0,0.2)',
                    }}
                >
                    {isPanelOpen ? 'Close' : 'Panel'}
                </button>
            </div>

            {/* Control Panel with smooth slide-in */}
            {isPanelOpen && (
                <div
                    style={{
                        position: 'absolute',
                        top: 80, 
                        left: 190, 
                        width: '240px',
                        height: 'auto',
                        backgroundColor: 'white',
                        boxShadow: '0px 4px 10px rgba(0,0,0,0.2)',
                        padding: '20px',
                        borderRadius: '8px',
                        zIndex: 1000,
                        animation: 'slideInLeft 0.3s ease-out', 
                    }}
                >
                    <h3>Control Panel</h3>
                    <p>Change marker type:</p>
                    <button
                        onClick={() => setMarkerType('black')}
                        style={{
                            margin: '5px',
                            padding: '10px',
                            background: markerType === 'black' ? '#007bff' : '#ddd',
                            color: markerType === 'black' ? 'white' : 'black',
                            border: 'none',
                            borderRadius: '5px',
                            cursor: 'pointer',
                            transition: 'all 0.3s ease',
                        }}
                    >
                        Black
                    </button>
                    <button
                        onClick={() => setMarkerType('white')}
                        style={{
                            margin: '5px',
                            padding: '10px',
                            background: markerType === 'white' ? '#007bff' : '#ddd',
                            color: markerType === 'white' ? 'white' : 'black',
                            border: 'none',
                            borderRadius: '5px',
                            cursor: 'pointer',
                            transition: 'all 0.3s ease',
                        }}
                    >
                        White
                    </button>
                    <button
                        onClick={() => setMarkerType('colored')}
                        style={{
                            margin: '5px',
                            padding: '10px',
                            background: markerType === 'colored' ? '#007bff' : '#ddd',
                            color: markerType === 'colored' ? 'white' : 'black',
                            border: 'none',
                            borderRadius: '5px',
                            cursor: 'pointer',
                            transition: 'all 0.3s ease',
                        }}
                    >
                        Colored
                    </button>

                    <h4>Save Map</h4>
                    <button onClick={saveMapAsImage}>PNG</button>
                    <button onClick={saveMapAsJPG}>JPG</button>
                    <button onClick={saveMapAsPDF}>PDF</button>
                </div>
            )}

            {/* Styles for animation */}
            <style>{`
                @keyframes slideInLeft {
                    0% {
                        transform: translateX(-20%);
                    }
                    100% {
                        transform: translateX(0);
                    }
                }
            `}</style>
        </div>
    );
};

export default Dashboard;
