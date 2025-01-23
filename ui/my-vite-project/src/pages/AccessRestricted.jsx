import React from 'react';
import '../static/css/AccessRestricted.css';
import UserMonitor from '../components/UserMonitor'; 
import '../static/css/Admin.css';

const AccessRestricted = () => {
  return (
    <div className="access-container">
      <UserMonitor />
      <h1>Access Restricted</h1>
      <p>You do not have permission to access this page.</p>
    </div>
  );
};

export default AccessRestricted;
