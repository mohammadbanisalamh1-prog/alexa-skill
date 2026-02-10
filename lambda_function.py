def lambda_handler(event, context):
    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "مرحبًا، هذه أول مهارة أليكسا لي"
            },
            "shouldEndSession": True
        }
    }
