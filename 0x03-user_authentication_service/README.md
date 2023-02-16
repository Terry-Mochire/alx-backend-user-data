## 0x03-user_authentication_service

In the industry, you should not implement your own authentication system and use a module or framework that doing it for you (like in Python-Flask: Flask-User). 
Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

#### Resources
- [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
- [Flask User](https://flask-user.readthedocs.io/en/latest/)
- [Requests Module](https://requests.kennethreitz.org/en/latest/user/quickstart/)
- [HTTP Status Codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)

#### Learning Objectives
- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes


#### Tasks

0. User model
1. Create user
2. Find user
3. Update user
4. Hash password
5. Register user
6. Basic Flask app
7. Register user
8. Credentials validation
9. Generate UUIDs
10. Get session ID
11. Log in
12. Find user by session ID
13. Destroy session
14. Log out
15. User profile
16. Generate reset password token
17. Get reset password token
18. Update password
19. Update password endpoint
20. End-to-end integration test

