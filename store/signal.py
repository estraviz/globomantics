from django.dispatch import receiver, Signal

# Create a custom signal
request_signal = Signal()


class RequestResponseDemo(object):
    # Function to send the signal
    def send(self):
        print("Http Request Sent.")
        request_signal.send(sender=self.__class__, Request=True)


# Function to receive the signal
@receiver(request_signal)
def receive(**kwargs):
    if kwargs.get('Request'):
        print("Http Request Received.")


demo = RequestResponseDemo()
demo.send()
