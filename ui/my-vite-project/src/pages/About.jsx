import React from 'react';
import '../static/css/About.css';
import UserMonitor from '../components/UserMonitor'; 

const About = () => {
  return (
    <div className="about-container">
      <UserMonitor />
      <h1>Hot topics!</h1>
    </div>
  );
};

export default About;
