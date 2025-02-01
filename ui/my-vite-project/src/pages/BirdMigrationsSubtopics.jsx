import React from 'react';
import '../static/css/BirdMigrationsSubtopics.css';
import UserMonitor from '../components/UserMonitor';

const subtopics = [
  {
    title: "Cardinal Spotting",
    keywords: '0.026*"see" + 0.016*"thank" + 0.013*"so" + 0.012*"cardinal" + 0.011*"also" + 0.010*"love" + 0.010*"very" + 0.008*"year" + 0.008*"spot" + 0.007*"look"'
  },
  {
    title: "Cardinal Time",
    keywords: '0.018*"just" + 0.014*"love" + 0.014*"see" + 0.012*"get" + 0.012*"so" + 0.012*"cardinal" + 0.011*"time" + 0.010*"look" + 0.010*"so_many" + 0.010*"go"'
  },
  {
    title: "Ephemeral Beauty",
    keywords: '0.027*"see" + 0.020*"bird" + 0.020*"love" + 0.014*"beautiful" + 0.011*"never_see" + 0.011*"time" + 0.011*"just" + 0.009*"so" + 0.009*"think" + 0.009*"look"'
  },
  {
    title: "Winter Flock",
    keywords: '0.029*"see" + 0.015*"think" + 0.009*"male" + 0.009*"photo" + 0.009*"so" + 0.009*"winter" + 0.008*"bird" + 0.008*"now" + 0.007*"as" + 0.007*"flock"'
  },
  {
    title: "Bird Banding",
    keywords: '0.037*"see" + 0.028*"bird" + 0.015*"get" + 0.012*"here" + 0.011*"year" + 0.010*"so" + 0.009*"look" + 0.008*"too" + 0.008*"band" + 0.008*"same"'
  },
  {
    title: "Hawk's-Eye View",
    keywords: '0.020*"see" + 0.019*"so" + 0.012*"great" + 0.011*"get" + 0.011*"photo" + 0.009*"very" + 0.008*"really" + 0.008*"way" + 0.008*"tree" + 0.008*"hawk"'
  }
];

const formatKeywords = (keywords) => {
  return keywords
    .split('+')
    .map(item => {
      const match = item.match(/(\d*\.\d+)\*\"(.*?)\"/);
      if (match) {
        const percentage = (parseFloat(match[1]) * 100).toFixed(1) + '%';
        return `${match[2]} (${percentage})`;
      }
      return item;
    })
    .join(', ');
};

const BirdMigrationsSubtopics = () => {
  return (
    <div className="birdMigrationsSubtopics-container">
      <UserMonitor />
      <h1>Subtopics highlighted in the comments related to Bird Migrations</h1>
      <ul className="subtopics-list">
        {subtopics.map((subtopic, index) => (
          <li key={index} className="subtopic-item">
            <h2>{index + 1}. {subtopic.title}</h2>
            <p className="keywords">Keywords: {formatKeywords(subtopic.keywords)}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BirdMigrationsSubtopics;
