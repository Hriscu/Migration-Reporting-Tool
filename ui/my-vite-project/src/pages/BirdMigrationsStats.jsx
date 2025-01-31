import React from 'react';
import '../static/css/BirdMigrationsStats.css';
import UserMonitor from '../components/UserMonitor'; 

const BirdMigrationsStats = () => {
  return (
    <div className="birdMigrationsStats-container">
      <UserMonitor />
      <h1>Hot topics!</h1>
    </div>
  );
};

export default BirdMigrationsStats;
