// there should be the API calls and other logic

import axios from 'axios';

export async function getGraph(graphName) {
  const response = await axios.get(
    `http://localhost:8000/api/v1/drawing?name=${graphName}`
  );
  return response.data;
}

export async function test() {
  const response = await axios.get(`http://localhost:8000/api/v1/test`);
}
