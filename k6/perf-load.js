import http from 'k6/http';
import { check, sleep } from 'k6';
import { Rate } from 'k6/metrics';

// Custom metric to track business-level errors
export const errorRate = new Rate('errors');

export const options = {
  // Moderate, CI-friendly stages (optional step only)
  stages: [
    { duration: '20s', target: 30 },
    { duration: '40s', target: 60 },
    { duration: '40s', target: 60 },
    { duration: '20s', target: 0 },
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% of requests under 500ms
    http_req_failed: ['rate<0.05'],   // <5% network/HTTP errors
    errors: ['rate<0.1'],             // <10% business flow errors
  },
};

const BASE_URL = __ENV.BASE_URL || 'http://localhost:5000';

export default function () {
  // 1) Healthcheck (public)
  const health = http.get(`${BASE_URL}/health`);
  check(health, {
    'health 200': (r) => r.status === 200,
    'health json ok': (r) => r.json('status') === 'ok',
  }) || errorRate.add(1);

  // 2) Register (form POST). Our app expects form-encoded fields and redirects on success.
  const username = `user_${__VU}_${__ITER}`;
  const password = 'Test123!';
  const reg = http.post(`${BASE_URL}/register`, { username, password });
  check(reg, {
    'register 200/201/302': (r) => r.status === 200 || r.status === 201 || r.status === 302,
  }) || errorRate.add(1);

  // 3) Login (form POST) -> redirects to /dashboard on success; cookies are kept per VU automatically
  const login = http.post(`${BASE_URL}/login`, { username, password });
  check(login, {
    'login 200/302': (r) => r.status === 200 || r.status === 302,
  }) || errorRate.add(1);

  // 4) Access an authenticated page to verify session is active
  const dash = http.get(`${BASE_URL}/dashboard`);
  check(dash, {
    'dashboard 200': (r) => r.status === 200,
  }) || errorRate.add(1);

  sleep(1);
}
