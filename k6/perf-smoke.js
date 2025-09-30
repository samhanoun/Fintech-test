import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 1,
  duration: '10s',
  thresholds: {
    http_req_failed: ['rate<0.01'], // less than 1% failures
    http_req_duration: ['p(95)<800'], // 95th percentile under 800ms
  },
};

const BASE_URL = __ENV.BASE_URL || 'http://localhost:5000';

export default function () {
  const res = http.get(`${BASE_URL}/health`);
  check(res, {
    'status is 200': (r) => r.status === 200,
    'contains ok': (r) => r.json('status') === 'ok',
  });
  sleep(1);
}
