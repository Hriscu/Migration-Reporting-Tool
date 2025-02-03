import React from 'react';
import '../static/css/Contact.css';
import UserMonitor from '../components/UserMonitor'; 

const Contact = () => {
  return (
    <div vocab='https://schema.org/' typeof='ContactPage'>
      <div className="contact-container">
        <UserMonitor />      
        <h1 property='name'>Contact</h1>
        <div property='contactPoint' className="contact-info">
          <p property="author">Hriscu C. Alexandru-Gabriel</p>
          <p property="email">Email: <a href="mailto:hriscu853@gmail.com">hriscu853@gmail.com</a></p>
          <p property="author">Iațu C. Antonio</p>
          <p property="email">Email: <a href="mailto:antonio.iatu@yahoo.com">antonio.iatu@yahoo.com</a></p>
        </div>
      </div>
    </div>
  );
};

export default Contact;
