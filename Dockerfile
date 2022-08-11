FROM node:alpine
RUN apk add python3
RUN apk add py3-beautifulsoup4
RUN apk add py3-requests
ADD scraper.py ./scraper.py
CMD ["python3" , "./scraper.py"]
