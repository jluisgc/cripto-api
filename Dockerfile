#official phyton runtime image
FROM python:3.9-slim

#set workin directory
WORKDIR /app

#Copy de currenc dir to into de container
COPY . .

#Run python script
CMD ["python", "cripto-api.py"]