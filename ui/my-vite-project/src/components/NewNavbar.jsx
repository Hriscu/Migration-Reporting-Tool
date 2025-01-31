import React, { useState } from 'react';
import { Link } from "react-router-dom";
import logo from '../assets/logo.png';
import '../static/css/NewNavbar.css';

const NewNavbar = () => {
    const [menuOpen, setMenuOpen] = useState(false);

    const toggleMenu = () => {
        setMenuOpen(!menuOpen);
    };

    return (
        <header>
            <nav className="navbar">
                <Link to="/dashboard" className="logo">
                    <img src={logo} alt="Logo" />
                    <h2>Migration Reporting Tool</h2>
                </Link>

                <button className="hamburger-btn" onClick={toggleMenu}>
                    ☰
                </button>

                <ul className={`links ${menuOpen ? 'show-menu' : ''}`}>
                    <li><Link to="/dashboard">Dashboard</Link></li>
                    <li><Link to="/about">About</Link></li>
                    <li><Link to="/contact">Contact</Link></li>
                    <button className="close-btn" onClick={toggleMenu}>✖</button>
                </ul>
            </nav>
        </header>
    );
};

export default NewNavbar;
