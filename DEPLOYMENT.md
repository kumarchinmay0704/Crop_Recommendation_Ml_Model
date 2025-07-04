# Deployment Guide - Crop Recommendation System

This guide provides instructions for deploying the Crop Recommendation System in different environments.

## Local Development

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/crop-recommendation-system.git
   cd crop-recommendation-system
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r crop_app3/requirements.txt
   ```

4. **Run the application**
   ```bash
   python crop_app3/crop_app.py
   ```

## Production Deployment

### Option 1: Using Gunicorn (Linux/macOS)

1. **Install Gunicorn**
   ```bash
   pip install gunicorn
   ```

2. **Create a WSGI entry point**
   Create a file named `wsgi.py` in the root directory:
   ```python
   import sys
   import os
   sys.path.append(os.path.join(os.path.dirname(__file__), 'crop_app3'))
   
   from crop_app import app
   
   if __name__ == "__main__":
       app.run()
   ```

3. **Run with Gunicorn**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
   ```

### Option 2: Using Docker

1. **Create a Dockerfile**
   ```dockerfile
   FROM python:3.9-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY . .
   
   EXPOSE 5000
   
   CMD ["python", "crop_app3/crop_app.py"]
   ```

2. **Build and run the Docker container**
   ```bash
   docker build -t crop-recommendation .
   docker run -p 5000:5000 crop-recommendation
   ```

### Option 3: Using Heroku

1. **Create a Procfile**
   ```
   web: gunicorn wsgi:app
   ```

2. **Create runtime.txt**
   ```
   python-3.9.16
   ```

3. **Deploy to Heroku**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

## Environment Variables

Create a `.env` file for configuration:

```env
FLASK_ENV=production
FLASK_DEBUG=False
HOST=0.0.0.0
PORT=5000
```

## Security Considerations

### For Production Deployment

1. **Use HTTPS**
   - Configure SSL certificates
   - Redirect HTTP to HTTPS

2. **Environment Variables**
   - Store sensitive data in environment variables
   - Never commit secrets to version control

3. **Input Validation**
   - The application already includes basic validation
   - Consider adding more robust validation for production

4. **Rate Limiting**
   - Implement rate limiting to prevent abuse
   - Consider using Flask-Limiter

5. **Logging**
   - Configure proper logging
   - Monitor application performance

## Monitoring

### Health Check Endpoint

Add a health check endpoint to your application:

```python
@app.route('/health')
def health_check():
    return {'status': 'healthy'}, 200
```

### Logging Configuration

```python
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    file_handler = RotatingFileHandler('logs/crop_recommendation.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Crop Recommendation System startup')
```

## Performance Optimization

1. **Caching**
   - Implement caching for model predictions
   - Use Redis or Memcached

2. **Database**
   - Consider adding a database for storing predictions
   - Use PostgreSQL or MySQL

3. **Load Balancing**
   - Use multiple application instances
   - Configure a load balancer

## Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Find process using port 5000
   lsof -i :5000
   # Kill the process
   kill -9 <PID>
   ```

2. **Permission denied**
   ```bash
   # Make scripts executable
   chmod +x run.sh
   chmod +x test_app.py
   ```

3. **Module not found**
   ```bash
   # Install missing dependencies
   pip install -r crop_app3/requirements.txt
   ```

### Debug Mode

For development, run Flask in debug mode:

```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

## Support

For deployment issues:
1. Check the logs for error messages
2. Verify all dependencies are installed
3. Ensure the model file is present
4. Test the application locally first

## Next Steps

After successful deployment:
1. Set up monitoring and alerting
2. Configure backups
3. Implement CI/CD pipeline
4. Add comprehensive testing
5. Document API endpoints 