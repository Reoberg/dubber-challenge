# MAIN GOALS:
# 1. Create a FastAPI app
# The program shall choose 6 numbers for the user.
# The 6 numbers shall be unique. For example {8, 10, 15, 28, 35, 43} is okay {8, 10, 15, 28, 43, 43} is not.
# The numbers shall be presented to the user in numerical order.
# The numbers shall be in the range of 1 to 49 inclusive.
# The application shall be written in any language or languages.
# The application shall be any form of application so long as it has a UI, for example a console application, desktop application, web page, a phone app.
# EXTRA: The numbers shall have a different coloured background: 1-9 grey, 10-19 blue, 20-29, pink, 30-39 green, 40-49 yellow.
# EXTRA: The program shall provide a bonus ball drawn after the original 6.


from fastapi import FastAPI
# Importand CORS middleware to allow requests from the frontend because it will be on different port
from fastapi.middleware.cors import CORSMiddleware

# Imported Pydantic for creating data model
from pydantic import BaseModel

# Imported random library to generate random numbers
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LotteryNumbers(BaseModel):
    numbers: list[int]
    bonus_ball: int

@app.get("/backend/generate_numbers")
async def generate_numbers():
    # We don't want to repeat the same numbers
    # So we will use a set to store the numbers
    numbers_result = set()
    
    while len(numbers_result) < 6:
        # Generate a random number between 1 and 49
        number = random.randint(1, 49)
        # Add the number to the set so there won't be any duplicates
        numbers_result.add(number)
        # We could also use random.sample(range(1, 50), 6) but I think this is more readable 
        
    # Our list is ready so we will sort it now to present them in numerical order as required
    numbers_result = sorted(numbers_result)
    
    # Now we will generate the bonus ball between 1 and 49
    # We will use a while loop to make sure the bonus ball is not in the original 6 numbers
    bonus_ball = random.randint(1, 49)
    while bonus_ball in numbers_result:
        bonus_ball = random.randint(1, 49)
        
    # Now we will return the numbers and the bonus ball. We will send request and pull the data from the frontend
    return LotteryNumbers(numbers=numbers_result, bonus_ball=bonus_ball)
    
    
# I wanted to demonstrate how to use the Python and FastAPI to create a simple API. I could also make it with Node.js and Fastify or Express.js. I could apply similar approach.

# In future we can add more endpoints to the API:
# For example we can add an endpoint to get the history of the numbers and create a new page that holds all history of the lotteries so eveyrone can see the history
# We can add User and Authentication to the API so we can store the history of the numbers for each user


# Also we can dockerize the app and deploy it to a cloud provider like AWS. We can use AWS Lambda to deploy the app and use AWS API Gateway to create an API for the app. 
# To turn it to a Serverless app if we don't want to use a server or we can use AWS EC2 to deploy the app and use AWS RDS to store the data.

# Alteraantively, we can deploy it in Kubernetes cluster in the cloud and manage in there

