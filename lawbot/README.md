# LawBot Project

Welcome to the LawBot project! The Law Chatbot is a conversational AI application designed to assist users with legal inquiries, providing information, guidance, and answers to common legal questions. Whether users are seeking legal advice or general information, the chatbot aims to facilitate a user-friendly and accessible interface for navigating legal topics.


## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Authors](#authors)

## Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 installed on your system.
- [Optional] Virtual Environment

### Installation

1. Clone the repository to your local machine:

   ```
   bash
   git clone https://gitlab.aisingapore.net/aiap/deep-skilling-phase/aiap15/aiap-15-mini-project/jokegen.git
   ```

2. Navigate to the project directory:

   ```
   cd jokegen
   ```
   
3. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate
   ```
4. Running the Backend Development Server (Start the FastAPI development server):

   Build the backend Docker image:

   ```
   bash
   docker build --no-cache -t backend:v0 -f backend.DockerFile .

   chmod 755 run_docker_build.sh
   ./run_docker_build.sh

   chmod 755 run_backend_docker.sh
   ./run_backend_docker.sh
   
    ```
    Configure the parameters for each response fields with its specified value.
   <img width="1372" alt="image" src="images/Screenshot 2024-03-11 at 17.03.14 (2).png">

5. Running the Frontend Development Server (Streamlit)
   ```
   chmod 755 run_frontend.sh
   ./run.sh
   ``` 

## Authors
| **Author**            | **Email** |
|-------------          |--------------|
| Low Shi Jer  |  low_shi_jer@aiap.sg   |
| Wai Jin Hui  |  wai_jin_hui@aiap.sg   |
| Jerald Han Wang Liang  |  jerald_han_wl@aiap.sg   |
| Crystal Toh Yi Shan  |  crystal_toh_ys@aiap.sg   |