import './App.css';
import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import NewNavbar from './components/NewNavbar'; 
import Dashboard from './pages/Dashboard';
import About from './pages/About';
import Contact from './pages/Contact';
import BirdMigrationsStats from './pages/BirdMigrationsStats';
import BirdMigrationsSubtopics from './pages/BirdMigrationsSubtopics';
import ExtraterrestrialMigrationsStats from './pages/ExtraterrestrialMigrationsStats';
import ExtraterrestrialMigrationsSubtopics from './pages/ExtraterrestrialMigrationsSubtopics';
import HumanMigrationsStats from './pages/HumanMigrationsStats';
import HumanMigrationsSubtopics from './pages/HumanMigrationsSubtopics';

function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false); 
  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  return (
    <Router>
      <NewNavbar isSidebarOpen={isSidebarOpen} toggleSidebar={toggleSidebar} />
      
      <div className={`main-content ${isSidebarOpen ? 'shifted' : ''}`}>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/BirdMigrationsStats" element={<BirdMigrationsStats />} />
          <Route path="/BirdMigrationsSubtopics" element={<BirdMigrationsSubtopics />} />
          <Route path="/ExtraterrestrialMigrationsStats" element={<ExtraterrestrialMigrationsStats />} />
          <Route path="/ExtraterrestrialMigrationsSubtopics" element={<ExtraterrestrialMigrationsSubtopics />} />
          <Route path="/HumanMigrationsStats" element={<HumanMigrationsStats />} />
          <Route path="/HumanMigrationsSubtopics" element={<HumanMigrationsSubtopics />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
