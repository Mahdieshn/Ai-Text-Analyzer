# 1. Base Image 
FROM node:20-alpine

# 2. Set working directory
WORKDIR /app

# 3. Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# 4. Copy the rest of the code
COPY . .

# 5. Expose the Vite port
EXPOSE 5173

# 6. Run the app with host flag
CMD ["npm", "run", "dev", "--", "--host"]