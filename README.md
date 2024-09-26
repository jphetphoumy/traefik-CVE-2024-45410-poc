# Shadow Corp CTF Challenge

Welcome to the Shadow Corp Capture the Flag (CTF) challenge! This challenge will test your skills in identifying and exploiting vulnerabilities related to security headers and HTTP proxy behavior. Your mission is to bypass protections and uncover secrets hidden within the Shadow Corp web application.

## Story

You’ve discovered the public-facing web interface of Shadow Corp, a notorious organization involved in covert cyber espionage. Rumor has it, they’ve secured a protected endpoint that only trusted insiders can access. However, there are whispers that with the right techniques, you can trick the system into revealing this hidden endpoint and expose Shadow Corp's secrets.

Your task: access the protected endpoint and retrieve the hidden flag!

## Setup

This CTF can be run locally, and you'll need to install and configure the web application.

# Prerequisites
docker compose is required to run this application
curl is recommended for querying and testing endpoints.
# How to Run

Clone the repository and navigate to the project directory:

```
cd traefik-CVE-2024-45410-poc
```

Run the CTF

```
docker compose up
```

# The Challenge

## Your Objective

Your primary goal is to access the /protected endpoint and retrieve the secret flag. However, you’ll notice that direct access is blocked unless certain conditions are met. The system checks for trusted sources by validating the X-Forwarded-Host header.

### Clue 1: Who Can Access?

The application is designed to only allow access from localhost (127.0.0.1). However, if you inspect the HTTP headers carefully, you might discover a way to "trick" the server into believing you are a trusted source. Look into HTTP proxy headers and how they can be manipulated.

### Clue 2: Headers Hold the Key

Have you ever explored hop-by-hop headers? These headers are commonly used by proxies to control or modify the behavior of forwarded requests. By correctly manipulating these headers, you might be able to convince the server that you're coming from a trusted location, even if you're not.

### Clue 3: Two Steps to Success
The Connection header can be a game-changer. What if you could introduce a header that the system implicitly trusts? Explore how you might modify the request headers to include X-Forwarded-Host in a way the server might not expect.

Example Command (Non-Solution)
Here’s an example of how to start experimenting with curl:

```bash
curl -i http://localhost:5000/protected
```

This will show you that access is denied by default.

### Clue 4: Hop-by-Hop Headers Can Be Your Ally

In some systems, certain headers are considered hop-by-hop, meaning they control the behavior of each intermediary in a chain of HTTP requests. These headers are stripped or altered by proxies. However, if you cleverly manipulate the headers and specify the right hop-by-hop header, you might find a way to bypass certain security mechanisms. Focus on how the Connection header works and how you might influence other headers that usually aren't forwarded beyond a single hop. This could help you trick the server into thinking you’re a trusted client.



Start thinking about how to tweak your request to gain access. The answer lies in how the application handles trusted host headers. Remember, manipulating headers may be the key to solving this CTF.

