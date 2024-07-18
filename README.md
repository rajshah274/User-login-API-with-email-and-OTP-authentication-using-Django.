# User Login API with Email and OTP Authentication

## Project Overview

This project aims to develop a secure and efficient API system for user authentication using email and One-Time Password (OTP). The system allows users to register with their email, receive an OTP, verify it, and gain access through session tokens managed by JWT.

## Key Features

1. **User Registration**
   - Endpoint to register a new user with an email address.
   - Email format validation and duplicate check.

2. **OTP Generation and Sending**
   - Endpoint to request an OTP.
   - Secure OTP generation.
   - OTP sent to the user's registered email address (printed in the console for this mock setup).

3. **OTP Verification**
   - Endpoint to verify the OTP.
   - User authentication upon successful OTP verification.

4. **Session Management**
   - JWT token generation and management.
   - Secure session tokens for authenticated users.

5. **Security Measures**
   - Rate limiting on OTP requests.
   - Secure algorithms for OTP generation and hashing.
   - Encrypted communication (to be enforced in production).

## Installation
 **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/auth_project.git
   cd auth_project
