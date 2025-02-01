import React from 'react';
import '../static/css/HumanMigrationsSubtopics.css';
import UserMonitor from '../components/UserMonitor';

const subtopics = [
  {
    title: "Citizenship Journey",
    keywords: '0.019*"get" + 0.014*"country" + 0.010*"go" + 0.008*"here" + 0.008*"also" + 0.008*"need" + 0.008*"year" + 0.008*"think" + 0.007*"citizenship" + 0.007*"look"'
  },
  {
    title: "Lifework",
    keywords: '0.012*"get" + 0.010*"work" + 0.009*"move" + 0.009*"want" + 0.009*"also" + 0.008*"see" + 0.008*"then" + 0.008*"so" + 0.007*"live" + 0.007*"people"'
  },
  {
    title: "Automated Country Moderation",
    keywords: '0.014*"country" + 0.009*"perform_automatically" + 0.009*"bot_action" + 0.009*"contact_moderator_question_concern" + 0.008*"move_country" + 0.008*"think" + 0.008*"time" + 0.007*"asylum" + 0.007*"political_commentaryrant" + 0.007*"post_offtopic"'
  },
  {
    title: "Level Playing Field",
    keywords: '0.012*"country" + 0.011*"get" + 0.008*"even" + 0.008*"work" + 0.008*"year" + 0.007*"most" + 0.006*"more" + 0.006*"well" + 0.005*"allow" + 0.005*"usually"'
  },
  {
    title: "Spanish Citizenship",
    keywords: '0.011*"want" + 0.010*"spanish" + 0.009*"get" + 0.008*"citizen" + 0.008*"year" + 0.008*"need" + 0.008*"move" + 0.007*"time" + 0.007*"know" + 0.007*"university"'
  },
  {
    title: "Visa & Job Hunt",
    keywords: '0.017*"get" + 0.017*"work" + 0.016*"visa" + 0.012*"need" + 0.012*"just" + 0.011*"job" + 0.011*"country" + 0.008*"year" + 0.007*"take" + 0.006*"go"'
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

const HumanMigrationsSubtopics = () => {
  return (
    <div className="humanMigrationsSubtopics-container">
      <UserMonitor />
      <h1>Subtopics highlighted in the comments related to Human Migrations</h1>
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

export default HumanMigrationsSubtopics;
