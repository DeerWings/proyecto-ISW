# Use the official Nginx image from the Docker Hub
FROM nginx:alpine

# Copy the HTML, JS, and CSS files into the default Nginx public directory
COPY index.html /usr/share/nginx/html/index.html
COPY script.js /usr/share/nginx/html/script.js
COPY styles.css /usr/share/nginx/html/styles.css

# Expose port 80 to the host
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]