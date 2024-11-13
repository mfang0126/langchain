import random
from datetime import datetime, timedelta

def generate_mock_conversations(num_conversations=10):
    topics = ["product inquiry", "technical support", "billing issue", "general inquiry"]
    products = ["laptop", "smartphone", "tablet", "smartwatch"]
    clients = ["Alice", "Bob", "Charlie", "David", "Eva"]

    conversations = []
    
    for _ in range(num_conversations):
        topic = random.choice(topics)
        product = random.choice(products) if topic == "product inquiry" else ""
        client = random.choice(clients)
        date = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
        
        if topic == "product inquiry":
            content = f"Client: Hi, I'm interested in your {product}. Can you tell me more about its features?\n"
            content += f"Agent: Certainly! Our {product} comes with the latest technology. What specific features are you most interested in?\n"
            content += f"Client: I'm particularly curious about its battery life and processing power.\n"
            content += f"Agent: Great question! The {product} has an impressive 12-hour battery life and is powered by the latest processor for optimal performance."
        elif topic == "technical support":
            content = f"Client: I'm having trouble with my device. It won't turn on.\n"
            content += f"Agent: I'm sorry to hear that. Let's try a few troubleshooting steps. First, have you tried holding the power button for 10 seconds?\n"
            content += f"Client: Yes, I tried that but it didn't work.\n"
            content += f"Agent: Okay, let's try connecting it to a power source for about 15 minutes and then attempt to turn it on again."
        elif topic == "billing issue":
            content = f"Client: I think there's an error on my latest bill.\n"
            content += f"Agent: I apologize for any inconvenience. Can you please provide your account number so I can look into this for you?\n"
            content += f"Client: Sure, it's AC123456.\n"
            content += f"Agent: Thank you. I see the issue. There was indeed an error in calculation. I'll process a refund for the overcharged amount immediately."
        else:  # general inquiry
            content = f"Client: What are your customer service hours?\n"
            content += f"Agent: Our customer service team is available 24/7 to assist you with any queries or concerns.\n"
            content += f"Client: That's great to know. Thank you!\n"
            content += f"Agent: You're welcome! Is there anything else I can help you with today?"

        conversation = {
            "content": content,
            "metadata": {
                "client_name": client,
                "conversation_topic": topic,
                "product": product,
                "date": date
            }
        }
        conversations.append(conversation)
    
    return conversations
