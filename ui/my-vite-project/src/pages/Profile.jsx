import React, { useState, useEffect } from 'react';
import profilePlaceholder from '../assets/profile.png';
import '../static/css/Profile.css';
import UserMonitor from '../components/UserMonitor';
import axiosInstance from '../lib/axios';
import '../static/css/Dashboard.css';
import Graph from '../components/Drawings';

const Profile = () => {
  const [user, setUser] = useState(null);
  const [savedCards, setSavedCards] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        setLoading(true);

        const userResponse = await axiosInstance.get('http://localhost:8000/api/v1/identity/profile/');
        setUser({
          email: userResponse.data.email,
          first_name: userResponse.data.first_name,
          last_name: userResponse.data.last_name,
          profilePicture: userResponse.data.profilePicture || profilePlaceholder,
        });

        setSavedCards(userResponse.data.savedCards || []);
      } catch (err) {
        setError(err.response?.data?.detail || 'Failed to load profile');
      } finally {
        setLoading(false);
      }
    };

    fetchProfile();
  }, []);

   const [drawingNames, setDrawingNames] = useState([]);
  

  if (loading) {
    return <div className="profile-container">Loading...</div>;
  }

  if (error) {
    return <div className="profile-container">Error: {error}</div>;
  }

  return (
    <div className="profile-container">
      {/* <UserMonitor /> */}
      <div className="profile-card">
        <div className="profile-header">
          <img src={user.profilePicture} alt="Profile" className="profile-picture" />
          <h2>{user.first_name} {user.last_name}</h2>
        </div>
        <div className="profile-body">
        <p className="email">{user.email}</p>
        </div>
      </div>
    </div>
  );
};

export default Profile;
