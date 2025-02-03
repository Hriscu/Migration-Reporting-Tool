# MiRT (Migration Reporting Tool)
 
<p>Considering observations provided by users (e.g., messages posted on a social network) or various sensors, develop an "intelligent" Web system capable to generate in real-time an interactive map regarding the migrations performed by various entities (birds, humans, robots, extraterrestrial beings) in a specific context (season, working, politic factors, calamity). A migration-related event could be directly reported – in conjunction to the GPS info + optional (meta)data – into the implemented platform or by using #mig-here hashtag on an existing social Web application (Instagram, Twitter, Vimeo). Several useful statistics and visualizations about the migratory habits of specific species – including information on geographical areas, climate, seasons, user comments/images/videos, etc. – should be offered by a SPARQL endpoint – possibly enhanced by additional knowledge from DBpedia and/or Wikidata. Visit also Migration Data Portal. <b>Bonus:</b> adopting a stream processing approach. </p> <p><strong>Related to the bonus: By using a stream processing approach, more suggestive images can be found at <a href="https://github.com/Hriscu/Migration-Reporting-Tool/tree/main/docs/Bonus_stream">this link</a>.</strong></p>

# Requirements

<p> The most important requirements are:</p>

* ✔️ The project consists of a (micro-)service-based Web application (i.e., a software system) developed by using existing social and semantic Web technologies.

* ✔️ A project proposal could be chosen by maximum 4 teams. Each team must have 2 members.

* ✔️ For the final assessment, the team must provide the full functionality of the developed solution, according to the specific requirements stated in the project description and discussed in the first 7 weeks of the semester during practical works (WADe labs).

* ⌛ The project should be developed and deployed according to the actual practices in Web engineering (e.g., documentation, test driven development, modularity, bug reporting, etc.) by using a modern approach regarding source-code management like Bitbucket, GitHub, or similar cloud-based solutions.

* ⌛ Resource representations to be processed by the (Web/mobile) client will include a valid HTML5 code, plus schema.org and RDFa constructs.

* ✔️ Each thing (resource) of interest will be exposed (and shared) by using a generated URL and/or QR code. **For more information, see the Acknowledgements section of this README.**

* ✔️ The code-source and specific content (data) must be available under the terms of the open source licenses and Creative Commons – consult Software Licenses in Plain English and Social Coding and Open Software. **For more information, see the License section of this README.**

<p> The most important requirements are:</p>

* ⌛ A proper use of various "exotic" programming paradigms like functional, distributed, parallel, reactive, etc.

* ⌛ Adopting a cloud-based solution – i.e. for the (RDF) data storage and/or the Web application deployment.

* ⌛ Using specific design patterns regarding the Web application architecture and/or the knowledge modeling – for example, applying various ontology design patterns.

* ✔️ Creativity and social impact of the proposed solution.

* ✔️ Team work – a penalty of 2 points for each assessed component will be applied for a 1-person project effort. Each member of the team will specify the most important contributions to the developed solution. **For more information, see the Progress section of this README.**

* ✔️ Implementation maturity – study Software Quality Checklist and Web Developer Checklist.

* ⌛ Overall impression – e.g., the suitable use of discussed Web technologies, impact on the end users + usability, business aspects, performance, further directions of development – consider things users care about.

# Deliverables & Calendar

<p> At the end of semester's week #17, a student team must deliver the following resources, according to each project proposal: </p>

1. ✔️ A public wiki associated to the WADe project repository should record the solution's progress. The content must be available in English language and minimally tagged with project, infoiasi, wade, and web. All project's deliverables must be referred by this wiki. **This README contains: the record of the solution's progress (in the Progress section of this README), tags (in the Tags section of this README), all project's deliverables (more informations in this section of the README)**

