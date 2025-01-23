import React, { useState } from 'react';
import { Link, redirect } from "react-router-dom";
import logo from '../assets/logo.png';
import '../static/css/NewNavbar.css';

const NewNavbar = () => {
    const [menuOpen, setMenuOpen] = useState(false);

    const toggleMenu = () => {
        setMenuOpen(!menuOpen);
    };

    return (
        <>
            <header>
                <div className="navbar">
                    <div className="logo">
                        <img src={logo} alt="Logo" />
                        <h2>Migration Reporting Tool</h2>
                    </div>

                    <div className={`hamburger-btn ${menuOpen ? 'active' : ''}`} onClick={toggleMenu}>
                        &#9776;
                    </div>

                    <nav className={`links ${menuOpen ? 'show-menu' : ''}`}>
                        <div className="close-btn" onClick={toggleMenu}>
                            &times;
                        </div>
                        <a href="/dashboard">Dashboard</a>
                        <a href="/profile">Profile</a>
                        <div className='login-btn'>
                            <Link to="/login">Login</Link>
                        </div>
                    </nav>
                </div>
            </header>
        </>
    );
};

export default NewNavbar;
