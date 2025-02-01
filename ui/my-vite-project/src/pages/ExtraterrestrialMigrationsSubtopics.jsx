import React from 'react';
import '../static/css/ExtraterrestrialMigrationsSubtopics.css';
import UserMonitor from '../components/UserMonitor';

const subtopics = [
  {
    title: "Perception",
    keywords: '0.013*"say" + 0.012*"just" + 0.011*"think" + 0.011*"thing" + 0.009*"people" + 0.008*"more" + 0.007*"see" + 0.007*"look" + 0.005*"know" + 0.005*"very"'
  },
  {
    title: "Human Intelligence Unveiled",
    keywords: '0.008*"look" + 0.008*"say" + 0.007*"human" + 0.007*"intelligence" + 0.006*"see" + 0.006*"explanation" + 0.006*"earth" + 0.005*"ai" + 0.005*"people" + 0.005*"most"'
  },
  {
    title: "Alien Intrusion",
    keywords: '0.008*"alien" + 0.008*"so" + 0.006*"then" + 0.006*"people" + 0.006*"way" + 0.005*"too" + 0.005*"delete" + 0.005*"serious" + 0.005*"post" + 0.005*"just"'
  },
  {
    title: "Automated Moderation",
    keywords: '0.008*"just" + 0.008*"believe" + 0.007*"contact_moderator" + 0.007*"question_concern" + 0.007*"perform_automatically" + 0.007*"bot_action" + 0.007*"new_response_influx_bot" + 0.007*"fudging_permissible" + 0.007*"list_sidebar_post_comment" + 0.007*"intertwine_ufosuap"'
  },
  {
    title: "Frequency of Consciousness",
    keywords: '0.009*"people" + 0.009*"think" + 0.009*"consciousness" + 0.009*"get" + 0.008*"reality" + 0.006*"just" + 0.006*"frequency" + 0.006*"time" + 0.005*"experience" + 0.005*"see"'
  },
  {
    title: "Perception & Action",
    keywords: '0.011*"say" + 0.011*"see" + 0.007*"go" + 0.007*"just" + 0.007*"verify" + 0.007*"so" + 0.007*"look" + 0.006*"believe" + 0.005*"get" + 0.005*"hear"'
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

const ExtraterrestrialMigrationsSubtopics = () => {
  return (
    <div className="extraterrestrialMigrationsSubtopics-container">
      <UserMonitor />
      <h1>Subtopics highlighted in the comments related to Extraterrestrial Migrations</h1>
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

export default ExtraterrestrialMigrationsSubtopics;
