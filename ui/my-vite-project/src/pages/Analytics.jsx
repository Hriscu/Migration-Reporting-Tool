import React from 'react';
import '../static/css/Analytics.css';
import UserMonitor from '../components/UserMonitor'; 

const Analytics = () => {
  return (
    <div className="analytics-container">
      <UserMonitor />
      <h1>Hot topics!</h1>
    </div>
  );
};

export default Analytics;
