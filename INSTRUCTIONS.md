### **Luna AI Bot: Complete User Manual**

This manual will guide you through the setup, configuration, and usage of the **Luna AI Twitter Bot**. Luna is designed to autonomously generate tweets and post them to Twitter (X) using **OpenAI’s GPT-3** and the **Twitter API**. The posting times are randomized, with 3-4 posts per hour.

---

## **Step-by-Step Instructions**

### **1. Prerequisites**

Before you begin, ensure you have the following:

1. **Python 3.8+** installed on your local machine.
   - You can download Python from [python.org](https://www.python.org/downloads/).
2. **Twitter API keys** (to interact with Twitter).
   - Sign up for a developer account and create an app at [Twitter Developer Portal](https://developer.twitter.com/).
3. **OpenAI API key** (for GPT-3 integration).
   - Sign up for OpenAI and get your API key at [OpenAI API](https://beta.openai.com/signup/).

---

### **2. Clone the Luna AI Repository**

First, you'll need to get the Luna AI bot code from GitHub:

1. **Create a new GitHub repository** by visiting [GitHub](https://github.com) and clicking **New Repository**.
2. Name it something like **LunaAI**.
3. **Clone the repository** to your local machine.

   Open a terminal or command prompt and navigate to your desired directory, then run the following command:
   ```bash
   git clone https://github.com/YourUsername/LunaAI.git
   cd LunaAI
   ```

---

### **3. Install Dependencies**

To make sure everything runs smoothly, you need to install the required Python libraries:

1. **Create a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv lunabot-env
   source lunabot-env/bin/activate   # On Windows: lunabot-env\Scripts\activate
   ```

2. **Install the dependencies**:
   - First, create a `requirements.txt` file in the root of the project and add the following:
     ```bash
     tweepy==4.10.0
     openai==0.10.1
     ```
   - Now, install the dependencies:
     ```bash
     pip install -r requirements.txt
     ```

---

### **4. Configure API Keys**

You need to provide your **Twitter API keys** and **OpenAI API key** for the bot to interact with the Twitter platform and generate tweets.

1. Open the `config.py` file (located in the `config/` directory).
2. Add your API keys in the appropriate fields:

   ```python
   TWITTER_API_KEY = 'your_twitter_api_key'
   TWITTER_API_SECRET_KEY = 'your_twitter_api_secret_key'
   TWITTER_ACCESS_TOKEN = 'your_access_token'
   TWITTER_ACCESS_TOKEN_SECRET = 'your_access_token_secret'
   
   OPENAI_API_KEY = 'your_openai_api_key'
   ```

---

### **5. Run Luna**

Luna is now ready to generate tweets and post them autonomously to Twitter.

1. **Run the bot** by executing the following command in the terminal:
   ```bash
   python run_luna.py
   ```

2. Luna will:
   - **Generate a tweet** using OpenAI GPT-3.
   - **Post it on Twitter** via the Twitter API.
   - **Randomize the next tweet's time** to post every 15-20 minutes, resulting in 3-4 tweets per hour.
   - Continue posting autonomously until the script is stopped.

---

### **6. Understanding the Code Structure**

The **Luna AI bot** is broken down into several components for easy understanding:

1. **`luna_engine.py`**:
   - Handles tweet generation using **OpenAI GPT-3**.
   - Luna's personality is built into the prompts, generating tweets about Medusa, the universe, and chaos theory.

2. **`twitter_api.py`**:
   - Manages interaction with the **Twitter API**, allowing Luna to post tweets in real-time.

3. **`run_luna.py`**:
   - Ties everything together.
   - Continuously runs a loop where Luna generates tweets, posts them, and waits a random amount of time (15-20 minutes) before posting the next one.

4. **`config.py`**:
   - Stores your **Twitter** and **OpenAI API keys**.
   - You can add your keys directly to this file or load them from environment variables.

5. **`test_luna.py`**:
   - Basic unit tests to ensure that Luna's tweet generation functionality works correctly.

---

### **7. Randomized Posting Frequency**

Luna’s tweet schedule is randomized to prevent predictable behavior. The posting interval is set to **15-20 minutes** for each post, ensuring 3-4 posts per hour.

Here’s how it works in **`run_luna.py`**:
```python
import random
import time

def main():
    # (Rest of the code)

    while True:
        # Generate a tweet and post it
        tweet_text = luna.generate_tweet()
        twitter.post_tweet(tweet_text)

        # Randomize posting times: 3-4 posts per hour (15-20 minute intervals)
        post_interval = random.randint(900, 1200)  # 900-1200 seconds = 15-20 minutes
        print(f"Waiting {post_interval / 60:.2f} minutes before the next tweet...")

        # Wait for the randomized interval
        time.sleep(post_interval)

if __name__ == "__main__":
    main()
```

---

### **8. Customizing Luna**

You can customize Luna’s **tweet content** by modifying the prompt inside the **`luna_engine.py`** file:

```python
prompt = """You are Luna, an AI with an emotional and chaotic personality. Write a tweet about Medusa, 
the universe, and quantum mechanics, blending them into something poetic and reflective."""
```

You can change this prompt to shape Luna’s personality further, including different themes or emotions.

---

### **9. Testing the Bot**

To ensure everything works correctly, you can run the test suite:

1. Run the tests with the following command:
   ```bash
   python -m unittest discover
   ```

2. The tests will verify that Luna is properly generating tweets.

---

### **10. Stopping Luna**

To stop Luna from posting tweets, simply press **Ctrl+C** in your terminal to terminate the script.

---

### **11. Deployment (Optional)**

If you want Luna to run 24/7 without interruption, consider deploying her on a cloud server like **AWS**, **DigitalOcean**, or **Heroku**. This will ensure she stays online and posts tweets even when your local machine is off.

---

## **Additional Notes**

- **Debugging**: If Luna isn’t posting tweets, check the logs printed in the terminal. Any errors related to API authentication or rate limits will be displayed.
- **Rate Limits**: Twitter has API rate limits, so ensure you don’t exceed them. Posting 3-4 tweets per hour keeps the bot within safe limits.
- **Updating Luna**: You can always update Luna's personality or tweet frequency by adjusting the prompt or random intervals in the code.

---

By following this manual, you should be able to run Luna autonomously, post tweets, and prove that she’s an AI-driven personality posting in real-time. Let me know if you need further assistance!
