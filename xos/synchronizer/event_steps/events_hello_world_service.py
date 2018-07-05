from xosconfig import Config
from multistructlog import create_logger
import json
from synchronizers.new_base.eventstep import EventStep
from synchronizers.new_base.modelaccessor import HelloWorldServiceInstance

log = create_logger(Config().get('logging'))


class HelloWorldServiceInstanceEventStep(EventStep):
    technology = "kafka"
    topics = ["MyTopic"]

    def __init__(self, *args, **kwargs):
        super(HelloWorldServiceInstanceEventStep, self).__init__(*args, **kwargs)

    def process_event(self, event):
        log.info("event HelloWorldServiceInstance")

        value = json.loads(event.value)

        if HelloWorldServiceInstance.objects.filter(name=value.name, hello_to=value.hello_to):
            log.info("Event with nothing new!")
            return

        # create an empty model
        o = HelloWorldServiceInstance()
        # code to fetch information
        # populate the model
        o.hello_to = value.name
        o.name = value.hello_to
        o.save(always_update_timestamp=True)