2. ⌛ A general (service-oriented) architecture of the Web application + the overall design from the point of view of a software engineer (for example: main modules, software architecture diagrams, input/output data formats, data/task flows, etc.) and concerning the end users. **From an architectural perspective, the software architecture diagrams can be found at [https://github.com/Hriscu/Migration-Reporting-Tool/tree/main/docs/Software%20architecture%20diagrams](https://github.com/Hriscu/Migration-Reporting-Tool/tree/main/docs/Software%20architecture%20diagrams). From a design perspective, the design is responsive.**

3. ⌛ An OpenAPI specification regarding the REST API – or, alternatively, a schema for the GraphQL API – provided by the project, including various usage examples and pragmatic case studies. **Relevant images of the OpenAPI specification for the REST API (Swagger) can be found at this link: [https://github.com/Hriscu/Migration-Reporting-Tool/tree/main/docs/OpenAPI_Swagger](https://github.com/Hriscu/Migration-Reporting-Tool/tree/main/docs/OpenAPI_Swagger).**

4. ⌛ A Scholarly HTML technical report. Its digital content will be equivalent to a minimum 10 printed A4 pages) describing the most significant details about:

* ⌛ Internal data structures/models to be used and managed by the Web application.

* ⌛ Technical aspects concerning the implemented API(s) – by adopting REST and/or GraphQL – according to the proposed Web system architecture.

* ⌛ Considerations regarding the designed/reused RDF-based knowledge model(s) – for example, the expressiveness and real usage of the proposed and/or reused vocabulary, taxonomy or ontology in the context of the developed system.

* ⌛ Pragmatic use of external data/knowledge sources – e.g., using various knowledge bases like Wikidata and DBpedia, plus several non-trivial SPARQL queries of interest. Also, explain how the solution conforms to the linked data principles.

* ⌛ A user guide of the developed solution – also available as a Scholarly HTML document including screen-captures and explaining at least 3 case-studies –, plus a (U)HD-quality video demonstration (duration: 5—7 minutes).

5. ⌛ A fully implemented and deployed – e.g. in the cloud – solution of the software project.

**Both Scholarly HTML (technical report and user guide) are available at [https://github.com/Hriscu/Migration-Reporting-Tool/tree/main/docs/Technical%20report%20%2B%20user%20guide](https://github.com/Hriscu/Migration-Reporting-Tool/tree/main/docs/Technical%20report%20%2B%20user%20guide)**
<p> <b> All deliverables are mandatory. </b></p>

## 💎 Bonuses

<p> Each team could be awarded with an amount of maximum 3 points for: </p>

* ⌛ adopting SHACL to validate RDF data,

* ⌛ proposing a decentralized approach based on the Solid – an open standard for structuring data, digital identities, and applications on the Web,

* ✔️ using various deep/machine learning and/or blockchain-based techniques. **Machine learning was applied for LDA topic modeling of comments collected from Reddit in this project.**

* ✔️ discussing and adopting methods and/or paradigms regarding the user interaction/experience.  **This project focuses on responsive design, user personas (see [https://github.com/Hriscu/Migration-Reporting-Tool/tree/main/docs/UI-UX%20aspects](https://github.com/Hriscu/Migration-Reporting-Tool/tree/main/docs/UI-UX%20aspects)), color schemes (Color Reference section of this README), and other strategies to enhance user interaction and experience.**

* ⌛ specifying a set of proper statecharts – details of interest, 

* ⌛ considering significant aspects with respect to the interoperability, performance, and/or security of the implemented solution.

## Tags
This project is tagged with:
- `project`
- `infoiasi`
- `wade`
- `web`

## Progress  
The project is being developed in multiple phases:  

1. **Create Repository for the Project on GitHub**  
  - **Completed on:** 16/10/2024  
  - **Handled by:** Hriscu Alexandru-Gabriel  

2. **Early Development of README and UI**  
  - **Completed on:** 06/01/2025  
  - **Handled by:** Hriscu Alexandru-Gabriel  

3. **UI Refinements and Interactive Map Fixes**  
  - **Completed on:** 22–24/01/2025  
  - **Handled by:** Hriscu Alexandru-Gabriel  

4. **Reddit Data Collector API**
  - **Completed on:** 28/01/2025  
  - **Handled by:** Hriscu Alexandru-Gabriel  

5. **Backend Testing**  
  - **Completed on:** 28/01/2025  
  - **Handled by:** Iațu Antonio  

6. **Heroku Testing**
  - **Completed on:** 28/01/2025  
  - **Handled by:** Iațu Antonio  

7. **Reddit Data Collector API - stream processing approach**
  - **Completed on:** 29/01/2025  
  - **Handled by:** Hriscu Alexandru-Gabriel 

8. **Multiple tests Fuseki - Heroku**
  - **Completed on:** 30/01/2025  
  - **Handled by:** Iațu Antonio

9. **Machine Learning with LDA for Topic Modeling**  
  - **Completed on:** 30/01/2025  
  - **Handled by:** Hriscu Alexandru-Gabriel

10. **Test MongoDB - Heroku**
  - **Completed on:** 30/01/2025  
  - **Handled by:** Iațu Antonio

11. **Applying over comments ML with LDA for Topic Modeling**
   - **Completed on:** 31/01/2025  
   - **Handled by:** Hriscu Alexandru-Gabriel

12. **DBpedia and insert to Fuseki**
  - **Completed on:** 31/01/2025  
  - **Handled by:** Iațu Antonio

13. **Posts and comments in Fuseki**
  - **Completed on:** 31/01/2025  
  - **Handled by:** Iațu Antonio

14. **Fix functionalities of UI**
  - **Completed on:** 31/01/2025  
  - **Handled by:** Hriscu Alexandru-Gabriel
  
15. **Make relations and send them to Fuseki**
  - **Completed on:** 01/02/2025  
  - **Handled by:** Iațu Antonio

16. **Fix aspect of UI**
  - **Completed on:** 01/02/2025  
  - **Handled by:** Hriscu Alexandru-Gabriel

17. **Integrate LICENSE MIT and work on README**
  - **Completed on:** 01/02/2025  
  - **Handled by:** Hriscu Alexandru-Gabriel

18. **Endpoint for Frontend**
  - **Completed on:** 02/02/2025  
  - **Handled by:** Iațu Antonio

19. **Preparing deliverables**
  - **Completed on:** 02/02/2025  
  - **Handled by:** Hriscu Alexandru-Gabriel

### Tech Stack

1. Client
  - [React.js](https://reactjs.org)
   
2. Server
  - [Django](https://www.djangoproject.com/)

3. Database
  - [MongoDB](https://www.mongodb.com/products/platform/atlas-database)
4. DevOps

###  Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Primary Color | #FFFFFF |
| Secondary Color | #491c81 |
| Accent Color | #008000 |
| Text Color | #491c81 |

### Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`REDDIT_CLIENT_ID`

`REDDIT_CLIENT_SECRET`

`REDDIT_USER_AGENT`

`MONGO_URI`

`MONGO_DB_NAME`



## License

Distributed under the MIT License. See LICENSE for more information.

## Contact

Hriscu Alexandru-Gabriel - hriscu853@gmail.com

Iațu Antonio - antonio.iatu@yahoo.com

Project Link: [https://github.com/Hriscu/Migration-Reporting-Tool](https://github.com/Hriscu/Migration-Reporting-Tool)

## Acknowledgements

This section is to mention useful resources and libraries that we have used in our project.

 - [geoPy](https://geopy.readthedocs.io/en/stable/)
 - [spaCy](https://spacy.io/)
 - [MongoDB Atlas](https://www.mongodb.com/docs/atlas/)
 - [Django](https://www.djangoproject.com/)
 - [Vite](https://vite.dev/guide/)
 - [LDAvis](https://github.com/cpsievert/LDAvis)
 - [PRAW](https://praw.readthedocs.io/en/stable/)
 - [Async PRAW](https://asyncpraw.readthedocs.io/en/stable/)

