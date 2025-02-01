import React from 'react';
import '../static/css/Contact.css';
import UserMonitor from '../components/UserMonitor'; 

const Contact = () => {
  return (
    <div className="contact-container">
      <UserMonitor />      
      <h1>Contact</h1>
      <div className="contact-info">
        <p>Hriscu C. Alexandru-Gabriel</p>
        <p>Email: <a href="mailto:hriscu853@gmail.com">hriscu853@gmail.com</a></p>
        <p>Iațu C. Antonio</p>
        <p>Email: <a href="mailto:antonio.iatu@yahoo.com">antonio.iatu@yahoo.com</a></p>
      </div>
    </div>
  );
};

export default Contact;
