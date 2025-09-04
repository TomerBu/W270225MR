SELECT * FROM api_post;

INSERT INTO api_post(title, text, status, created_at, updated_at, author_id) VALUES
('REST API Design', 'Best practices for designing RESTful APIs including proper HTTP methods, status codes, and resource naming conventions', 'draft', '2025-09-04 15:34:15.123456+03', '2025-09-04 15:34:15.123469+03', 1),

('Docker Containerization', 'Complete guide to containerizing applications with Docker, including Dockerfile optimization and multi-stage builds', 'published', '2025-09-04 15:35:22.987654+03', '2025-09-04 15:35:22.987667+03', 1),

('Database Migrations', 'How to handle database schema changes safely in production environments using migration tools and strategies', 'draft', '2025-09-04 15:36:08.555777+03', '2025-09-04 15:36:08.555790+03', 1),

('Authentication & JWT', 'Implementing secure user authentication using JSON Web Tokens, including token refresh strategies and security considerations', 'published', '2025-09-04 15:37:41.333222+03', '2025-09-04 15:37:41.333235+03', 1),

('Testing Strategies', 'Comprehensive testing approach covering unit tests, integration tests, and end-to-end testing for web applications', 'draft', '2025-09-04 15:38:55.888999+03', '2025-09-04 15:38:55.889012+03', 1),

('CI/CD Pipelines', 'Setting up continuous integration and deployment pipelines using GitHub Actions, including automated testing and deployment', 'published', '2025-09-04 15:40:12.444555+03', '2025-09-04 15:40:12.444568+03', 1);


INSERT INTO api_tag(name)
VALUES('Cloud Deployment');


INSERT INTO api_post(title, text, status,created_at,updated_at, author_id)
VALUES('Happy Birthday to our Blog', 'yay!!hay', 'draft', '2025-09-04 15:33:29.523541+03', '2025-09-04 15:33:29.523541+03', 1);

SELECT * FROM api_tag;


SELECT * FROM api_post; -- 10
SELECT * FROM api_tag; -- 8

INSERT INTO api_post_tags(post_id, tag_id)
VALUES(10, 8);

SELECT * FROM api_post_tags;