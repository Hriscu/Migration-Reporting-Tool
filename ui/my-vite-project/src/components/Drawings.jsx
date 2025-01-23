import React, { useState, useEffect, useRef } from 'react';
import axiosInstance from '../lib/axios';

const Graph = ({ graphName, saved }) => {
  const [hasError, setHasError] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [isSaved, setIsSaved] = useState(saved);
  const iframeRef = useRef(null); // Reference to the iframe
  const url = "http://localhost:8000/api/v1/drawings?name=" + graphName;

  useEffect(() => {
    // Check if the URL is reachable
    const checkConnection = async () => {
      try {
        const response = await fetch(url, { method: 'HEAD' });
        if (!response.ok) {
          throw new Error('Server responded with an error');
        }
        setHasError(false); // URL is reachable
      } catch (error) {
        setHasError(true); // URL is not reachable
      } finally {
        setIsLoading(false); // Loading complete
      }
    };

    checkConnection();
  }, [url]);

  const handleIframeLoad = () => {
    const iframe = iframeRef.current;
    if (iframe && iframe.contentWindow) {
      // Add a message event listener to receive messages from the iframe
      window.addEventListener("message", (event) => {
        if (event.origin !== "http://localhost:8000") {
          console.warn("Untrusted origin:", event.origin);
          return;
        }
        console.log("Message received from iframe:", event.data);
        const { type, nodeId, title, topic } = event.data;
        if (type === "nodeClick" && nodeId && title && topic) {
          const firstThreeWords = title.split(" ").slice(0, 3).join(" ");
          const url = `http://127.0.0.1:8000/api/v1/drawings/posts?post_id=${nodeId}&topic=${topic}&text=${encodeURIComponent(firstThreeWords)}`;
          window.open(url, "_blank");
        } else {
          console.warn("Incomplete or unexpected data received:", event.data);
        }
      });
    }
  };

  const handleSave = async () => {
    try {
      const response = await axiosInstance.post('/favourites', {
        graph_id: graphName,
      });

      console.log(response);
      if (response.status != 200) {
        throw new Error('Failed to save the graph.');
      }

      console.log('Graph saved successfully.');

      setIsSaved(true);
    } catch (error) {
      console.error('Error saving graph:', error);
    }
  };

  const handleDelete = async () => {
    try {
      setIsSaved(false);
      console.log(graphName);
      const response = await axiosInstance.delete(`/favourites?name=${graphName}`);

      console.log(response);
      if (response.status != 200) {
        throw new Error('Failed to delete the graph.');
      }

      console.log('Graph deleted successfully.');
    } catch (error) {
      console.error('Error deleting graph:', error);
    }
  };

  return (
    <div className="drawing">
      {isLoading ? (
        <div style={{ textAlign: 'center', padding: '20px' }}>
          <p>Loading...</p>
        </div>
      ) : hasError ? (
        <div style={{ color: 'red', textAlign: 'center', padding: '20px' }}>
          <h2>Error Loading Graph</h2>
          <p>The server is unreachable. Please check your connection or try again later.</p>
        </div>
      ) : (
        <div>
          <iframe
            ref={iframeRef} // Attach the reference
            src={url}
            scrolling="no"
            frameBorder="0"
            onLoad={handleIframeLoad} // Trigger when the iframe loads
          ></iframe>
          {
            isSaved ? (
              <button className="delete-btn" onClick={handleDelete}>
                Delete
              </button>
            ) : (
              <button className="save-btn" onClick={handleSave}>
                Save
              </button>
            )
          }
        </div>
      )}
    </div>
  );
};

export default Graph;
