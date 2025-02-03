import React, { useEffect } from 'react';

const UserMonitor = () => {
  useEffect(() => {
    const monitorPageAccess = () => {
      const currentPage = window.location.href; 
      const timestamp = new Date().toISOString(); 

      if (sessionStorage.getItem('lastLoggedPage') !== currentPage) {
        const logEntry = {
          timestamp,
          action: `User accessed page ${currentPage}`,
          page: currentPage,
        };

        saveLog(logEntry); 
        sessionStorage.setItem('lastLoggedPage', currentPage);
      }
    };

    const handleClick = (event) => {
      const action = `User clicked on ${event.target.tagName} at position (${event.clientX}, ${event.clientY})`;
      const currentPage = window.location.href; 
      const timestamp = new Date().toISOString(); 

      const logEntry = {
        timestamp,
        action,
        page: currentPage,
      };

      saveLog(logEntry);
    };

    const handlePopState = monitorPageAccess;

    monitorPageAccess();

    window.addEventListener('popstate', handlePopState);
    document.addEventListener('click', handleClick);

    return () => {
      window.removeEventListener('popstate', handlePopState);
      document.removeEventListener('click', handleClick);
    };
  }, []); 

  const saveLog = async (logEntry) => {
    try {
      // const response = await fetch('http://35.228.54.3:5000/log', {
        const response = await fetch('localhost:5000/log', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(logEntry),
      });

      if (!response.ok) {
        throw new Error('Failed to save log');
      }

      const data = await response.json();
      console.log('Log saved:', data);
    } catch (error) {
      console.error('Error:', error);
      window.location.href = '/';
    }
  };

  return null; 
};

export default UserMonitor;
