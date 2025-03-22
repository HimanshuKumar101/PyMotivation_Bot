# PyMotivator

PyMotivator is a Python project that sends motivational quotes to a specified phone number using the Twilio API. The project uses the `apscheduler` library to schedule the sending of messages at specific times.

## Prerequisites

- Python 3.6 or higher
- Twilio account with an account SID and auth token
- Virtual environment (optional but recommended)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/PyMotivation_Bot.git
   cd PyMotivator
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv env
   .\env\Scripts\activate  # For Windows
   source env/bin/activate  # For macOS/Linux
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Set the environment variables for Twilio:
   ```sh
   $env:TWILIO_ACCOUNT_SID = "your_account_sid"
   $env:TWILIO_AUTH_TOKEN = "your_auth_token"
   $env:PHONE = "recipient_phone_number"
   ```

## Usage

1. Run the `motivator.py` script to send a motivational quote immediately:
   ```sh
   python motivator.py
   ```

2. Run the `cron.py` script to schedule sending motivational quotes at specific times:
   ```sh
   python cron.py
   ```

## Project Structure

- `motivator.py`: Fetches a random motivational quote and sends it using Twilio.
- `twilio_conn.py`: Contains functions to set up the Twilio client and send messages.
- `cron.py`: Schedules the sending of motivational quotes using `apscheduler`.
- `config.py`: Loads environment variables for Twilio credentials and phone number.

