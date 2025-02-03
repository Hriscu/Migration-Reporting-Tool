import React from 'react';
import '../static/css/About.css';
import UserMonitor from '../components/UserMonitor'; 

const About = () => {
  return (
    <div vocab='https://schema.org/' typeof='AboutPage'>
      <div className="about-container">
        <UserMonitor />      
        <h1 property='name'>About the Migration Reporting Tool</h1>
        <p property='description'>
          This application is designed to provide an interactive map showcasing the migrations performed by various entities, including birds, humans and extraterrestrial beings. These migrations are tracked in real-time, taking into account various factors such as seasons, working conditions, political factors, and calamities.
        </p>
        <p property='description'>
          Migration-related events are reported through GPS information and optional metadata, either directly through our platform or via the #mig-here hashtag on social networks such as Reddit.
        </p>
        <p property='description'>
          In addition to the map, the platform offers detailed statistics and visualizations on the migratory patterns of specific species, including geographical areas, climate conditions, seasons, and user-generated content (such as comments, images, and videos).
        </p>
        <p property='description'>
          All of this data is accessible through a SPARQL endpoint, which is enhanced with additional knowledge from DBpedia.
        </p>
        <p property='description'>We also explored a stream processing approach to make the data even more real-time and dynamic using Async PRAW (the Asynchronous Python Reddit API Wrapper).</p>
      </div>
    </div>
  );
};

export default About;
