#Use a base python image (version 3.9)

From loan.py
#Create a working directory for the application

WORKDIR /home/app
#Copy the requirements file into the working directory
COPY loan.py /home/app/loan.py

RUN pip install -r loan.py

#Export the port where the application listens
EXPOSE 1000

#Set the command to run when the container starts
CMD ["python", "loan.py"]